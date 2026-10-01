# Vietnamese translation checkpoint

This is an unfinished translation checkpoint for the personal fork `ibretsam/HowToLiveBetter`. Keep translation work in the fork; the upstream project explicitly does not accept translated content.

Source: https://github.com/eternity4719/HowToLiveBetter, commit `6f6d969abe19fd4aa8b30979d634f2a187be0a55` (2026-10-01).

## Captured progress

- 43 source documents: README, 34 book chapters, and eight reader-facing long articles; the translation notes describe 649 book entries.
- 137 translation tasks contain 4,103 text items. The 26 captured Workers AI task results contain 993 translated items.
- Cached task IDs: 0–12, 14–25, and 83. Missing IDs: 13, 26–82, and 84–136 (111 tasks).
- Produced files: `vi/TRANSLATION.md` and `vi/book/18.md`. Only chapter 18 is emitted as a translated source document; the other 42 source documents still need assembled output and review.
- `vi/README.md`, `vi/translation-manifest.json`, and `tools/check-vi.py` are referenced by the notes but do not exist yet. Do not present the translation as complete or fully validated.
- `progress.json` lists exact per-source cached and missing task IDs. `snapshot-manifest.json` records the original paths, sizes, SHA-256 hashes, and capture timestamp.

## Restore caches

Run from the repository root in a new checkout of this checkpoint branch. These commands restore the original working-cache locations without overwriting existing cache files:

```sh
python3 - <<'PYRESTORE'
from pathlib import Path
import shutil, subprocess
root = Path.cwd()
git_dir = Path(subprocess.check_output(['git', 'rev-parse', '--git-dir'], text=True).strip())
if not git_dir.is_absolute():
    git_dir = root / git_dir
checkpoint = root / 'translation-checkpoint'
for name in ['vi-tasks.json', 'translation-vi-cache.json']:
    target = git_dir / name
    if not target.exists():
        shutil.copy2(checkpoint / name, target)
cache = git_dir / 'vi-llm-cache'
cache.mkdir(parents=True, exist_ok=True)
for source in (checkpoint / 'vi-llm-cache').glob('*.json'):
    target = cache / source.name
    if not target.exists():
        shutil.copy2(source, target)
PYRESTORE
```

## Continue the work

Read `AGENTS.md`, `CLAUDE.md`, and `vi/TRANSLATION.md` before editing. Reuse the cached Workers AI outputs by task index from `vi-tasks.json`. Each task identifies its source and an ordered list of items with `id`, `text`, `tokens`, and `original`; result files hold `translations`, `usage`, and `model`. Verify item IDs/counts and protected-token preservation before assembling files. Complete only missing or invalid tasks; preserve the existing chapter 18 draft for comparison and review.

The captured `tools/translate-vi.py` is an earlier Google Translate implementation and uses the separate `translation-vi-cache.json` (478 entries). It does not resume the Workers AI cache. The Workers AI runner itself was not present in the captured repository; recreate that runner using the task/result schemas and authorized cloud execution tools. No runtime credentials or personal session data are included. Do not blindly rerun the Google script as if it resumed Workers AI.

Preserve the source's meaning, conditions, negations, chapter/item numbering, evidence grades, all quantities, statistical notation, HTML metadata, citations, and reference bibliography. Translate reader-facing prose into clear Vietnamese, retain original citation titles for traceability, and repair relative links for `vi/`. Keep the mainland China legal, healthcare, benefits, emergency-number, and CNY context; do not substitute Vietnamese policies. Keep attribution, CC BY 4.0 licensing, source revision, and unofficial machine-draft status. Do not translate or alter contributor tooling, AI skills, or source verification logs as reader-facing content.

After completion, create the manifest and checks that the notes promise; verify coverage, numbering, quantities, evidence grades, protected tokens, references, and internal links, then review translation quality. Change claims about checks in `vi/TRANSLATION.md` to match what was actually verified. This checkpoint does not itself establish translation accuracy or completion.
