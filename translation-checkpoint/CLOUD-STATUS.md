# Cloud restoration and completed translation — 2026-10-01

Restored `codex/vietnamese-cloud-checkpoint` from commit
`6d88a2570e9ef99ad3c301eb8d020a655e3a54f0` in the cloud. All original cache
hashes match `snapshot-manifest.json`. The 43 source documents remain identical
to source commit `6f6d969abe19fd4aa8b30979d634f2a187be0a55`.
No credentials or personal files were copied. No Mac process was stopped.
Restoration, translation, assembly and checks run independently of the Mac.

## Completed coverage

- 137/137 planned batches; 4,103/4,103 text items with ordered source IDs.
- 43 translated reader documents: README, 34 chapters, eight long articles.
- 649 numbered book entries. Start reading at `vi/README.md`.
- README Markdown examples and command comments translated separately in
  `vi-reviewed-cache/code-overrides.json`.
- Source attribution, source revision and CC BY 4.0 license preserved.

The original checkpoint contained 26 Workers AI batches and 993 strings.
It had two Vietnamese files, of which only chapter 18 was a translated source
file. Its ID/order, truncation, placeholder and number problems are documented
in the historical `cloud-qa.json` and `tools/check-vi-checkpoint.py`.
The old caches and snapshots were preserved without modification. Complete,
ID-validated translations now live separately in `vi-reviewed-cache/`.

## Method and validation

Work continued with existing session models and native agents. No Workers AI
credential was needed, no Google Translate runner was restarted, and no paid
external service or new credential was used. Translations were compared with
source items; terse drafts were rewritten to restore explanations and qualifiers.

Reproduce current assembly and checks from the repository root:

```sh
python3 tools/assemble-vi.py
python3 tools/check-vi.py --write-report
node tools/check-plain.mjs
node tools/check-refs.mjs --check
node tools/sync-stats.mjs --check
```

`current-qa.json` and `vi/translation-manifest.json` record current checks:
source hashes and task inputs, complete coverage, IDs/order, protected tokens,
literal numeric tokens, entry numbering, evidence grades, citation text, HTML
comments, heading/field/table structure, code examples, external destinations,
relative paths and translated Markdown anchors. Current translation checks pass
with zero failures. The Node checks also pass for the unchanged Chinese source;
they do not certify Vietnamese prose quality.

Retained Chinese text is intentional in bibliographies, attribution, original
file destinations, searchable platform names and the distinct legal terms
`定金` / `订金`, with Vietnamese explanations. Mainland China law, emergency
numbers, healthcare, benefits and CNY amounts were not replaced with Vietnam's.

These are AI drafts with model-based review, not professional translation,
medical or legal approval. Automated checks cannot establish every sentence's
semantic accuracy or current factual validity. Source inconsistencies remain;
for example chapter 1's mushroom-poisoning entry contains an instruction to
induce vomiting that differs from other poisoning guidance. This report flags
the source wording, rather than silently rewriting it.

## Persistence and handoff

Translation changes are committed locally on the dedicated checkpoint branch.
GitHub rejected a push to `ibretsam/HowToLiveBetter` with HTTP 403 because the
cloud identity `khanhle3109` lacks write access. No alternate identity,
credential, upstream or unrelated repository was used. The original checkpoint
is remote; the completed cloud commits have not been pushed.

The portable final ZIP includes the tracked repository, current translations,
all public translation checkpoints and a Git bundle of the dedicated branch.
It excludes `.git` runtime configuration, credentials and untracked scratch
files. An authorized writer can restore the bundle and push that branch to the
user's fork; instructions are in `vi/HANDOFF.md`. The ZIP is saved in ChatGPT
Library so the completed work does not depend on this execution workspace.
