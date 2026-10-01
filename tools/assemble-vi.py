#!/usr/bin/env python3
"""Assemble ID-validated direct translations; never calls translation services."""
import argparse
from collections import Counter
import importlib.util
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CP = ROOT / 'translation-checkpoint'
REVIEWED = CP / 'vi-reviewed-cache'
TOKEN = re.compile(r'⟦P\d+⟧')
sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('translate_vi', ROOT / 'tools/translate-vi.py')
base = importlib.util.module_from_spec(spec)
spec.loader.exec_module(base)


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
        output = ROOT / target
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(base.notice(source) + '\n'.join(translated) + '\n')
        written.append(target)
    print(json.dumps({'reviewed_tasks':len(complete),'reviewed_items':sum(len(tasks[n]['items']) for n in complete),'exported_documents':len(written),'missing_tasks':missing}, indent=2))


if __name__ == '__main__':
    main()
