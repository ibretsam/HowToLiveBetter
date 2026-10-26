#!/usr/bin/env python3
"""Check full upstream coverage and honest translation labels in the Pages build."""
from collections import Counter
import importlib.util
import json
from pathlib import Path
import re
import sys

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("build_vi_site", ROOT / "tools/build-vi-site.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)
data = json.loads((builder.OUT / "data.json").read_text())
meta = data["meta"]
source = builder.git_text(meta["source_commit"], "README.md")
expected = sorted(set(re.findall(r"\]\((book/[^)#]+\.md)\)", source)))
assert expected == [s["sourcePath"] for s in data["sections"]], "Chapter coverage differs"
ids, counts = set(), Counter()
updates = builder.vi_updates.load_reviewed()
applied_updates = set()
for section in data["sections"]:
    current = builder.parse(builder.git_text(meta["source_commit"], section["sourcePath"]))
    old = builder.parse(builder.git_text(meta["translation_base_commit"], section["sourcePath"]))
    old_by_n = {e["number"]: e for e in old["entries"]}
    assert section["introOriginal"] == current["intro"], "Chapter introduction was dropped"
    intro_id = f"intro-{section['id']}"
    if intro_id in updates:
        task, draft, review = updates[intro_id]
        assert task["source_sha256"] == builder.vi_updates.digest({"title": current["title"], "intro": current["intro"]})
        assert section["title"] == draft["translation"]["title"]
        assert section["introTranslation"] == builder.vi_updates.segments.rewrite_links(
            draft["translation"]["intro"], section["sourcePath"])
        assert section["introStatus"] == "draft" and section["introTranslationRevision"] == meta["source_commit"]
        applied_updates.add(intro_id)
    else:
        assert section["introStatus"] == "outdated"
    assert len(section["entries"]) == len(current["entries"])
    for entry, original in zip(section["entries"], current["entries"]):
        assert entry["id"] not in ids, "Duplicate item ID"
        ids.add(entry["id"])
        assert entry["original"] == original, f"Source content altered: {entry['id']}"
        assert entry["status"] in builder.STATUSES
        counts[entry["status"]] += 1
        if entry["status"] == "pending":
            assert entry["translation"] is None
        else:
            assert builder.complete(entry["translation"])
            if entry["reviewedUpdate"]:
                task, draft, review = updates[entry["id"]]
                assert task["source_sha256"] == builder.vi_updates.digest(original)
                assert entry["translation"] == builder.vi_updates.entry_translation(task, draft)
                assert entry["status"] == "draft"
                assert entry["translationRevision"] == meta["source_commit"]
                applied_updates.add(entry["id"])
            else:
                baseline = old_by_n[entry["number"]]
                assert builder.same_content(baseline, original) == (entry["status"] == "draft"), entry["id"]
                assert entry["translationRevision"] == meta["translation_base_commit"]
            assert entry["translationRevision"] in entry["translationSourceUrl"]
        assert meta["source_commit"] in entry["sourceUrl"], "Source URL not pinned"
assert dict(counts) == meta["counts"]
assert sum(counts.values()) == meta["total"]
assert meta["reviewed_updates"] == sum(ident.startswith("e-") for ident in applied_updates)
expected_docs = list(dict.fromkeys(re.findall(r"\]\((docs/[^)#/]+\.md)\)", source)))
assert expected_docs == [d["sourcePath"] for d in data["docs"]], "Article coverage differs"
for doc in data["docs"]:
    original = builder.git_text(meta["source_commit"], doc["sourcePath"])
    assert original == doc["originalMarkdown"], f"Article content missing: {doc['id']}"
    assert doc["status"] in builder.STATUSES
    assert bool(doc["translationMarkdown"]) == (doc["status"] != "pending")
    if doc["translationMarkdown"]:
        if doc["reviewedUpdate"]:
            ident = "doc-" + doc["id"]
            task, draft, review = updates[ident]
            assert task["source_sha256"] == builder.vi_updates.digest(original)
            assert doc["translationMarkdown"] == builder.vi_updates.segments.rewrite_links(
                draft["translation"]["markdown"], doc["sourcePath"])
            assert doc["status"] == "draft" and doc["translationRevision"] == meta["source_commit"]
            applied_updates.add(ident)
        else:
            old = builder.git_text(meta["translation_base_commit"], doc["sourcePath"])
            assert (old == original) == (doc["status"] == "draft")
            assert doc["translationRevision"] == meta["translation_base_commit"]
        assert doc["translationRevision"] in doc["translationSourceUrl"]
guide = data["guide"]
assert guide["originalMarkdown"] == source
if guide["reviewedUpdate"]:
    task, draft, review = updates["guide"]
    assert task["source_sha256"] == builder.vi_updates.digest(source)
    assert guide["translationMarkdown"] == builder.vi_updates.segments.rewrite_links(
        draft["translation"]["markdown"], "README.md")
    assert guide["status"] == "draft" and guide["translationRevision"] == meta["source_commit"]
    applied_updates.add("guide")
else:
    assert guide["status"] == "outdated"
assert applied_updates == set(updates)
assert meta["reviewed_supplementary"] == sum(not ident.startswith("e-") for ident in applied_updates)
html = (builder.OUT / "index.html").read_text()
assert 'lang="vi"' in html and "__SITE_URL__" not in html
assert "__SOURCE_README_URL__" not in html
assert guide["sourceUrl"] in html
assert (builder.OUT / "README.md").read_bytes() == (ROOT / "README.md").read_bytes()
assert "Chưa hoàn tất bản dịch" in html and "Bản dịch chưa cập nhật" in html
assert (builder.OUT / "vendor/marked.js").exists()
assert (builder.OUT / ".nojekyll").exists()
print(f"PASS: {len(expected)} chapters, {len(ids)} complete source entries, "
      f"{len(expected_docs)} articles; translation status and pinned source links verified.")
print("This verifies coverage and revision tracking, not professional translation accuracy.")
