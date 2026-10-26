#!/usr/bin/env python3
"""Validate the all-Markdown localization inventory and reviewed file hashes."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def git_bytes(*args):
    return subprocess.check_output(["git", *args], cwd=ROOT)


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main():
    report = json.loads((ROOT / "vi/markdown-localization.json").read_text())
    baseline = report["baseline_commit"]
    expected = {p for p in git_bytes("ls-tree", "-rz", "--name-only", baseline).decode().split("\0")
                if p.endswith(".md")}
    rows = report["files"]
    assert len({r["path"] for r in rows}) == len(rows), "Duplicate inventory paths"
    assert {r["path"] for r in rows} == expected, "Inventory differs from baseline Markdown files"
    config = json.loads((ROOT / "vi/site-config.json").read_text())
    assert report["book_source_commit"] == config["source_commit"], "Book source revision mismatch"
    for row in rows:
        path = row["path"]
        assert row["source_sha256"] == digest(git_bytes("show", f"{baseline}:{path}")), path
        assert row["status"] in {"translated", "existing_vietnamese", "pending"}, path
        assert (ROOT / path).is_file(), f"Missing file: {path}"
        if row["status"] != "pending":
            assert row["translation_sha256"] == digest((ROOT / path).read_bytes()), f"Changed after review: {path}"
            assert row["method"], f"Missing translation provenance: {path}"
    counts = Counter(row["status"] for row in rows)
    assert dict(counts) == report["counts"], "Summary counts do not match file records"
    status = (ROOT / "vi/MARKDOWN-STATUS.md").read_text()
    complete = len(rows) - counts["pending"]
    assert f"**{complete}/{len(rows)} tệp**" in status, "Human-readable total differs from inventory"
    assert f"**Chưa hoàn tất bản dịch: {counts['pending']} tệp**" in status, "Pending total differs from inventory"
    for row in rows:
        if row["status"] == "pending":
            assert f"`{row['path']}` — **chưa hoàn tất bản dịch**" in status, row["path"]
    print(f"Verified Markdown inventory: {complete}/{len(rows)} complete; {counts['pending']} pending.")


if __name__ == "__main__":
    main()
