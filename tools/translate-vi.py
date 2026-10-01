#!/usr/bin/env python3
"""Build an explicitly labelled Vietnamese machine-translation draft.

Only public reader-facing text is sent to Google Translate. Original citations,
URLs, inline code, numbers, statistical abbreviations and Markdown structure are
protected. Cache lives in .git; rerunning never overwrites an existing translation
unless --overwrite is supplied. No API key or third-party package is required.
"""

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
import threading
import time
import urllib.parse
import urllib.request

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
LOCK = threading.Lock()
CACHE = {}
CACHE_PATH = None


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


def request_translation(query):
    params = urllib.parse.urlencode({"client": "gtx", "sl": "zh-CN", "tl": "vi", "dt": "t", "q": query})
    url = "https://translate.googleapis.com/translate_a/single?" + params
    request = urllib.request.Request(url, headers={"User-Agent": "HowToLiveBetter-Vietnamese-Draft/1.0"})
    last = None
    for attempt in range(5):
        try:
            with urllib.request.urlopen(request, timeout=45) as response:
                payload = json.load(response)
            return "".join(part[0] for part in payload[0] if part[0])
        except Exception as exc:
            last = exc
            time.sleep(min(2 ** attempt, 16))
    raise RuntimeError(f"Translation request failed: {last}")


def translate_batch(items):
    # Batches are split recursively if the service alters a line marker.
    queries = []
    originals = []
    for n, (_, value) in enumerate(items):
        masked, tokens = protect(value)
        queries.append(f"⟦L{n:04d}⟧ {masked}")
        originals.append(tokens)
    try:
        output = request_translation("\n".join(queries))
        parts = list(re.finditer(r"⟦L(\d{4})⟧", output))
        if [int(m[1]) for m in parts] != list(range(len(items))):
            raise ValueError("Line markers changed")
        values = []
        for n, match in enumerate(parts):
            end = parts[n + 1].start() if n + 1 < len(parts) else len(output)
            value = unprotect(output[match.end():end], originals[n])
            if not value:
                raise ValueError("Empty translation")
            values.append(value)
    except ValueError:
        if len(items) == 1:
            # Single-line calls don't require a line marker.
            masked, tokens = protect(items[0][1])
            values = [unprotect(request_translation(masked), tokens)]
        else:
            half = len(items) // 2
            return translate_batch(items[:half]) + translate_batch(items[half:])
    with LOCK:
        CACHE.update({key: value for (key, _), value in zip(items, values)})
        temporary = CACHE_PATH.with_suffix(".tmp")
        temporary.write_text(json.dumps(CACHE, ensure_ascii=False), encoding="utf-8")
        temporary.replace(CACHE_PATH)
    return values


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


def main():
    global CACHE, CACHE_PATH
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--overwrite", action="store_true", help="Explicitly replace existing translated files")
    parser.add_argument("--only", help="Translate one source path, for example book/18-养孩子划不划算.md")
    parser.add_argument("--workers", type=int, default=3)
    args = parser.parse_args()
    git_dir = subprocess.check_output(["git", "rev-parse", "--absolute-git-dir"], cwd=ROOT, text=True).strip()
    CACHE_PATH = Path(git_dir) / "translation-vi-cache.json"
    if CACHE_PATH.exists():
        CACHE = json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    selected = [args.only] if args.only else list(FILES)
    prepared = {}
    queries = {}
    for source in selected:
        if source not in FILES:
            raise SystemExit(f"Unsupported source file: {source}")
        if (ROOT / FILES[source]).exists() and not args.overwrite:
            print(f"Preserving existing {FILES[source]}", flush=True)
            continue
        original, lines, needed = prepare(source)
        prepared[source] = (original, lines)
        queries.update({k: v for k, v in needed if k not in CACHE})
    batches = []
    batch = []
    size = 0
    for item in queries.items():
        masked, _ = protect(item[1])
        encoded_size = len(urllib.parse.quote_plus(masked)) + 40
        if batch and size + encoded_size > 7800:
            batches.append(batch)
            batch, size = [], 0
        batch.append(item)
        size += encoded_size
    if batch:
        batches.append(batch)
    print(f"{len(prepared)} files, {len(queries)} text segments, {len(batches)} batches", flush=True)
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = [pool.submit(translate_batch, batch) for batch in batches]
        for n, future in enumerate(as_completed(futures), 1):
            future.result()
            if n % 10 == 0 or n == len(futures):
                print(f"Translated {n}/{len(futures)} batches", flush=True)
    for source, (original, lines) in prepared.items():
        translated = ["".join(CACHE[value] if is_query else value for is_query, value in pieces) for pieces in lines]
        target = ROOT / FILES[source]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(notice(source) + "\n".join(translated) + "\n", encoding="utf-8")
        print(f"Wrote {FILES[source]}", flush=True)
    if len(selected) == len(FILES):
        manifest = {
            "source_repository": "https://github.com/eternity4719/HowToLiveBetter",
            "source_commit": subprocess.check_output(["git", "rev-parse", "origin/main"], cwd=ROOT, text=True).strip(),
            "translation_date": "2026-10-01",
            "language": "vi",
            "status": "machine-translated draft; structural checks and selected editorial corrections only",
            "engine": "Google Translate (zh-CN to vi)",
            "citations": "Original bibliographies and quoted source passages retained verbatim",
            "files": [{"source": src, "translation": dst,
                       "source_sha256": digest((ROOT / src).read_text(encoding="utf-8")),
                       "entries": len(re.findall(r"^### \d+\.", (ROOT / src).read_text(encoding="utf-8"), re.M)) if src.startswith("book/") else None}
                      for src, dst in FILES.items()]
        }
        (ROOT / "vi/translation-manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
