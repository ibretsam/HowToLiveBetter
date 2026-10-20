#!/usr/bin/env python3
"""Validate current-source translation packets, drafts and independent reviews."""
import json
import subprocess
import sys
from collections import Counter
import importlib.util
from pathlib import Path

sys.dont_write_bytecode = True
from vi_updates import CP, ROOT, digest, validate_draft, load_reviewed

spec = importlib.util.spec_from_file_location("builder", ROOT / "tools/build-vi-site.py")
builder = importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)


def main():
    inventory = json.loads((CP / "inventory.json").read_text())
    source_commit = inventory["source_commit"]
    config = json.loads((ROOT / "vi/site-config.json").read_text())
    assert source_commit == config["source_commit"], "Inventory must match publication source"
    tasks, source_entries = {}, {}
    for source in {item["source_path"] for item in inventory["entries"]}:
        text = subprocess.check_output(["git", "show", f"{source_commit}:{source}"], cwd=ROOT).decode()
        section = int(Path(source).name[:2])
        for entry in builder.parse(text)["entries"]:
            source_entries[f"e-{section}-{entry['number']}"] = (source, entry)
    for item in inventory["entries"]:
        ident = item["id"]
        assert ident not in tasks, f"Duplicate inventory ID: {ident}"
        task = json.loads((CP / "tasks" / f"{ident}.json").read_text())
        source, original = source_entries[ident]
        assert task["id"] == ident and task["source_commit"] == source_commit
        assert task["source_path"] == source and task["original"] == original, f"{ident}: source changed"
        assert digest(original) == item["source_sha256"] == task["source_sha256"]
        tasks[ident] = task
    assert set(tasks) == set(source_entries), "Incomplete inventory"
    assert {p.stem for p in (CP / "tasks").glob("e-*.json")} == set(tasks), "Unexpected packet"
    for item in inventory["other_content"]:
        ident = item["id"]
        task = json.loads((CP / "other-tasks" / f"{ident}.json").read_text())
        original = builder.git_text(source_commit, item["source_path"])
        if item["kind"] == "chapter_heading_and_intro":
            parsed = builder.parse(original)
            original = {"title": parsed["title"], "intro": parsed["intro"]}
        assert task["id"] == ident and task["source_commit"] == source_commit
        assert task["source_path"] == item["source_path"] and task["original"] == original
        assert task["source_sha256"] == digest(original), f"{ident}: supplementary source mismatch"
        tasks[ident] = task
    assert {p.stem for p in (CP / "other-tasks").glob("*.json")} == {
        item["id"] for item in inventory["other_content"]}, "Supplementary inventory mismatch"
    drafted = []
    for path in sorted((CP / "drafts").glob("*.json")):
        draft = json.loads(path.read_text())
        validate_draft(tasks[path.stem], draft)
        drafted.append(path.stem)
    reviewed = load_reviewed()
    print(json.dumps({
        "status": "passed", "source_commit": source_commit,
        "inventoried_entries": len(source_entries), "other_units": len(inventory["other_content"]),
        "pilot_entries": sum(t.get("pilot", False) for t in tasks.values()),
        "validated_drafts": len(drafted), "independently_reviewed": len(reviewed),
        "reviewed_previous_status": dict(Counter(tasks[k].get("status", "supplementary") for k in reviewed)),
        "unreviewed_drafts": sorted(set(drafted) - set(reviewed)),
    }, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
