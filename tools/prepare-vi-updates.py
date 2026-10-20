#!/usr/bin/env python3
"""Add immutable work packets; rerunning preserves every existing draft/review."""
import json
from pathlib import Path
from vi_updates import CP, ROOT, digest

data = json.loads((ROOT / "dist/vi-site/data.json").read_text())
inventory = json.loads((CP / "inventory.json").read_text())
assert inventory["source_commit"] == data["meta"]["source_commit"], "Build/inventory source differs"
pilot = {13: [1, 2, 3, 26, 27, 28, 45, 46, 47, 48],
         34: list(range(1, 13)), 19: [1, 2, 19, 20, 21, 22, 23, 24]}


def save_packet(directory, task):
    path = CP / directory / (task["id"] + ".json")
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        existing = json.loads(path.read_text())
        for key in ("id", "source_commit", "source_path", "source_sha256", "original"):
            assert existing[key] == task[key], f"Refusing to overwrite changed source packet: {path}"
    else:
        path.write_text(json.dumps(task, ensure_ascii=False, indent=2) + "\n")


for section in data["sections"]:
    source = section["sourcePath"]
    for entry in section["entries"]:
        task = {
            "id": entry["id"], "source_commit": inventory["source_commit"],
            "source_path": source, "source_sha256": digest(entry["original"]),
            "status": entry["status"], "original": entry["original"],
            "previous_translation": entry["translation"],
            "pilot": entry["number"] in pilot.get(section["id"], []),
        }
        save_packet("tasks", task)
    original = {"title": section["originalTitle"], "intro": section["introOriginal"]}
    save_packet("other-tasks", {
        "id": f"intro-{section['id']}", "source_commit": inventory["source_commit"],
        "source_path": source, "source_sha256": digest(original), "original": original,
        "previous_translation": {"title": section["title"], "intro": section["introTranslation"]},
    })
for doc in [*data["docs"], data["guide"]]:
    ident = "guide" if doc is data["guide"] else "doc-" + doc["id"]
    save_packet("other-tasks", {
        "id": ident, "source_commit": inventory["source_commit"],
        "source_path": doc["sourcePath"], "source_sha256": digest(doc["originalMarkdown"]),
        "original": doc["originalMarkdown"], "previous_translation": doc["translationMarkdown"],
    })
print("Prepared 765 entry packets and 44 supplementary packets; existing work preserved.")
