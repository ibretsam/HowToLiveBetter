#!/usr/bin/env python3
"""Check all current Vietnamese translations against pinned public source.

Default: complete translation required, exit 1 for any failure. --partial audits
available results without treating incomplete coverage as a failure. It never
calls a service or certifies clinical/legal correctness or professional editing.
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
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
CP = ROOT / 'translation-checkpoint'
SOURCE = '6f6d969abe19fd4aa8b30979d634f2a187be0a55'
REVIEWED = CP / 'vi-reviewed-cache'
TOKEN = re.compile(r'⟦P\d+⟧')
HAN = re.compile(r'[\u3400-\u9fff]')
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('assembler', ROOT / 'tools/assemble-vi.py')
assembler = importlib.util.module_from_spec(spec)
spec.loader.exec_module(assembler)
base = assembler.base


def digest(data):
    return hashlib.sha256(data).hexdigest()


def numbers(text):
    return Counter(re.findall(r'\d+(?:\.\d+)?', TOKEN.sub('', text)))


def heading_slug(text):
    text = re.sub(r'<[^>]*>', '', text).lower().strip()
    text = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return ''.join(c for c in text if c.isalnum() or c in '-_ ').replace(' ', '-')


def markdown_headings(text):
    code = False
    counts, anchors = Counter(), set()
    for line in text.splitlines():
        if line.startswith('```'):
            code = not code
        if code:
            continue
        match = re.match(r'^#{1,6}\s+(.*)$', line)
        if match:
            slug = heading_slug(match[1])
            n = counts[slug]
            counts[slug] += 1
            anchors.add(slug + (f'-{n}' if n else ''))
    anchors.update(re.findall(r'<a\s+id="([^"]+)"', text))
    return anchors


def audit(partial=False):
    tasks = json.loads((CP / 'vi-tasks.json').read_text())
    failures, review_flags, complete = [], [], []
    items = 0
    for n, task in enumerate(tasks):
        path = REVIEWED / f'{n}.json'
        if not path.exists():
            continue
        d = json.loads(path.read_text())
        values = d.get('translations', [])
        if d.get('item_ids') != [i['id'] for i in task['items']]:
            failures.append({'task':n,'issue':'ordered_ids'})
        if len(values) != len(task['items']):
            failures.append({'task':n,'issue':'item_count'})
        for k, (item, value) in enumerate(zip(task['items'], values)):
            if not isinstance(value, str) or not value.strip():
                failures.append({'task':n,'item':k,'issue':'empty'})
                continue
            if Counter(TOKEN.findall(value)) != Counter(TOKEN.findall(item['text'])):
                failures.append({'task':n,'item':k,'issue':'protected_tokens'})
            if numbers(value) != numbers(item['text']):
                failures.append({'task':n,'item':k,'issue':'numbers','missing':dict(numbers(item['text'])-numbers(value)),'extra':dict(numbers(value)-numbers(item['text']))})
            # Source paths/titles retained for attribution are explicit review flags.
            if HAN.search(value):
                review_flags.append({'task':n,'item':k,'issue':'retained_han','text':value})
        complete.append(n)
        items += len(values)
    missing = sorted(set(range(len(tasks))) - set(complete))
    if missing and not partial:
        failures.append({'issue':'missing_tasks','tasks':missing})
    exported, entries, manifests = 0, 0, []
    for source, target in base.FILES.items():
        raw = (ROOT / source).read_bytes()
        baseline = subprocess.check_output(['git','show',f'{SOURCE}:{source}'],cwd=ROOT)
        if raw != baseline:
            failures.append({'source':source,'issue':'source_revision'})
        ns = [n for n,t in enumerate(tasks) if t['source']==source]
        original, lines, queries = base.prepare(source)
        task_inputs = {i['id']:i['original'] for n in ns for i in tasks[n]['items']}
        if any(task_inputs.get(key)!=value for key,value in queries):
            failures.append({'source':source,'issue':'task_source_inputs'})
        path = ROOT / target
        checked = {}
        if path.exists():
            exported += 1
            text = path.read_text()
            if source.startswith('book/'):
                entries += len(re.findall(r'^### \d+\.',text,re.M))
            checked['numbered_headings'] = re.findall(r'^### (\d+)\.',original,re.M)==re.findall(r'^### (\d+)\.',text,re.M)
            checked['evidence_grades'] = [assembler.evidence_annotation(s) for s in re.findall(r'^- 证据等级：(.*)$',original,re.M)]==re.findall(r'^- Mức độ bằng chứng: (.*)$',text,re.M)
            checked['html_comments'] = re.findall(r'<!--.*?-->',original,re.S)==re.findall(r'<!--.*?-->',text,re.S)
            checked['citations'] = [base.rewrite_links(s,source) for s in re.findall(r'^- 来源：(.*)$',original,re.M)]==re.findall(r'^- Nguồn: (.*)$',text,re.M)
            checked['no_placeholders'] = not TOKEN.search(text)
            checked['complete_task_coverage'] = all(n in complete for n in ns)
            # All externally linked destinations remain identical (including image URLs).
            urls=lambda s:Counter(u.rstrip('.,;:') for u in re.findall(r'https?://[^\s<>"`）)。]+',s))
            checked['external_urls'] = urls(original)==urls(text)
            checked['heading_structure'] = [m[0] for m in re.findall(r'^(#{1,6})\s+(.+)$',original,re.M)]==[m[0] for m in re.findall(r'^(#{1,6})\s+(.+)$',text,re.M)]
            code_pattern = r'^```.*?^```[^\n]*'
            source_prose = re.sub(code_pattern,'',original,flags=re.M|re.S)
            target_prose = re.sub(code_pattern,'',text,flags=re.M|re.S)
            checked['entry_fields'] = all(
                len(re.findall(r'^- '+re.escape(src)+r'：',source_prose,re.M)) ==
                len(re.findall(r'^- '+re.escape(dst)+r': ',target_prose,re.M))
                for src,dst in [('成本','Chi phí'),('说人话','Nói dễ hiểu'),
                                ('收益','Lợi ích'),('备注','Ghi chú')])
            expected_code = assembler.code_overrides(source,base.rewrite_links(original,source))
            checked['code_blocks'] = re.findall(code_pattern,expected_code,re.M|re.S)==re.findall(code_pattern,text,re.M|re.S)
            checked['code_example_numbers'] = numbers('\n'.join(re.findall(code_pattern,original,re.M|re.S)))==numbers('\n'.join(re.findall(code_pattern,text,re.M|re.S)))
            checked['table_structure'] = [line.count('|') for line in original.splitlines() if line.startswith('|')]==[line.count('|') for line in text.splitlines() if line.startswith('|')]
            for key, ok in checked.items():
                if not ok:
                    failures.append({'target':target,'issue':key})
            # Paths are checked separately from fragments, which need translated anchors.
            for match in re.finditer(r'\]\(([^)]+)\)|\b(?:src|href)="([^"]+)"',text):
                url = match[1] or match[2]
                if re.match(r'^(?:https?://|mailto:|data:)',url):
                    continue
                dest,_,frag = url.partition('#')
                p = (path.parent / urllib.parse.unquote(dest)).resolve() if dest else path
                if not p.exists():
                    if not partial:
                        failures.append({'target':target,'issue':'relative_path','url':url})
                elif frag and p.suffix=='.md':
                    if urllib.parse.unquote(frag) not in markdown_headings(p.read_text()):
                        failures.append({'target':target,'issue':'internal_anchor','url':url})
        elif not partial:
            failures.append({'target':target,'issue':'missing_output'})
        manifests.append({'source':source,'target':target,'source_sha256':digest(raw),'translation_sha256':digest(path.read_bytes()) if path.exists() else None,'tasks':ns,'missing_tasks':[n for n in ns if n not in complete],'checks':checked,'status':'translated_ai_draft' if path.exists() and all(n in complete for n in ns) else 'incomplete'})
    report={'status':'passed' if not failures and not missing else 'incomplete' if missing else 'failed','source_commit':SOURCE,'source_documents':len(base.FILES),'total_tasks':len(tasks),'total_items':sum(len(t['items']) for t in tasks),'reviewed_tasks':len(complete),'reviewed_items':items,'missing_tasks':missing,'exported_documents':exported,'book_entries':entries,'failure_counts':dict(Counter(x['issue'] for x in failures)),'failures':failures,'review_flags':review_flags,'limitations':['Automated invariants do not certify every translated sentence or medical/legal advice.','The source policies and evidence are translated at the pinned revision, not independently updated.']}
    manifest={'status':report['status'],'source_repository':'https://github.com/eternity4719/HowToLiveBetter','source_commit':SOURCE,'license':'CC BY 4.0','method':'direct model translation with item IDs; preserved Workers AI cache retained for comparison','files':manifests}
    return report,manifest


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--partial',action='store_true')
    p.add_argument('--write-report',action='store_true')
    a=p.parse_args()
    report,manifest=audit(a.partial)
    if a.write_report:
        (CP/'current-qa.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
        (ROOT/'vi/translation-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
    print(json.dumps({k:report[k] for k in ['status','reviewed_tasks','reviewed_items','exported_documents','book_entries','failure_counts']},indent=2))
    raise SystemExit(1 if report['failures'] else 0)


if __name__=='__main__':main()
