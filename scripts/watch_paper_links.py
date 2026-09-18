#!/usr/bin/env python3
"""Watch Markdown files and expand standalone paper URLs into bibliography entries."""

from __future__ import annotations

import argparse
import html
from html.parser import HTMLParser
import os
from pathlib import Path
import re
import sys
import time
from typing import Dict, Iterable, List, NamedTuple, Optional, Sequence, Tuple
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


DEFAULT_INTERVAL = 1.0
REQUEST_TIMEOUT = 15
IGNORED_DIRECTORIES = {
    ".git",
    ".idea",
    ".vscode",
    ".venv",
    "build",
    "dist",
    "node_modules",
    "__pycache__",
}

VENUES: Sequence[Tuple[str, str]] = (
    ("Robotics: Science and Systems", "RSS"),
    ("Computer Vision and Pattern Recognition", "CVPR"),
    ("International Conference on Computer Vision", "ICCV"),
    ("European Conference on Computer Vision", "ECCV"),
    ("Winter Conference on Applications of Computer Vision", "WACV"),
    ("Conference on Robot Learning", "CoRL"),
    ("International Conference on Robotics and Automation", "ICRA"),
    ("International Conference on Intelligent Robots and Systems", "IROS"),
    ("International Conference on Machine Learning", "ICML"),
    ("International Conference on Learning Representations", "ICLR"),
    ("Neural Information Processing Systems", "NeurIPS"),
    ("Association for Computational Linguistics", "ACL"),
    ("Empirical Methods in Natural Language Processing", "EMNLP"),
    (
        "North American Chapter of the Association for Computational Linguistics",
        "NAACL",
    ),
    ("AAAI Conference on Artificial Intelligence", "AAAI"),
    ("International Joint Conference on Artificial Intelligence", "IJCAI"),
    ("ACM Multimedia", "ACM MM"),
    ("British Machine Vision Conference", "BMVC"),
    ("SIGGRAPH", "SIGGRAPH"),
)

VENUE_ACRONYMS = (
    "CVPR",
    "ICCV",
    "ECCV",
    "WACV",
    "RSS",
    "CoRL",
    "ICRA",
    "IROS",
    "ICML",
    "ICLR",
    "NeurIPS",
    "NIPS",
    "ACL",
    "EMNLP",
    "NAACL",
    "COLING",
    "AAAI",
    "IJCAI",
    "AAMAS",
    "BMVC",
    "KDD",
    "SIGGRAPH",
    "CHI",
)


class Paper(NamedTuple):
    title: str
    authors: List[str]
    venue: str
    url: str
    label: str


class Candidate(NamedTuple):
    line: str
    indentation: str
    url: str


class Document(NamedTuple):
    text: str
    encoding: str
    bom: bytes


def clean_text(value: str = "") -> str:
    value = re.sub(r"<[^>]*>", " ", value)
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def escape_markdown(value: str) -> str:
    return re.sub(r"([\\`*_{}\[\]])", r"\\\1", value)


def first_year(value: str = "") -> str:
    match = re.search(r"\b(?:19|20)\d{2}\b", value)
    return match.group(0) if match else ""


def extract_venue(*values: str) -> str:
    value = " ".join(item for item in values if item)
    year = first_year(value)

    for long_name, acronym in VENUES:
        if long_name.casefold() in value.casefold():
            return " ".join(item for item in (acronym, year) if item)

    pattern = r"\b(" + "|".join(map(re.escape, VENUE_ACRONYMS)) + r")\b"
    match = re.search(pattern + r"(?:[\s'’,-]*(\d{2,4}))?", value, re.IGNORECASE)
    if not match:
        return ""

    canonical = next(
        item for item in VENUE_ACRONYMS if item.casefold() == match.group(1).casefold()
    )
    if canonical == "NIPS":
        canonical = "NeurIPS"
    venue_year = match.group(2) or year
    if len(venue_year) == 2:
        venue_year = "20" + venue_year
    return " ".join(item for item in (canonical, venue_year) if item)


def _local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def _first_child_text(element: ET.Element, local_name: str) -> str:
    for child in element.iter():
        if _local_name(child.tag) == local_name:
            return clean_text("".join(child.itertext()))
    return ""


