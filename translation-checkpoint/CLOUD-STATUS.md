# Cloud restoration and QA — 2026-10-01

Restored branch `codex/vietnamese-cloud-checkpoint` at checkpoint commit
`6d88a2570e9ef99ad3c301eb8d020a655e3a54f0` in `/workspace/HowToLiveBetter`.
All preserved cache hashes match the snapshot. The 43 source documents match
the pinned source commit, and task inputs match those source documents.
No source prose or cached translation was overwritten. No local Mac process
was stopped, and no credentials or personal files were copied.

## Verified progress

- 137 tasks, 4,103 items; 26 cached tasks containing 993 output strings.
- 111 tasks missing; 3,110 items have no Workers AI result.
- Two pre-existing Vietnamese files are present, but only `vi/book/18.md`
  is a translated source document; `vi/TRANSLATION.md` is explanatory material.
- Added `vi/translation-manifest.json` with all 43 source-to-target mappings,
  source SHA-256 values, per-file missing tasks, and explicit incomplete status.
- Added `tools/check-vi.py`; run `python3 tools/check-vi.py --write-report`.
  Exit 1 deliberately reports an incomplete/invalid checkpoint.

## QA findings

`cloud-qa.json` contains reproducible item indices and source IDs:
31 protected-token mismatches, 336 numeric-review flags, and 17 remaining-Han
flags. Numeric differences require review: punctuation/localization can also
trigger them. Counts can overlap and are not counts of proven translation errors.

Two inspected problems are definite: task 0 item 3 is a source paragraph about
649 recommendations but its cached result is a chapter-3 link; task 16 item 1
ends mid-sentence and omits the latter portion and its protected link. Equal
array lengths therefore do not guarantee matching item order or complete text.
Existing results have no returned item IDs; future inference should return IDs
and be validated by ID, content, numbers, and placeholders before assembly.

## Remaining blocker

This environment exposes no Workers AI inference tool and no `wrangler`
executable. The checkpoint explicitly contains neither the previous Workers AI
runner nor its runtime credentials. Available tool discovery did not expose a
Workers AI connector. Thus the previous translation pipeline cannot currently
be resumed here. No paid service, new credential, or replacement translation
service has been used; the old Google Translate runner was not restarted.

The restored files and QA do not depend on the Mac. However, **ongoing automated
translation has not been established**, and this report is not a promise that a
background process will keep translating after the turn ends. To resume that
pipeline, make its already-authorized inference capability available in this
cloud session (not by committing secrets), or establish an approved replacement.
Then reuse valid results, repair invalid results, translate the 111 missing
tasks, assemble all files, fix internal anchors, and perform full semantic QA.

## Remote persistence blocker

Pushing this checkpoint branch to `ibretsam/HowToLiveBetter` returned HTTP 403:
GitHub denied access to the cloud session's authenticated identity
`khanhle3109`. No upstream or unrelated repository was used. The QA changes are
committed locally; a portable patch is also exported to
`/workspace/shared/howtolivebetter-cloud-qa.patch`. The original checkpoint
remains remotely preserved, but the new QA commit needs an authorized writer
to push it to the dedicated fork branch.
