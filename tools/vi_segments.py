#!/usr/bin/env python3
"""Shared segmentation helpers for the Vietnamese translation.

Splits source documents into translatable segments, protects citations, URLs,
inline code and Markdown structure, and rewrites links for the vi/ tree. Used by
assemble-vi.py and check-vi.py; it never calls a translation service.
"""

import hashlib
import os
from pathlib import Path
import re
import urllib.parse

ROOT = Path(__file__).resolve().parents[1]
HAN = re.compile(r"[\u3400-\u9fff]")
FIELDS = {"成本": "Chi phí", "说人话": "Nói dễ hiểu", "收益": "Lợi ích",
          "证据等级": "Mức độ bằng chứng", "来源": "Nguồn", "备注": "Ghi chú"}
DOC_SLUGS = {
    "做平台要办哪些证": "giay-phep-cho-nen-tang",
    "刚确诊慢性病之后": "sau-chan-doan-benh-man-tinh",
    "孩子出生前后要办的事": "viec-can-lam-truoc-va-sau-khi-sinh-con",
    "家庭应急装备清单": "danh-sach-do-dung-khan-cap",
    "生物钟和夜班": "dong-ho-sinh-hoc-va-ca-dem",
    "结婚划不划算": "ket-hon-co-dang-khong",
    "被裁了之后先做什么": "viec-can-lam-khi-bi-sa-thai",
    "遇到陌生人出事该不该停": "co-nen-dung-lai-giup-nguoi-la",
}
FILES = {"README.md": "vi/README.md"}
FILES.update({p.relative_to(ROOT).as_posix(): f"vi/book/{p.name[:2]}.md"
              for p in sorted((ROOT / "book").glob("*.md"))})
FILES.update({f"docs/{name}.md": f"vi/docs/{slug}.md" for name, slug in DOC_SLUGS.items()})
PROTECT = re.compile(
    r"`[^`]+`|<https?://[^>]+>|https?://[^\s<>）]+|"
    r"(?<=\]\()[^)]+(?=\))|<[^>]+>"
)


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def rewrite_url(url, source):
    if re.match(r"(?:https?://|mailto:|#)", url):
        return url
    path, sep, fragment = url.partition("#")
    origin = (ROOT / source).parent
    resolved = Path(os.path.normpath(origin / urllib.parse.unquote(path)))
    try:
        rel = resolved.relative_to(ROOT).as_posix()
    except ValueError:
        return url
    destination = ROOT / FILES.get(rel, rel)
    new = Path(os.path.relpath(destination, (ROOT / FILES[source]).parent)).as_posix()
    if path.endswith("/"):
        new += "/"
    return new + (sep + fragment if sep else "")


def rewrite_links(text, source):
    text = re.sub(r"(\]\()([^)]+)(\))",
                  lambda m: m[1] + rewrite_url(m[2], source) + m[3], text)
    return re.sub(r'(\b(?:src|href)=")([^"#]+)(")',
                  lambda m: m[1] + rewrite_url(m[2], source) + m[3], text)


def protect(text):
    tokens = []
    def replace(match):
        token = f"⟦P{len(tokens):04d}⟧"
        tokens.append(match[0])
        return token
    return PROTECT.sub(replace, text), tokens


def unprotect(text, tokens):
    for n, value in enumerate(tokens):
        token = f"⟦P{n:04d}⟧"
        if text.count(token) != 1:
            raise ValueError(f"Protected token missing or duplicated: {token}")
        text = text.replace(token, value)
    if re.search(r"⟦[PL]\d+⟧", text):
        raise ValueError("Unresolved placeholder")
    # The service sometimes inserts spaces between Markdown delimiters.
    text = re.sub(r"\]\s+\(", "](", text)
    text = re.sub(r"\[\s+([^\]]+?)\s+\]", r"[\1]", text)
    return text.strip()


def prepare(source):
    original = (ROOT / source).read_text(encoding="utf-8").replace("\r\n", "\n")
    lines = []
    queries = []
    code = False
    bibliography = False
    for raw in original.splitlines():
        line = rewrite_links(raw, source)
        if line.startswith("```"):
            code = not code
            lines.append([(False, line)])
            continue
        if re.match(r"^##? (?:来源|参考文献|原始来源|原始出处)\s*$", line):
            bibliography = True
        elif re.match(r"^#{1,2} ", line):
            bibliography = False
        field = re.match(r"^(- )?(成本|说人话|收益|证据等级|来源|备注)：(.*)$", line)
        if field:
            prefix = (field[1] or "") + FIELDS[field[2]] + ": "
            body = field[3]
            if field[2] in ("来源", "证据等级"):
                lines.append([(False, prefix + body)])
                continue
        else:
            match = re.match(r"^(#{1,6} (?:\d+\. )?|[-*] |\d+\. )(.*)$", line)
            prefix, body = (match[1], match[2]) if match else ("", line)
        if code or bibliography and not line.startswith("#") or line.startswith("<!--") or not HAN.search(body):
            lines.append([(False, line)])
            continue
        # Each table cell is independent, so translated text cannot change columns.
        cells = re.split(r"(\|)", body) if body.startswith("|") else [body]
        pieces = [(False, prefix)]
        for cell in cells:
            if HAN.search(cell):
                key = digest(cell)
                queries.append((key, cell))
                pieces.append((True, key))
            else:
                pieces.append((False, cell))
        lines.append(pieces)
    return original, lines, queries


def notice(source):
    original = Path(os.path.relpath(ROOT / source, (ROOT / FILES[source]).parent)).as_posix()
    notes = Path(os.path.relpath(ROOT / "vi/TRANSLATION.md", (ROOT / FILES[source]).parent)).as_posix()
    return (f"> **Bản dịch tiếng Việt chưa chính thức — bản nháp dịch máy.** "
            f"[Thông tin bản dịch]({notes}) · [Đối chiếu bản gốc tiếng Trung]({original}).\n"
            "> Luật, trợ cấp, số điện thoại và khoản tiền trong sách thuộc bối cảnh Trung Quốc đại lục; "
            "tiền tính bằng nhân dân tệ, trừ khi ghi rõ đơn vị khác.\n\n")