def parse_arxiv_xml(xml: str, original_url: str) -> Paper:
    try:
        root = ET.fromstring(xml)
    except ET.ParseError as error:
        raise ValueError("arXiv 返回的 XML 无法解析") from error

    entry = next((item for item in root.iter() if _local_name(item.tag) == "entry"), None)
    if entry is None:
        raise ValueError("arXiv 没有返回论文信息")

    title = _first_child_text(entry, "title")
    authors = []
    for author in (item for item in entry if _local_name(item.tag) == "author"):
        name = _first_child_text(author, "name")
        if name:
            authors.append(name)
    comment = _first_child_text(entry, "comment")
    journal_ref = _first_child_text(entry, "journal_ref")

    if not title or not authors:
        raise ValueError("arXiv 返回的信息不完整")
    # Publication year alone is not evidence of a venue. If arXiv does not
    # explicitly mention a conference or journal, keep the source as Arxiv.
    venue = extract_venue(comment, journal_ref) or "Arxiv"
    return Paper(title, authors, venue, original_url, "Arxiv")


class CitationHTMLParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.metadata: Dict[str, List[str]] = {}
        self.title_parts: List[str] = []
        self._inside_title = False
        self._ignored_depth = 0

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, Optional[str]]]) -> None:
        tag = tag.casefold()
        attributes = {key.casefold(): value or "" for key, value in attrs}
        if tag == "meta":
            key = (attributes.get("name") or attributes.get("property") or "").casefold()
            if key and "content" in attributes:
                self.metadata.setdefault(key, []).append(clean_text(attributes["content"]))
        if tag == "title":
            self._inside_title = True
        if tag in {"script", "style"}:
            self._ignored_depth += 1

    def handle_endtag(self, tag: str) -> None:
        tag = tag.casefold()
        if tag == "title":
            self._inside_title = False
        if tag in {"script", "style"} and self._ignored_depth:
            self._ignored_depth -= 1

    def handle_data(self, data: str) -> None:
        if self._ignored_depth:
            return
        if self._inside_title and data.strip():
            self.title_parts.append(data)


def _first_metadata(metadata: Dict[str, List[str]], *keys: str) -> str:
    for key in keys:
        for value in metadata.get(key, []):
            if value:
                return value
    return ""


def _arxiv_comment_text(source: str) -> str:
    pattern = re.compile(
        r"<(td|div)\b[^>]*\bclass\s*=\s*(['\"])[^'\"]*\bcomments\b[^'\"]*\2[^>]*>"
        r"(.*?)</\1>",
        re.IGNORECASE | re.DOTALL,
    )
    return clean_text(" ".join(match.group(3) for match in pattern.finditer(source)))


def link_label(url: str) -> str:
    hostname = (urllib.parse.urlsplit(url).hostname or "").removeprefix("www.")
    if hostname.endswith("arxiv.org"):
        return "Arxiv"
    if hostname.endswith("openreview.net"):
        return "OpenReview"
    if hostname.endswith("thecvf.com"):
        return "CVF"
    if hostname in {"doi.org", "dx.doi.org"}:
        return "DOI"
    return "Paper"


def parse_paper_html(source: str, url: str) -> Paper:
    parser = CitationHTMLParser()
    parser.feed(source)
    metadata = parser.metadata
    html_title = clean_text(" ".join(parser.title_parts))
    title = _first_metadata(
        metadata,
        "citation_title",
        "dc.title",
        "dcterms.title",
        "og:title",
        "twitter:title",
    ) or html_title
    authors = [item for item in metadata.get("citation_author", []) if item]
    if not authors:
        authors = [
            item
            for item in (metadata.get("dc.creator") or metadata.get("author") or [])
            if item
        ]
    venue_name = _first_metadata(
        metadata,
        "citation_conference_title",
        "citation_journal_title",
    )
    if venue_name.casefold().startswith("arxiv"):
        venue_name = ""
    publication_date = _first_metadata(
        metadata,
        "citation_publication_date",
        "citation_date",
        "dc.date",
        "citation_year",
    )
    label = link_label(url)
    venue = extract_venue(venue_name, publication_date)
    if venue_name and not venue:
        venue = clean_text(venue_name)
        year = first_year(publication_date)
        if year and year not in venue:
            venue = f"{venue} {year}"
    if not venue and label == "Arxiv":
        venue = extract_venue(_arxiv_comment_text(source)) or "Arxiv"

    if not title or not authors:
        raise ValueError("网页缺少 citation_title 或 citation_author 元数据")
    return Paper(title, authors, venue, url, label)


