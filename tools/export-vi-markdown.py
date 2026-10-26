#!/usr/bin/env python3
"""Export reviewed reader content into the fork's main Markdown files.

The immutable Chinese source lives at site-config.json's Git revision. Archived
vi/ drafts and their review hashes are never rewritten by this exporter.
"""
import argparse
import importlib.util
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LABELS = {"cost": "Chi phí", "plain": "Nói dễ hiểu", "benefit": "Lợi ích",
          "grade": "Mức độ bằng chứng", "sources": "Nguồn", "notes": "Ghi chú"}


def exports(data):
    meta = data["meta"]
    paths = {f"vi/book/{s['id']:02d}.md": s["sourcePath"] for s in data["sections"]}
    paths.update({d["translationPath"]: d["sourcePath"] for d in data["docs"]})
    paths["vi/README.md"] = "README.md"
    site = f"https://{meta['repository'].split('/')[0]}.github.io/{meta['repository'].split('/')[1]}/"

    def links(text, old_path, new_path):
        def url(value):
            if urlsplit(value).scheme or value.startswith(("#", "//")):
                return value
            path, sep, fragment = value.partition("#")
            resolved = os.path.normpath(str(Path(old_path).parent / unquote(path)))
            target = paths.get(resolved, resolved)
            if target == "README.md" and fragment:
                return site + "#guide"
            # Old Chinese heading anchors cannot address Vietnamese headings.
            # Route chapter references to the reader, whose IDs are stable.
            chapter = re.match(r"book/(\d+)", target)
            if chapter and fragment:
                return site + "#sec-" + str(int(chapter[1]))
            result = Path(os.path.relpath(target, Path(new_path).parent)).as_posix()
            if path.endswith("/"):
                result += "/"
            return result + (sep + fragment if sep else "")
        text = re.sub(r"(\]\()([^)]+)(\))", lambda m: m[1] + url(m[2]) + m[3], text)
        return re.sub(r'(\b(?:src|href)=")([^"#]+)(")', lambda m: m[1] + url(m[2]) + m[3], text)

    def notice(source):
        original = f"https://github.com/{meta['upstream']}/blob/{meta['source_commit']}/{quote(source, safe='/')}"
        return (f"> Bản dịch tiếng Việt chưa chính thức, theo nguồn ngày {meta['synced_at']}. "
                f"[Đối chiếu bản gốc tiếng Trung]({original}).\n"
                "> Nội dung về pháp luật, trợ cấp và tiền tệ giữ bối cảnh Trung Quốc của nguyên tác.\n\n")

    result = {}
    for section in data["sections"]:
        assert section["introStatus"] == "draft", f"Unreviewed intro {section['id']}"
        source = section["sourcePath"]
        old_path = f"vi/book/{section['id']:02d}.md"
        blocks = ["[← Về mục lục](../README.md)\n\n" + notice(source)
                  + f"# {section['id']}. {section['title']}\n\n"
                  + links(section["introTranslation"], old_path, source)]
        for entry in section["entries"]:
            assert entry["status"] == "draft" and entry["translation"], f"Unreviewed entry {entry['id']}"
            vi = entry["translation"]
            tags = " ".join(f"{k}={v}" for k, v in entry["original"]["tags"].items())
            block = f"### {entry['number']}. {vi['title']}\n<!-- 成本标签: {tags} -->\n"
            block += "\n".join(f"- {label}: {links(vi['fields'][key], old_path, source)}"
                               for key, label in LABELS.items())
            if vi.get("extra"):
                block += "\n\n" + links(vi["extra"], old_path, source)
            blocks.append(block)
        result[source] = "\n\n".join(blocks).rstrip() + "\n"
    for doc in data["docs"]:
        assert doc["status"] == "draft" and doc["translationMarkdown"], f"Unreviewed document {doc['id']}"
        source = doc["sourcePath"]
        # Supplementary links were rebased by vi_segments against vi/<source>,
        # including the new article absent from the archived filename map.
        old_path = "vi/" + source if doc["id"] == "truoc-khi-doi-viec-chuyen-thanh-pho" else doc["translationPath"]
        result[source] = notice(source) + links(doc["translationMarkdown"], old_path, source).rstrip() + "\n"
    result["docs/引用对照.md"] = reference_report(data)
    return result


