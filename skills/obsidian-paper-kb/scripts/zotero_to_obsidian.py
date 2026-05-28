#!/usr/bin/env python3
"""Read a Zotero local item and create an Obsidian paper-note scaffold."""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import textwrap
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, unquote, urlencode, urlparse
from urllib.request import Request, urlopen


DEFAULT_ZOTERO = "http://127.0.0.1:23119"
DEFAULT_VAULT = r"D:\Masterdegree_obsidian\Masterdegree"


class ZoteroError(RuntimeError):
    pass


def api_get(base_url: str, path: str, params: dict[str, Any] | None = None) -> Any:
    query = f"?{urlencode(params or {})}" if params else ""
    url = f"{base_url.rstrip('/')}{path}{query}"
    req = Request(url, headers={"Zotero-API-Version": "3"})
    try:
        with urlopen(req, timeout=12) as resp:
            body = resp.read().decode("utf-8")
    except HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")
        raise ZoteroError(f"Zotero API HTTP {exc.code}: {detail}") from exc
    except URLError as exc:
        raise ZoteroError(f"Cannot reach Zotero local API at {base_url}: {exc}") from exc
    if not body:
        return None
    return json.loads(body)


def get_item_by_key(base_url: str, key: str) -> dict[str, Any] | None:
    if not re.fullmatch(r"[A-Za-z0-9]{8}", key):
        return None
    try:
        item = api_get(base_url, f"/api/users/0/items/{quote(key.upper())}", {"format": "json"})
    except ZoteroError as exc:
        if "HTTP 404" in str(exc):
            return None
        raise
    if item and item.get("data", {}).get("itemType") not in {"attachment", "note"}:
        return item
    return None


def search_items(base_url: str, query: str, limit: int) -> list[dict[str, Any]]:
    items = api_get(
        base_url,
        "/api/users/0/items",
        {
            "format": "json",
            "limit": limit,
            "q": query,
            "itemType": "-attachment || note",
        },
    )
    if not isinstance(items, list):
        return []
    return [item for item in items if item.get("data", {}).get("itemType") not in {"attachment", "note"}]


def norm(value: Any) -> str:
    return str(value or "").strip()


def score_item(item: dict[str, Any], query: str) -> int:
    q = query.strip().lower()
    data = item.get("data", {})
    key = norm(data.get("key")).lower()
    citekey = norm(data.get("citationKey")).lower()
    doi = norm(data.get("DOI")).lower()
    title = norm(data.get("title")).lower()
    if q == key:
        return 100
    if q == citekey:
        return 95
    if q == doi:
        return 90
    if q == title:
        return 85
    if q and q in title:
        return 70
    if q and q in citekey:
        return 65
    if q and any(q in norm(tag.get("tag")).lower() for tag in data.get("tags", [])):
        return 40
    return 10


