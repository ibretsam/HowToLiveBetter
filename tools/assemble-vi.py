#!/usr/bin/env python3
"""Assemble ID-validated direct translations; never calls translation services."""
import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import re
import sys
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
CP = ROOT / 'translation-checkpoint'
REVIEWED = CP / 'vi-reviewed-cache'
TOKEN = re.compile(r'⟦P\d+⟧')
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('translate_vi', ROOT / 'tools/translate-vi.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


def slug(text):
    text = re.sub(r'<[^>]*>', '', text).lower().strip()
    text = re.sub(r'!?\[([^\]]+)\]\([^)]*\)', r'\1', text)
    return ''.join(c for c in text if c.isalnum() or c in '-_ ').replace(' ', '-')


def headings(text):
    counts, result, code = Counter(), [], False
    for line in text.splitlines():
        if line.startswith('```'):
            code = not code
        if code:
            continue
        m = re.match(r'^#{1,6}\s+(.*)$', line)
        if m:
            s = slug(m[1]); n = counts[s]; counts[s] += 1
            result.append(s + (f'-{n}' if n else ''))
    return result


def repair_anchors(written):
    maps = {}
    for source, target in base.FILES.items():
        path = ROOT / target
        if not path.exists():
            continue
        old, new = headings((ROOT/source).read_text()), headings(path.read_text())
        assert len(old) == len(new), target
        maps[path.resolve()] = dict(zip(old, new))
    for target in written:
        path = ROOT / target
        def replace(m):
            url = m[2]
            if re.match(r'^(?:https?://|mailto:|data:)',url):
                return m[0]
            dest, sep, fragment = url.partition('#')
            resolved = (path.parent / urllib.parse.unquote(dest)).resolve() if dest else path.resolve()
            mapped = maps.get(resolved,{}).get(urllib.parse.unquote(fragment))
            return m[1] + dest + sep + mapped + m[3] if sep and mapped else m[0]
        path.write_text(re.sub(r'(\]\()([^)]+)(\))', replace, path.read_text()))


def load_cache():
    tasks = json.loads((CP / 'vi-tasks.json').read_text())
    by_source, cache, complete = {}, {}, []
    overrides = {}
    for path in REVIEWED.glob('token-overrides-*.json'):
        overrides.update(json.loads(path.read_text()))
    for n, task in enumerate(tasks):
        by_source.setdefault(task['source'], []).append(n)
        path = REVIEWED / f'{n}.json'
        if not path.exists():
            continue
        result = json.loads(path.read_text())
        assert result['item_ids'] == [i['id'] for i in task['items']], f'IDs mismatch task {n}'
        assert len(result['translations']) == len(task['items']), f'Count mismatch task {n}'
        for k, (item, value) in enumerate(zip(task['items'], result['translations'])):
            assert isinstance(value, str) and value.strip(), f'Empty {n}:{k}'
            assert Counter(TOKEN.findall(value)) == Counter(TOKEN.findall(item['text'])), f'Placeholders {n}:{k}'
            tokens = [overrides.get(f'{n}:{k}:{j}', token) for j, token in enumerate(item['tokens'])]
            translated = base.unprotect(value, tokens)
            if item['id'] in cache and cache[item['id']] != translated:
                # Identical source strings may be translated naturally more than once.
                # Use first result consistently; no source content is lost.
                continue
            cache[item['id']] = translated
        complete.append(n)
    return tasks, by_source, cache, complete


def code_overrides(source, text):
    path = REVIEWED / 'code-overrides.json'
    data = json.loads(path.read_text()) if path.exists() else {}
    for entry in data.get(source, []):
        old = base.rewrite_links(entry['source'], source)
        if old not in text:
            # The captured preparer relabels bibliography/evidence fields even
            # inside fenced examples. Accept that deterministic intermediate.
            old = re.sub(r'^- 证据等级：', '- Mức độ bằng chứng: ', old, flags=re.M)
            old = re.sub(r'^- 来源：', '- Nguồn: ', old, flags=re.M)
        assert text.count(old) == 1, f'Code example source mismatch: {source}'
        text = text.replace(old, entry['translation'])
    return text


def evidence_annotation(value):
    return value.replace('（争议）', ' (có tranh luận)').replace(
        '（指南强推荐，但底层证据等级低）',
        ' (hướng dẫn khuyến nghị mạnh, nhưng mức độ bằng chứng nền tảng thấp)')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--partial', action='store_true', help='Export only complete source files')
    args = parser.parse_args()
    tasks, by_source, cache, complete = load_cache()
    missing = sorted(set(range(len(tasks))) - set(complete))
    if missing and not args.partial:
        raise SystemExit(f'Missing reviewed tasks: {missing}')
    written = []
    for source, target in base.FILES.items():
        if any(n not in complete for n in by_source[source]):
            continue
        original, lines, queries = base.prepare(source)
        assert all(key in cache for key, _ in queries), source
        translated = [''.join(cache[value] if is_query else value for is_query, value in pieces) for pieces in lines]
        translated = [evidence_annotation(line) if line.startswith('- Mức độ bằng chứng: ') else line for line in translated]
        output = ROOT / target
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(base.notice(source) + code_overrides(source, '\n'.join(translated)) + '\n')
        written.append(target)
    repair_anchors(written)
    print(json.dumps({'reviewed_tasks':len(complete),'reviewed_items':sum(len(tasks[n]['items']) for n in complete),'exported_documents':len(written),'missing_tasks':missing}, indent=2))


if __name__ == '__main__':
    main()