def reference_report(data):
    """Translate the generated reference index without fabricating source quotes."""
    meta = data["meta"]
    original = subprocess.check_output(
        ["git", "show", f"{meta['source_commit']}:docs/引用对照.md"], cwd=ROOT).decode()
    titles = {e["original"]["title"]: e["translation"]["title"]
              for s in data["sections"] for e in s["entries"]}
    headings = {Path(s["sourcePath"]).stem: f"{s['id']:02d} — {s['title']}" for s in data["sections"]}
    units = {"节首": "Lời dẫn chương", "开头": "Mở đầu"}
    for doc in data["docs"]:
        headings[doc["sourcePath"].removesuffix(".md")] = doc["title"]
        zh = re.findall(r"^#{1,6} (.+)$", doc["originalMarkdown"], re.M)
        vi = re.findall(r"^#{1,6} (.+)$", doc["translationMarkdown"], re.M)
        assert len(zh) == len(vi), f"Heading mismatch: {doc['id']}"
        units.update(zip(zh, vi))
    count = 0
    rows = []
    for line in original.splitlines():
        if line.startswith("## "):
            rows.append("\n## " + headings[line[3:]] + "\n")
        elif line.startswith("| 出处"):
            rows.append("| Vị trí dẫn | Tham chiếu | Tiêu đề mục đích bằng tiếng Việt | Ngữ cảnh nguồn (trích nguyên văn để đối chiếu) |")
        elif line.startswith("| ---"):
            rows.append(line)
        elif line.startswith("| "):
            source, ref, title, context = line[2:-2].split(" | ")
            source = units.get(source, source)
            source = re.sub(r"第 (\d+) 条", r"Mục \1", source)
            assert not re.search(r"[\u4e00-\u9fff]", source), source
            ref = re.sub(r"第 (\d+) 节", r"chương \1,", ref)
            ref = re.sub(r"第 (\d+) 条", r"mục \1", ref).replace("本节", "Trong chương này, ")
            assert not re.search(r"[\u4e00-\u9fff]", ref), ref
            rows.append(f"| {source} | {ref} | {titles[title]} | {context} |")
            count += 1
    header = """# Bảng đối chiếu tham chiếu chéo

Bảng này được xuất bằng `python3 tools/export-vi-markdown.py` từ bảng đối chiếu nguồn đã ghim và bản dịch đã rà soát. Không sửa tay các dòng dữ liệu.

Trong nguyên tác, cụm “mục X” chỉ ghi vị trí, không ghi nội dung. Chèn hoặc xóa mục có thể làm hàng loạt tham chiếu trỏ nhầm, dù số mục vẫn nằm trong phạm vi hợp lệ. Vì vậy, bảng ghi **tiêu đề thực sự được trỏ tới** và được lưu trong Git. Khi số mục không đổi nhưng tiêu đề đích đổi trong `git diff`, cần kiểm tra xem tham chiếu có bị lệch do đánh lại số hay không.

Phạm vi quét của nguồn gồm nội dung mục và lời dẫn từng chương trong `book/`, cùng các bài dài ở `docs/`. Bài dài không có “chương này”; số mục đứng riêng được xem như số điều luật và bỏ qua. Tham chiếu trong bài dài phải ghi đủ chương X, mục Y. Cột vị trí ghi số mục, lời dẫn chương hoặc tiêu đề phụ gần nhất trong bài dài.

Lớp kiểm tra thứ hai là **từ khóa làm mốc**: ngữ cảnh phải có từ khớp tiêu đề đích, chẳng hạn “hỗ trợ y tế, xem mục 11” hoặc “xem mục 16 (giấy vay nợ và bảo lãnh)”. Trên bản tiếng Trung, `node tools/check-refs.mjs --check` báo lỗi với số mục đứng trơ trọi không có từ làm mốc. Nếu bị lệch, chỉ nhìn số mục và tiêu đề trong diff chưa chắc phát hiện được. Tham chiếu một khoảng, như chương 8, mục 11 đến 14, là ngoại lệ vì nói tới cả nhóm mục; trường hợp đó dựa vào diff.

Quy tắc của bộ kiểm tra tiếng Trung xét cả độ dài và khoảng cách: trong cùng câu phải có ba chữ Hán liên tiếp khớp tiêu đề, hoặc trong cùng vế ngăn bằng dấu phẩy phải có hai chữ khớp. Hai chữ thông dụng tình cờ trùng ở ngoài vế không đủ. Quy tắc được siết ngày 2026-09-20 sau khi chèn mục ở chương 31: tham chiếu khoản vay đến mục 15 bị lệch sang mục làm việc từ xa cho công ty nước ngoài và tự khai thuế, nhưng hai chữ thông dụng ở vế trước khiến bộ kiểm tra cũ vẫn báo đạt.

Các tiêu đề đích và vị trí trong bảng dưới được chuyển sang tiếng Việt. **Cột cuối giữ nguyên trích đoạn tiếng Trung** vì đây là bằng chứng về chính chuỗi văn bản mà bộ kiểm tra nguồn đã nhận diện, không phải phần thuyết minh chưa dịch. Muốn đọc nội dung tiếng Việt đầy đủ, mở chương hoặc bài tương ứng. Các nhãn máy, tên tệp và trích dẫn gốc được giữ để đối chiếu.

"""
    assert count == int(re.search(r"共 (\d+) 处引用", original)[1])
    return header + f"Tổng cộng **{count} tham chiếu** tại nguồn `{meta['source_commit'][:7]}`.\n" + "\n".join(rows) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    spec = importlib.util.spec_from_file_location("build_vi_site", ROOT / "tools/build-vi-site.py")
    builder = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(builder)
    builder.build()
    data = json.loads((builder.OUT / "data.json").read_text())
    expected = exports(data)
    for name, content in expected.items():
        path = ROOT / name
        if args.check:
            assert path.read_text() == content, f"Markdown differs from reviewed content: {name}"
        else:
            path.write_text(content)
    print(f"{'Verified' if args.check else 'Exported'} {len(expected)} Vietnamese Markdown files (34 chapters, 9 articles, reference index).")


if __name__ == "__main__":
    main()
