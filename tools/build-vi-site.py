#!/usr/bin/env python3
"""Build a static Vietnamese reader with complete, versioned Chinese fallbacks.

No network or translation service is used. Existing translations are compared
with their pinned source, never silently treated as translations of new content.
"""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
from urllib.parse import quote
import vi_updates

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "dist/vi-site"
FIELDS = {
    "成本": "Chi phí", "说人话": "Nói dễ hiểu", "收益": "Lợi ích",
    "证据等级": "Mức độ bằng chứng", "来源": "Nguồn", "备注": "Ghi chú",
}
KEYS = dict(zip(FIELDS, ("cost", "plain", "benefit", "grade", "sources", "notes")))
DOCS = {
    "结婚划不划算": ("ket-hon-co-dang-khong", "Kết hôn có đáng không?"),
    "家庭应急装备清单": ("danh-sach-do-dung-khan-cap", "Đồ dùng khẩn cấp trong gia đình"),
    "遇到陌生人出事该不该停": ("co-nen-dung-lai-giup-nguoi-la", "Có nên dừng lại giúp người lạ?"),
    "做平台要办哪些证": ("giay-phep-cho-nen-tang", "Giấy phép khi vận hành nền tảng"),
    "生物钟和夜班": ("dong-ho-sinh-hoc-va-ca-dem", "Đồng hồ sinh học và ca đêm"),
    "被裁了之后先做什么": ("viec-can-lam-khi-bi-sa-thai", "Việc cần làm khi bị sa thải"),
    "孩子出生前后要办的事": ("viec-can-lam-truoc-va-sau-khi-sinh-con", "Trước và sau khi sinh con"),
    "刚确诊慢性病之后": ("sau-chan-doan-benh-man-tinh", "Sau chẩn đoán bệnh mạn tính"),
    "换工作、换城市之前": ("truoc-khi-doi-viec-chuyen-thanh-pho", "Trước khi đổi việc hoặc chuyển thành phố"),
}
STATUSES = {"draft": "Bản nháp tiếng Việt", "outdated": "Bản dịch chưa cập nhật", "pending": "Chưa hoàn tất bản dịch"}


def git_text(commit, path):
    return subprocess.check_output(["git", "show", f"{commit}:{path}"], cwd=ROOT).decode()


def checksum(text):
    return hashlib.sha256(text.encode()).hexdigest()


def parse(text, vietnamese=False):
    heading = re.search(r"^# (?:\d+\.\s*)?(.+)$", text, re.M)
    parts = re.split(r"(?m)^### (\d+)\. (.+)\n", text)
    entries = []
    for i in range(1, len(parts), 3):
        number, title, body = parts[i:i+3]
        fields = {}
        for zh, vi in FIELDS.items():
            label, colon = (vi, ":") if vietnamese else (zh, "：")
            match = re.search(r"^- " + re.escape(label) + re.escape(colon) + r"\s*(.*)$", body, re.M)
            fields[KEYS[zh]] = match[1].strip() if match else ""
        tags = dict(re.findall(r"(\S+)=(\S+)", re.search(r"<!-- 成本标签:(.*?)-->", body)[1])) if "<!-- 成本标签:" in body else {}
        field_labels = list(FIELDS.values()) if vietnamese else list(FIELDS)
        field_line = re.compile(r"^- (?:" + "|".join(map(re.escape, field_labels)) + r")[:：]")
        extra = "\n".join(line for line in body.splitlines()
                          if not field_line.match(line) and not line.startswith("<!--")).strip()
        entries.append({"number": int(number), "title": title.strip(), "fields": fields, "tags": tags, "extra": extra})
    intro = parts[0].split(heading[0], 1)[-1].strip() if heading else ""
    return {"title": heading[1] if heading else "", "intro": intro, "entries": entries}


def same_content(a, b):
    # Ignore metadata and whitespace only. Even a small prose correction marks
    # a translation outdated; being conservative is preferable to hiding edits.
    normalize = lambda s: re.sub(r"\s+", "", s)
    return normalize(a["title"]) == normalize(b["title"]) and normalize(a["extra"]) == normalize(b["extra"]) and all(
        normalize(a["fields"][k]) == normalize(b["fields"][k]) for k in KEYS.values())


def complete(entry):
    return bool(entry and entry["title"] and all(entry["fields"].values())
                and not re.search(r"\[CHƯA DỊCH\]|⟦[PL]\d+⟧", json.dumps(entry, ensure_ascii=False)))


def source_url(config, path, commit=None):
    return f"https://github.com/{config['upstream']}/blob/{commit or config['source_commit']}/{quote(path, safe='/')}"