def choose_item(base_url: str, query: str, limit: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    direct = get_item_by_key(base_url, query)
    if direct:
        return direct, [direct]
    candidates = search_items(base_url, query, limit)
    if not candidates:
        raise ZoteroError(f"No Zotero items matched query: {query}")
    ranked = sorted(candidates, key=lambda item: score_item(item, query), reverse=True)
    return ranked[0], ranked


def children(base_url: str, item_key: str) -> list[dict[str, Any]]:
    data = api_get(base_url, f"/api/users/0/items/{quote(item_key)}/children", {"format": "json"})
    return data if isinstance(data, list) else []


def file_url_to_path(href: str) -> str:
    parsed = urlparse(href)
    if parsed.scheme != "file":
        return ""
    path = unquote(parsed.path)
    if re.match(r"^/[A-Za-z]:/", path):
        path = path[1:]
    return path.replace("/", "\\")


def pdf_attachments(base_url: str, item_key: str) -> list[dict[str, str]]:
    result: list[dict[str, str]] = []
    for child in children(base_url, item_key):
        data = child.get("data", {})
        if data.get("itemType") != "attachment" or data.get("contentType") != "application/pdf":
            continue
        enclosure = child.get("links", {}).get("enclosure", {})
        href = norm(enclosure.get("href"))
        result.append(
            {
                "key": norm(data.get("key")),
                "title": norm(enclosure.get("title") or data.get("filename") or data.get("title")),
                "href": href,
                "path": file_url_to_path(href),
            }
        )
    return result


def creators_text(creators: list[dict[str, Any]]) -> str:
    names = []
    for creator in creators:
        last = norm(creator.get("lastName"))
        first = norm(creator.get("firstName"))
        name = " ".join(part for part in [first, last] if part)
        if not name:
            name = norm(creator.get("name"))
        if name:
            names.append(name)
    return "; ".join(names) if names else "unknown"


def year_from_date(date: str) -> str:
    match = re.search(r"\d{4}", date or "")
    return match.group(0) if match else "unknown"


def venue(data: dict[str, Any]) -> str:
    for key in ("publicationTitle", "proceedingsTitle", "conferenceName", "publisher", "university"):
        value = norm(data.get(key))
        if value:
            return value
    return "unknown"


def yaml_quote(value: Any) -> str:
    text = norm(value).replace("\\", "\\\\").replace('"', '\\"')
    return f'"{text}"'


def safe_filename(text: str, fallback: str) -> str:
    value = norm(text) or fallback
    value = re.sub(r'[<>:"/\\|?*\x00-\x1f]', " ", value)
    value = re.sub(r"\s+", " ", value).strip(" .")
    return value[:150] or fallback


def extract_title_translation(extra: str) -> str:
    for line in (extra or "").splitlines():
        if line.lower().startswith("titletranslation:"):
            return line.split(":", 1)[1].strip()
    return ""


def extract_pdf_text(path: str, max_chars: int) -> str:
    if not path or max_chars <= 0:
        return ""
    pdf_path = Path(path)
    if not pdf_path.exists():
        return ""
    try:
        from pypdf import PdfReader
    except Exception:
        return ""
    try:
        reader = PdfReader(str(pdf_path))
        chunks: list[str] = []
        for page in reader.pages:
            chunks.append(page.extract_text() or "")
            if sum(len(chunk) for chunk in chunks) >= max_chars:
                break
        text = "\n".join(chunks)
    except Exception:
        return ""
    return text[:max_chars].strip()


def markdown_note(item: dict[str, Any], pdfs: list[dict[str, str]], text_excerpt: str) -> str:
    data = item.get("data", {})
    title = norm(data.get("title")) or "Untitled"
    citekey = norm(data.get("citationKey")) or "unknown"
    item_key = norm(data.get("key"))
    tags = ["paper", "zotero"]
    for tag in data.get("tags", []):
        tag_value = norm(tag.get("tag"))
        if tag_value:
            tags.append(tag_value)
    first_pdf = pdfs[0] if pdfs else {}
    title_translation = extract_title_translation(norm(data.get("extra")))
    abstract = norm(data.get("abstractNote"))
    tag_lines = "\n".join(f"  - {yaml_quote(tag)}" for tag in tags)
    pdf_path = first_pdf.get("path", "")
    pdf_href = first_pdf.get("href", "")
    today = _dt.date.today().isoformat()
    excerpt_block = ""
    if text_excerpt:
        excerpt_block = "\n## PDF Text Excerpt For Codex\n\n" + textwrap.shorten(
            re.sub(r"\s+", " ", text_excerpt), width=5000, placeholder=" ..."
        ) + "\n"
    return f"""---
type: paper
status: imported
zotero_item_key: {yaml_quote(item_key)}
citekey: {yaml_quote(citekey)}
zotero_uri: {yaml_quote(f"zotero://select/library/items/{item_key}" if item_key else "")}
authors: {yaml_quote(creators_text(data.get("creators", [])))}
year: {yaml_quote(year_from_date(norm(data.get("date"))))}
venue: {yaml_quote(venue(data))}
doi: {yaml_quote(data.get("DOI"))}
pdf: {yaml_quote(pdf_path)}
tags:
{tag_lines}
created: {yaml_quote(today)}
---

# {title}

## One-Sentence Takeaway


## Bibliographic Info

- Zotero item: `zotero://select/library/items/{item_key}`
- Citekey: `{citekey}`
- DOI: {norm(data.get("DOI")) or "unknown"}
- PDF: {pdf_path or pdf_href or "unknown"}

## Title Translation

{title_translation or ""}

## Abstract

{abstract or ""}

## Reading Questions

- 

## Research Problem


## Main Idea


## Method


## Key Formulas Or Algorithms


## Experiments Or Evidence


## Main Findings


## Limitations


## Reusable Concepts

- 

## Connections

- Topics:
- Related papers:
- Thesis relevance:

## Follow-Up Tasks

- [ ] Read the paper and replace the scaffold with a synthesized note.
{excerpt_block}"""


def note_path(vault: Path, item: dict[str, Any]) -> Path:
    data = item.get("data", {})
    citekey = norm(data.get("citationKey"))
    key = norm(data.get("key")) or "zotero-item"
    title = safe_filename(norm(data.get("title")), key)
    prefix = safe_filename(citekey or key, key)
    return vault / "10-Papers" / f"{prefix} - {title}.md"


def build_result(args: argparse.Namespace) -> dict[str, Any]:
    item, candidates = choose_item(args.zotero_url, args.query, args.limit)
    data = item.get("data", {})
    pdfs = pdf_attachments(args.zotero_url, data.get("key"))
    text_excerpt = extract_pdf_text(pdfs[0]["path"], args.text_chars) if pdfs else ""
    vault = Path(args.vault)
    output_path = note_path(vault, item)
    note = markdown_note(item, pdfs, text_excerpt if args.include_excerpt else "")
    return {
        "query": args.query,
        "selected": {
            "key": data.get("key"),
            "citationKey": data.get("citationKey"),
            "title": data.get("title"),
            "year": year_from_date(norm(data.get("date"))),
            "doi": data.get("DOI"),
            "itemType": data.get("itemType"),
            "authors": creators_text(data.get("creators", [])),
            "tags": [tag.get("tag") for tag in data.get("tags", []) if tag.get("tag")],
        },
        "pdfs": pdfs,
        "pdfTextExcerpt": text_excerpt,
        "candidateCount": len(candidates),
        "outputPath": str(output_path),
        "note": note,
    }


def write_note(path: Path, note: str, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and not overwrite:
        raise ZoteroError(f"Output note already exists. Use --overwrite to replace it: {path}")
    path.write_text(note, encoding="utf-8")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--query", required=True, help="Zotero item key, citation key, DOI, or title search.")
    parser.add_argument("--vault", default=DEFAULT_VAULT, help=f"Obsidian vault path. Default: {DEFAULT_VAULT}")
    parser.add_argument("--zotero-url", default=DEFAULT_ZOTERO, help=f"Zotero local API URL. Default: {DEFAULT_ZOTERO}")
    parser.add_argument("--limit", type=int, default=50, help="Maximum search candidates to inspect.")
    parser.add_argument("--text-chars", type=int, default=0, help="Extract this many characters from the first PDF.")
    parser.add_argument("--include-excerpt", action="store_true", help="Include extracted PDF text excerpt in the note.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files; print the selected output path.")
    parser.add_argument("--overwrite", action="store_true", help="Replace an existing note.")
    parser.add_argument("--json", action="store_true", help="Print structured JSON result.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv or sys.argv[1:])
    try:
        result = build_result(args)
        if not args.dry_run:
            write_note(Path(result["outputPath"]), result["note"], args.overwrite)
        if args.json:
            printable = dict(result)
            if not args.include_excerpt:
                printable.pop("note", None)
            print(json.dumps(printable, ensure_ascii=False, indent=2))
        else:
            action = "Would write" if args.dry_run else "Wrote"
            print(f"{action}: {result['outputPath']}")
            print(f"Selected: {result['selected']['citationKey'] or result['selected']['key']} - {result['selected']['title']}")
            if result["pdfs"]:
                print(f"PDF: {result['pdfs'][0]['path'] or result['pdfs'][0]['href']}")
            else:
                print("PDF: none found")
        return 0
    except ZoteroError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