def arxiv_id(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    if not (parsed.hostname or "").endswith("arxiv.org"):
        return ""
    match = re.fullmatch(r"/(?:abs|pdf)/(.+?)(?:\.pdf)?", parsed.path)
    return match.group(1) if match else ""


def metadata_page_url(url: str) -> str:
    parsed = urllib.parse.urlsplit(url)
    hostname = parsed.hostname or ""
    path = parsed.path
    if hostname.endswith("arxiv.org") and path.startswith("/pdf/"):
        path = re.sub(r"\.pdf$", "", path.replace("/pdf/", "/abs/", 1))
    if hostname.endswith("openreview.net") and path == "/pdf":
        path = "/forum"
    if hostname.endswith("thecvf.com") and path.endswith(".pdf"):
        path = path.replace("/papers/", "/html/").removesuffix(".pdf") + ".html"
    return urllib.parse.urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, parsed.fragment))


def fetch_text(url: str) -> str:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "text/html, application/atom+xml;q=0.9, */*;q=0.8",
            "User-Agent": "paper-reading-markdown-watcher/1.0 (metadata fetcher)",
        },
    )
    with urllib.request.urlopen(request, timeout=REQUEST_TIMEOUT) as response:
        payload = response.read()
        charset = response.headers.get_content_charset() or "utf-8"
        return payload.decode(charset, errors="replace")


def fetch_paper_metadata(url: str) -> Paper:
    identifier = arxiv_id(url)
    if identifier:
        endpoint = "https://export.arxiv.org/api/query?id_list=" + urllib.parse.quote(
            identifier, safe=""
        )
        try:
            return parse_arxiv_xml(fetch_text(endpoint), url)
        except (OSError, ValueError, ET.ParseError) as api_error:
            try:
                page_url = "https://arxiv.org/abs/" + urllib.parse.quote(identifier, safe="/")
                return parse_paper_html(fetch_text(page_url), url)
            except (OSError, ValueError) as page_error:
                raise RuntimeError(
                    f"arXiv API 与论文页均不可用: {api_error}; {page_error}"
                ) from page_error

    page_url = metadata_page_url(url)
    return parse_paper_html(fetch_text(page_url), url)


def normalize_author_name(author: str) -> str:
    """Render a metadata name as `Given Family`, without an internal comma."""
    name = clean_text(author)
    parts = [part.strip() for part in name.split(",") if part.strip()]
    if len(parts) == 2:
        return f"{parts[1]} {parts[0]}"
    return " ".join(parts) if len(parts) > 2 else name


def select_display_authors(authors: Sequence[str]) -> List[str]:
    """Normalize names; select the first and likely corresponding author."""
    cleaned = [normalize_author_name(author) for author in authors]
    cleaned = [author for author in cleaned if author]
    if len(cleaned) <= 2:
        return cleaned
    return [cleaned[0], cleaned[-1]]


def format_entry(paper: Paper, indentation: str = "") -> str:
    authors = ",  ".join(select_display_authors(paper.authors))
    venue = f"**{escape_markdown(clean_text(paper.venue) or 'Arxiv')}**"
    title = escape_markdown(clean_text(paper.title))
    return (
        f"{indentation}- **{title}** & {authors} & {venue} & "
        f"[{paper.label}]({paper.url})"
    )


def find_url_only_lines(content: str) -> List[Candidate]:
    candidates: List[Candidate] = []
    fence = ""
    for line in content.splitlines():
        fence_match = re.match(r"^\s*(`{3,}|~{3,})", line)
        if fence_match:
            marker = fence_match.group(1)[0]
            if not fence:
                fence = marker
            elif fence == marker:
                fence = ""
            continue
        if fence:
            continue
        match = re.match(r"^(\s*)(?:-\s*)?(https?://\S+?)\s*$", line)
        if match:
            candidates.append(Candidate(line, match.group(1), match.group(2)))
    return candidates


