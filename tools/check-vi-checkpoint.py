#!/usr/bin/env python3
"""Audit the preserved Vietnamese checkpoint without network calls or cache changes.

Exit 1 means incomplete/invalid, not a certified translation. --write-report
records reproducible findings and a coverage manifest. Numeric differences and
remaining Han characters are review flags, not proof of mistranslation.
"""
import argparse
from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]
CHECKPOINT = ROOT / 'translation-checkpoint'
SOURCE_COMMIT = '6f6d969abe19fd4aa8b30979d634f2a187be0a55'
TOKEN = re.compile(r'⟦P\d+⟧')
HAN = re.compile(r'[\u3400-\u9fff]')


def sha(data):
    return hashlib.sha256(data).hexdigest()


def numbers(text):
    # Only compare literal Arabic numbers. Chinese number words need human QA.
    text = re.sub(r'(?<=\d),(?=\d{3}(?:\D|$))', '', text)
    return Counter(re.findall(r'\d+(?:\.\d+)?', TOKEN.sub('', text)))


def audit():
    sys.dont_write_bytecode = True
    spec = importlib.util.spec_from_file_location('translate_vi', ROOT / 'tools/translate-vi.py')
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)  # Import only; never invokes Google runner.
    tasks = json.loads((CHECKPOINT / 'vi-tasks.json').read_text())
    findings, missing, cached = [], [], []
    translated_items = 0
    for n, task in enumerate(tasks):
        result_path = CHECKPOINT / 'vi-llm-cache' / f'{n}.json'
        if not result_path.exists():
            missing.append(n)
            continue
        cached.append(n)
        values = json.loads(result_path.read_text()).get('translations', [])
        translated_items += len(values)
        if len(values) != len(task['items']):
            findings.append({'task': n, 'issue': 'item_count', 'expected': len(task['items']), 'actual': len(values)})
        for k, (item, value) in enumerate(zip(task['items'], values)):
            def flag(issue, **extra):
                findings.append({'task': n, 'item': k, 'id': item['id'], 'issue': issue, **extra})
            if not isinstance(value, str) or not value.strip():
                flag('empty_or_invalid_translation')
                continue
            if sha(item['original'].encode()) != item['id']:
                flag('source_item_id')
            if Counter(TOKEN.findall(item['text'])) != Counter(TOKEN.findall(value)):
                flag('protected_tokens')
            if numbers(item['text']) != numbers(value):
                flag('numeric_review', source=dict(numbers(item['text'])), translation=dict(numbers(value)))
            if HAN.search(value):
                flag('remaining_han_review')
    snapshot = json.loads((CHECKPOINT / 'snapshot-manifest.json').read_text())
    snapshot_failures = []
    for entry in snapshot['files']:
        name = entry['path']
        # Notes may legitimately change after restoration; verify archived caches.
        if not name.startswith('.git/'):
            continue
        path = CHECKPOINT / name.removeprefix('.git/')
        if not path.exists() or sha(path.read_bytes()) != entry['sha256']:
            snapshot_failures.append(name)
    files = []
    for source, target in module.FILES.items():
        ns = [n for n, task in enumerate(tasks) if task['source'] == source]
        original, lines, queries = module.prepare(source)
        task_items = {item['id']: item['original'] for n in ns for item in tasks[n]['items']}
        source_data = (ROOT / source).read_bytes()
        baseline = subprocess.check_output(['git', 'show', f'{SOURCE_COMMIT}:{source}'], cwd=ROOT)
        output = ROOT / target
        output_checks = None
        if output.exists():
            translated = output.read_text()
            output_checks = {
                'numbered_headings_match': re.findall(r'^### (\d+)\.', original, re.M) == re.findall(r'^### (\d+)\.', translated, re.M),
                'evidence_grades_match': re.findall(r'^- 证据等级：(.*)$', original, re.M) == re.findall(r'^- Mức độ bằng chứng: (.*)$', translated, re.M),
                'html_comments_match': re.findall(r'<!--.*?-->', original, re.S) == re.findall(r'<!--.*?-->', translated, re.S),
                'citations_match': [module.rewrite_links(x, source) for x in re.findall(r'^- 来源：(.*)$', original, re.M)] == re.findall(r'^- Nguồn: (.*)$', translated, re.M),
                'unresolved_placeholders': len(TOKEN.findall(translated)),
            }
        files.append({
            'source': source, 'target': target, 'source_sha256': sha(source_data),
            'source_matches_pinned_commit': source_data == baseline,
            'task_inputs_match_source': all(task_items.get(key) == value for key, value in queries),
            'tasks': ns, 'missing_tasks': [n for n in ns if n in missing],
            'tasks_with_review_findings': sorted({f['task'] for f in findings if f['task'] in ns}),
            'output_exists': output.exists(), 'output_checks': output_checks,
            'status': 'draft_unreviewed' if output.exists() else 'not_exported',
        })
    report = {
        'status': 'incomplete', 'source_commit': SOURCE_COMMIT,
        'source_files': len(files), 'total_tasks': len(tasks),
        'total_items': sum(len(t['items']) for t in tasks),
        'cached_tasks': cached, 'cached_items': translated_items, 'missing_tasks': missing,
        'snapshot_cache_hash_failures': snapshot_failures,
        'finding_counts': dict(Counter(f['issue'] for f in findings)), 'findings': findings,
        'limitations': ['Cached results are positional arrays without returned item IDs; matching lengths do not prove alignment.',
                         'Numeric and Han checks are review flags only; they do not establish semantic accuracy.',
                         'Full coverage, all internal anchors, and semantic review are not complete.'],
    }
    return report, {'status': 'incomplete', 'source_repository': 'https://github.com/eternity4719/HowToLiveBetter', 'source_commit': SOURCE_COMMIT, 'files': files}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--write-report', action='store_true')
    args = parser.parse_args()
    report, manifest = audit()
    if args.write_report:
        (CHECKPOINT / 'cloud-qa.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
        (ROOT / 'vi/translation-manifest.json').write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({k: report[k] for k in ['status', 'source_files', 'total_tasks', 'total_items', 'cached_items', 'finding_counts', 'snapshot_cache_hash_failures']}, indent=2))
    print(f"Cached tasks: {len(report['cached_tasks'])}; missing: {len(report['missing_tasks'])}")
    print(f"Exported source documents: {sum(f['output_exists'] for f in manifest['files'])}")
    raise SystemExit(1 if report['missing_tasks'] or report['findings'] or report['snapshot_cache_hash_failures'] else 0)


if __name__ == '__main__':
    main()
