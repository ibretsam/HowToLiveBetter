"""Versioned, independently reviewed updates layered over the archived VI draft.

Source packets are immutable for this translation cycle. A review is bound to
the complete draft hash, so editing a reviewed draft invalidates its approval.
"""
from collections import Counter
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CP = ROOT / "translation-checkpoint/vi-current"
FIELDS = ("title", "cost", "plain", "benefit", "notes", "extra")
HAN = re.compile(r"[\u3400-\u9fff]")
PLACEHOLDER = re.compile(r"\[CHƯA DỊCH\]|⟦[PL]\d+⟧")
spec = importlib.util.spec_from_file_location("vi_segments", ROOT / "tools/vi_segments.py")
segments = importlib.util.module_from_spec(spec)
spec.loader.exec_module(segments)


def digest(value):
    return hashlib.sha256(json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()).hexdigest()


def numbers(text):
    return Counter(re.findall(r"\d+(?:\.\d+)?", text))


def urls(text):
    protected = []
    pattern = r'\]\(([^)]+)\)|`([^`]+)`|<(https?://[^>]+)>|(https?://[^\s<>"）)]+)'
    for match in re.finditer(pattern, text):
        link, code, autolink, bare = match.groups()
        protected.append(("code", code) if code is not None else (
            "url", link or autolink or bare.rstrip(".,;:，。；")))
    return Counter(protected)


def prose(text):
    text = re.sub(r"\]\([^)]+\)", "]", text)
    text = re.sub(r"https?://[^\s<>]+|`[^`]+`|<!--.*?-->", "", text)
    return text


def source_value(original, field):
    if isinstance(original, str):
        assert field == "markdown"
        return original
    if "fields" not in original:
        return original[field]
    return original[field] if field in ("title", "extra") else original["fields"][field]


def validate_draft(task, draft):
    for key in ("id", "source_commit", "source_sha256"):
        assert draft.get(key) == task[key], f"{task['id']}: {key} mismatch"
    assert task["source_sha256"] == digest(task["original"]), f"{task['id']}: corrupt source packet"
    assert isinstance(draft.get("translator"), str) and draft["translator"].strip(), "Translator missing"
    translated = draft.get("translation")
    original_content = task["original"]
    fields = (("markdown",) if isinstance(original_content, str) else
              FIELDS if "fields" in original_content else ("title", "intro"))
    assert isinstance(translated, dict) and set(translated) == set(fields), f"{task['id']}: fields"
    retained = draft.get("retained_terms", {})
    assert isinstance(retained, dict) and set(retained) <= set(fields), "Invalid retained-term fields"
    for field in fields:
        value = translated[field]
        original = source_value(task["original"], field)
        assert isinstance(value, str), f"{task['id']} {field}: not text"
        assert field in ("extra", "intro", "markdown") or "\n" not in value, f"{task['id']} {field}: multiline field"
        assert bool(value.strip()) == bool(original.strip()), f"{task['id']} {field}: missing/extra content"
        assert not PLACEHOLDER.search(value), f"{task['id']} {field}: placeholder"
        remaining = prose(value)
        terms = retained.get(field, [])
        assert isinstance(terms, list), "Retained terms must be a list"
        for term in terms:
            assert isinstance(term, str) and 0 < len(term) <= 80 and HAN.search(term), "Invalid retained term"
            assert term in original and term in value, f"{task['id']} {field}: unsupported retained term {term}"
        for term in sorted(terms, key=len, reverse=True):
            remaining = remaining.replace(term, "")
        assert not HAN.search(remaining), f"{task['id']} {field}: untranslated prose"
        assert numbers(value) == numbers(original), (
            f"{task['id']} {field}: numbers missing={numbers(original)-numbers(value)} "
            f"extra={numbers(value)-numbers(original)}")
        assert urls(value) == urls(original), f"{task['id']} {field}: link/code mismatch"
        for term in ("HR", "RR", "OR", "CI", "RCT"):
            pattern = r"(?<![A-Za-z])"+term+r"(?![A-Za-z])"
            assert len(re.findall(pattern, value)) == len(re.findall(pattern, original)), (
                f"{task['id']} {field}: statistical term {term}")
        if field in ("intro", "markdown"):
            headings = lambda s: re.findall(r"^(#{1,6})\s+", s, re.M)
            tables = lambda s: [line.count("|") for line in s.splitlines() if line.startswith("|")]
            assert headings(value) == headings(original), f"{task['id']}: heading structure"
            assert tables(value) == tables(original), f"{task['id']}: table structure"


def validate_review(draft, review):
    assert review.get("id") == draft["id"], "Review ID mismatch"
    assert review.get("source_sha256") == draft["source_sha256"], "Review source mismatch"
    assert review.get("draft_sha256") == digest(draft), f"{draft['id']}: review invalidated by draft edit"
    assert review.get("reviewer") and review["reviewer"] != draft["translator"], "Independent reviewer required"
    assert review.get("status") == "passed", f"{draft['id']}: review not passed"
    assert review.get("checks") == {
        "meaning": True, "numbers_and_units": True, "conditions_and_negation": True,
        "references": True, "readability": True,
    }, f"{draft['id']}: incomplete review"
    assert isinstance(review.get("notes"), str), "Review notes missing"


def load_reviewed():
    results = {}
    if not (CP / "reviews").exists():
        return results
    for path in sorted((CP / "reviews").glob("*.json")):
        review = json.loads(path.read_text())
        draft = json.loads((CP / "drafts" / path.name).read_text())
        directory = "tasks" if path.stem.startswith("e-") else "other-tasks"
        task = json.loads((CP / directory / path.name).read_text())
        assert path.stem == task["id"], f"Wrong filename: {path}"
        validate_draft(task, draft)
        validate_review(draft, review)
        results[task["id"]] = (task, draft, review)
    return results


def entry_translation(task, draft):
    """Copy citations, evidence and metadata; only authored prose is replaced."""
    entry = copy.deepcopy(task["original"])
    for field, value in draft["translation"].items():
        value = segments.rewrite_links(value, task["source_path"])
        if field in ("title", "extra"):
            entry[field] = value
        else:
            entry["fields"][field] = value
    entry["fields"]["sources"] = segments.rewrite_links(entry["fields"]["sources"], task["source_path"])
    entry["fields"]["grade"] = entry["fields"]["grade"].replace("（争议）", " (có tranh luận)").replace(
        "（指南强推荐，但底层证据等级低）",
        " (hướng dẫn khuyến nghị mạnh, nhưng mức độ bằng chứng nền tảng thấp)")
    return entry