def read_document(path: Path) -> Document:
    payload = path.read_bytes()
    if payload.startswith(b"\xff\xfe"):
        return Document(payload[2:].decode("utf-16-le"), "utf-16-le", b"\xff\xfe")
    if payload.startswith(b"\xfe\xff"):
        return Document(payload[2:].decode("utf-16-be"), "utf-16-be", b"\xfe\xff")
    if payload.startswith(b"\xef\xbb\xbf"):
        return Document(payload[3:].decode("utf-8"), "utf-8", b"\xef\xbb\xbf")
    return Document(payload.decode("utf-8"), "utf-8", b"")


def write_document(path: Path, text: str, document: Document) -> None:
    path.write_bytes(document.bom + text.encode(document.encoding))


def markdown_files(root: Path) -> Iterable[Path]:
    for directory, names, filenames in os.walk(root):
        names[:] = [name for name in names if name not in IGNORED_DIRECTORIES]
        for filename in filenames:
            if filename.casefold().endswith(".md"):
                yield Path(directory, filename)


def process_markdown_file(
    path: Path, metadata_cache: Dict[str, Paper], dry_run: bool = False
) -> int:
    try:
        original = read_document(path)
    except FileNotFoundError:
        return 0

    candidates = find_url_only_lines(original.text)
    if not candidates:
        return 0

    replacements: Dict[str, str] = {}
    for candidate in candidates:
        try:
            paper = metadata_cache.get(candidate.url)
            if paper is None:
                paper = fetch_paper_metadata(candidate.url)
                metadata_cache[candidate.url] = paper
            replacements[candidate.line] = format_entry(paper, candidate.indentation)
        except (OSError, RuntimeError, ValueError, urllib.error.URLError) as error:
            print(f"[跳过] {candidate.url}: {error}", file=sys.stderr)

    if not replacements:
        return 0

    latest = read_document(path)
    segments = latest.text.splitlines(keepends=True)
    changed = 0
    for index, segment in enumerate(segments):
        ending_match = re.search(r"(?:\r\n|\r|\n)$", segment)
        ending = ending_match.group(0) if ending_match else ""
        line = segment[: -len(ending)] if ending else segment
        if line in replacements:
            segments[index] = replacements[line] + ending
            changed += 1
    if not changed:
        return 0

    updated = "".join(segments)
    if dry_run:
        print(f"[预览] {path}")
        for replacement in replacements.values():
            print(f"  {replacement}")
    else:
        write_document(path, updated, latest)
        print(f"[已展开] {path} ({changed} 条)")
    return changed


def process_all(root: Path, metadata_cache: Dict[str, Paper], dry_run: bool) -> int:
    return sum(
        process_markdown_file(path, metadata_cache, dry_run)
        for path in markdown_files(root)
    )


def snapshot(root: Path) -> Dict[Path, Tuple[int, int]]:
    result: Dict[Path, Tuple[int, int]] = {}
    for path in markdown_files(root):
        try:
            info = path.stat()
            result[path] = (info.st_mtime_ns, info.st_size)
        except FileNotFoundError:
            pass
    return result


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="监听 Markdown 文件，把单独一行的论文 URL 展开成论文条目。"
    )
    parser.add_argument("--once", action="store_true", help="扫描一次后退出")
    parser.add_argument("--dry-run", action="store_true", help="只预览，不写入文件")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="扫描目录")
    parser.add_argument(
        "--interval", type=float, default=DEFAULT_INTERVAL, help="监听间隔（秒）"
    )
    arguments = parser.parse_args()
    if arguments.interval < 0.2:
        parser.error("--interval 必须是不小于 0.2 的秒数")
    arguments.root = arguments.root.resolve()
    return arguments


def main() -> int:
    arguments = parse_arguments()
    metadata_cache: Dict[str, Paper] = {}
    print(f"[扫描目录] {arguments.root}")
    process_all(arguments.root, metadata_cache, arguments.dry_run)
    if arguments.once:
        return 0

    previous = snapshot(arguments.root)
    print("[监听中] 在 Markdown 中粘贴单独一行的论文 URL；按 Ctrl+C 退出。")
    try:
        while True:
            time.sleep(arguments.interval)
            current = snapshot(arguments.root)
            changed_paths = [
                path for path, signature in current.items() if previous.get(path) != signature
            ]
            previous = current
            for path in changed_paths:
                process_markdown_file(path, metadata_cache, arguments.dry_run)
    except KeyboardInterrupt:
        print("\n[已停止]")
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
