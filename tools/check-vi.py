#!/usr/bin/env python3
"""Check Vietnamese edition coverage and source fidelity without network calls.

This validates structure, references, citations and written numbers, not the
semantic accuracy of the translation. Source snapshots are read from Git.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "vi/translation-manifest.json"
FIELDS = {"成本": "Chi phí", "说人话": "Nói dễ hiểu", "收益": "Lợi ích",
          "证据等级": "Mức độ bằng chứng", "来源": "Nguồn", "备注": "Ghi chú"}
NUMBER = re.compile(r"\d+(?:\.\d+)?")
LINK = re.compile(r"\]\(([^)]+)\)")
URL = re.compile(r"https?://[^\s<>）]+")
HAN = re.compile(r"[\u3400-\u9fff]")
STATS = re.compile(r"\b(?:HR|RR|OR|CI|SMD|SMR)\b")


def plain(line):
    line = re.sub(r"<!--.*?-->", "", line)
    line = re.sub(r"`[^`]*`|<[^>]*>|https?://\S+|(?<=\]\()[^)]+(?=\))", "", line)
    return line


def main():
    if not MANIFEST.exists():
        sys.exit("Missing vi/translation-manifest.json")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    commit = manifest["source_commit"]
    errors = []
    entries = 0
    for record in manifest["files"]:
        source_path, target_path = record["source"], ROOT / record["translation"]
        source = subprocess.check_output(["git", "show", f"{commit}:{source_path}"], cwd=ROOT).decode("utf-8")
        if hashlib.sha256(source.encode()).hexdigest() != record["source_sha256"]:
            errors.append(f"{source_path}: source snapshot checksum mismatch")
        if not target_path.is_file():
            errors.append(f"Missing {record['translation']}")
            continue
        target = target_path.read_text(encoding="utf-8")
        if "[CHƯA DỊCH]" in target:
            errors.append(f"{record['translation']}: unfinished translation")
        if re.search(r"⟦[PL]\d+⟧", target):
            errors.append(f"{record['translation']}: unresolved translation placeholder")
        if source_path.startswith("book/"):
            original_titles = re.findall(r"^### (\d+)\.", source, re.M)
            translated_titles = re.findall(r"^### (\d+)\.", target, re.M)
            entries += len(translated_titles)
            if original_titles != translated_titles:
                errors.append(f"{record['translation']}: recommendation numbering differs")
            for zh, vi in FIELDS.items():
                if len(re.findall(rf"^- {zh}：", source, re.M)) != len(re.findall(rf"^- {vi}:", target, re.M)):
                    errors.append(f"{record['translation']}: missing or duplicated {vi} fields")
            if re.findall(r"^- 证据等级：(.*)$", source, re.M) != [x.lstrip() for x in re.findall(r"^- Mức độ bằng chứng:(.*)$", target, re.M)]:
                errors.append(f"{record['translation']}: evidence grades differ")
            original_refs = [x.strip() for x in re.findall(r"^- 来源：(.*)$", source, re.M)]
            translated_refs = [x.strip() for x in re.findall(r"^- Nguồn:(.*)$", target, re.M)]
            # Bibliographic text and its external URLs must remain unchanged.
            if original_refs != translated_refs:
                errors.append(f"{record['translation']}: original citations differ")
            original_tags = re.findall(r"<!-- 成本标签:.*?-->", source)
            if original_tags != re.findall(r"<!-- 成本标签:.*?-->", target):
                errors.append(f"{record['translation']}: original cost tags differ")
            # Match each entry's fields independently; dates can change order.
            for zh, vi in FIELDS.items():
                if zh in ("来源", "证据等级"):
                    continue
                original_rows = re.findall(rf"^- {zh}：(.*)$", source, re.M)
                translated_rows = re.findall(rf"^- {vi}:(.*)$", target, re.M)
                for n, (a, b) in enumerate(zip(original_rows, translated_rows), 1):
                    missing = Counter(NUMBER.findall(plain(a))) - Counter(NUMBER.findall(plain(b)))
                    if missing:
                        errors.append(f"{record['translation']} item {n} {vi}: missing written numbers {dict(missing)}")
                    missing_stats = Counter(STATS.findall(plain(a))) - Counter(STATS.findall(plain(b)))
                    if missing_stats:
                        errors.append(f"{record['translation']} item {n} {vi}: missing statistical symbols {dict(missing_stats)}")
                    if HAN.search(plain(b)):
                        errors.append(f"{record['translation']} item {n} {vi}: untranslated Chinese prose")
        else:
            missing = Counter(NUMBER.findall(plain(source))) - Counter(NUMBER.findall(plain(target)))
            if missing:
                errors.append(f"{record['translation']}: missing written numbers {dict(missing)}")
        for url in LINK.findall(target):
            if re.match(r"(?:https?://|mailto:|#)", url):
                continue
            path = unquote(url.split("#", 1)[0])
            if not (target_path.parent / path).exists():
                errors.append(f"{record['translation']}: broken local link {url}")
    expected = sum(r["entries"] or 0 for r in manifest["files"])
    if entries != expected:
        errors.append(f"Expected {expected} recommendations, found {entries}")
    if errors:
        print("\n".join(errors))
        print(f"FAILED: {len(errors)} issues")
        sys.exit(1)
    print(f"PASS: {len(manifest['files'])} translated files, {entries} recommendations; source snapshots, numbering, fields, evidence grades, citations, metadata, numbers and local links checked.")
    print("This is a structural check, not a full language or subject-matter review.")


if __name__ == "__main__":
    main()