def build():
    config = json.loads((ROOT / "vi/site-config.json").read_text())
    config["source_commit"] = subprocess.check_output(
        ["git", "rev-parse", config["source_commit"]], cwd=ROOT).decode().strip()
    base = config["translation_base_commit"]
    manifest = json.loads((ROOT / "vi/translation-manifest.json").read_text())
    records = {r["source"]: r for r in manifest["files"]}
    mappings = json.loads((ROOT / "vi/entry-mapping.json").read_text())["pairs"]
    updates = vi_updates.load_reviewed()
    applied_updates = set()
    def update_for(ident, source, original):
        update = updates.get(ident)
        if update:
            task, draft, review = update
            assert task["source_commit"] == config["source_commit"], f"Update source revision: {ident}"
            assert task["source_path"] == source and task["source_sha256"] == vi_updates.digest(original), (
                f"Update source content mismatch: {ident}")
            applied_updates.add(ident)
        return update
    sections, docs, counts = [], [], Counter()
    readme = git_text(config["source_commit"], "README.md")
    chapter_paths = sorted(set(re.findall(r"\]\((book/[^)#]+\.md)\)", readme)))
    assert chapter_paths, "No source chapters discovered"
    for source in chapter_paths:
        current_text = (ROOT / source).read_text()
        assert current_text == git_text(config["source_commit"], source), f"Source revision mismatch: {source}"
        current = parse(current_text)
        sec = int(Path(source).name[:2])
        record = records.get(source)
        target = record.get("target", record.get("translation")) if record else None
        translated_text = (ROOT / target).read_text() if target and (ROOT / target).exists() else ""
        if record and translated_text:
            assert checksum(translated_text) == record["translation_sha256"], f"Translation changed without review: {target}"
        translated = parse(translated_text, True)
        previous = parse(git_text(base, source)) if record else {"entries": []}
        old_by_n = {e["number"]: e for e in previous["entries"]}
        vi_by_n = {e["number"]: e for e in translated["entries"]}
        section = {"id": sec, "title": translated["title"] or current["title"],
                   "originalTitle": current["title"], "introOriginal": current["intro"],
                   "introTranslation": translated["intro"], "sourcePath": source,
                   "introStatus": "outdated", "introTranslationRevision": base,
                   "sourceUrl": source_url(config, source), "entries": []}
        intro_update = update_for(f"intro-{sec}", source, {"title": current["title"], "intro": current["intro"]})
        if intro_update:
            intro = intro_update[1]["translation"]
            section.update(title=intro["title"],
                           introTranslation=vi_updates.segments.rewrite_links(intro["intro"], source),
                           introStatus="draft", introTranslationRevision=config["source_commit"])
        for entry in current["entries"]:
            n = entry["number"]
            ident = f"e-{sec}-{n}"
            vi, old = vi_by_n.get(n), old_by_n.get(n)
            mapping = mappings.get(f"e-{sec}-{n}", {})
            # Numbering is stable in this update, but refuse a mismatched pairing.
            matches = old and (old["title"] == entry["title"] or
                old["fields"]["sources"] == entry["fields"]["sources"] or
                (mapping.get("translation_source_title") == old["title"] and
                 mapping.get("source_title") == entry["title"]))
            status = "pending"
            if complete(vi) and matches:
                status = "draft" if same_content(old, entry) else "outdated"
            if status == "pending":
                vi = None
            translation_commit = base
            update = update_for(ident, source, entry)
            if update:
                task, draft, review = update
                vi = vi_updates.entry_translation(task, draft)
                status = "draft"
                translation_commit = task["source_commit"]
            counts[status] += 1
            section["entries"].append({
                "id": ident, "number": n, "status": status,
                "translation": vi, "original": entry,
                "sourceUrl": source_url(config, source),
                "translationSourceUrl": source_url(config, source, translation_commit),
                "translationRevision": translation_commit,
                "reviewedUpdate": bool(update),
            })
        sections.append(section)
    doc_paths = list(dict.fromkeys(re.findall(r"\]\((docs/[^)#/]+\.md)\)", readme)))
    for source in doc_paths:
        slug, title = DOCS.get(Path(source).stem, (Path(source).stem, Path(source).stem))
        original = (ROOT / source).read_text()
        assert original == git_text(config["source_commit"], source)
        record = records.get(source)
        target = record.get("target", record.get("translation")) if record else None
        translation = (ROOT / target).read_text() if target and (ROOT / target).exists() else None
        if record and translation:
            assert checksum(translation) == record["translation_sha256"], f"Translation changed: {target}"
        status = "pending"
        if translation and "[CHƯA DỊCH]" not in translation:
            status = "draft" if original == git_text(base, source) else "outdated"
        translation_commit = base
        doc_update = update_for("doc-" + slug, source, original)
        if doc_update:
            translation = vi_updates.segments.rewrite_links(doc_update[1]["translation"]["markdown"], source)
            translation_commit = config["source_commit"]
            status = "draft"
            target = target or f"vi/docs/{slug}.md"
        docs.append({"id": slug, "title": title, "status": status, "sourcePath": source,
                     "translationPath": target, "originalMarkdown": original,
                     "translationMarkdown": translation if status != "pending" else None,
                     "sourceUrl": source_url(config, source),
                     "translationSourceUrl": source_url(config, source, translation_commit),
                     "translationRevision": translation_commit, "reviewedUpdate": bool(doc_update)})
    guide_update = update_for("guide", "README.md", readme)
    guide_translation = (ROOT / "vi/README.md").read_text()
    guide_commit = base
    if guide_update:
        guide_translation = vi_updates.segments.rewrite_links(guide_update[1]["translation"]["markdown"], "README.md")
        guide_commit = config["source_commit"]
    assert applied_updates == set(updates), "Reviewed update has no current content"
    reviewed_entries = sum(ident.startswith("e-") for ident in applied_updates)
    data = {"meta": {**config, "total": sum(counts.values()), "counts": dict(counts),
                    "reviewed_updates": reviewed_entries,
                    "reviewed_supplementary": len(applied_updates) - reviewed_entries,
                    "statusLabels": STATUSES}, "sections": sections, "docs": docs,
            "guide": {"title": "Hướng dẫn đọc và thuật ngữ", "status": "draft" if guide_update else "outdated",
                      "translationMarkdown": guide_translation,
                      "originalMarkdown": readme, "sourcePath": "README.md",
                      "translationPath": "vi/README.md",
                      "translationRevision": guide_commit, "reviewedUpdate": bool(guide_update),
                      "sourceUrl": source_url(config, "README.md"),
                      "translationSourceUrl": source_url(config, "README.md", guide_commit)}}
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT / "data.json").write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n")
    html = (ROOT / "vi/index.html").read_text()
    marked = ROOT / "tools/epub/node_modules/marked/lib/marked.umd.js"
    if not marked.exists():
        raise RuntimeError("Run npm --prefix tools/epub ci before building the reader.")
    (OUT / "vendor").mkdir(exist_ok=True)
    shutil.copy2(marked, OUT / "vendor/marked.js")
    shutil.copy2(ROOT / "tools/epub/node_modules/marked/LICENSE", OUT / "vendor/marked-LICENSE")
    site_url = f"https://{config['repository'].split('/')[0]}.github.io/{config['repository'].split('/')[1]}/"
    (OUT / "index.html").write_text(html.replace("__SITE_URL__", site_url))
    (OUT / ".nojekyll").write_text("")
    (OUT / "404.html").write_text(html.replace("__SITE_URL__", site_url))
    (OUT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nSitemap: {site_url}sitemap.xml\n")
    (OUT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{site_url}</loc></url></urlset>\n')
    shutil.copy2(ROOT / "LICENSE", OUT / "LICENSE")
    # Source files, including reader articles and verification notes, remain
    # available as downloads; the UI reads full content from data.json.
    for directory in ("book", "docs", "vi/book", "vi/docs"):
        shutil.copytree(ROOT / directory, OUT / directory, dirs_exist_ok=True)
    for file in ("README.md", "vi/README.md", "vi/TRANSLATION.md", "vi/TRANSLATION-PLAN.md"):
        shutil.copy2(ROOT / file, OUT / file)
    report = {"source_commit": config["source_commit"], "translation_base_commit": base,
              "checkpoint": str(vi_updates.CP.relative_to(ROOT)),
              "inherited_reviews_for_identical_source": sum(
                  draft["source_commit"] != config["source_commit"] for _, draft, _ in updates.values()),
              "chapters": len(sections), "entries": sum(counts.values()),
              "articles": len(docs), "entries_by_status": dict(counts),
              "reviewed_updates": reviewed_entries,
              "reviewed_supplementary": len(applied_updates) - reviewed_entries,
              "chapter_intros_by_status": dict(Counter(s["introStatus"] for s in sections)),
              "guide_status": data["guide"]["status"],
              "articles_by_status": dict(Counter(d["status"] for d in docs))}
    (OUT / "coverage.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return data


if __name__ == "__main__":
    build()
