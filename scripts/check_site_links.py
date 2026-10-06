#!/usr/bin/env python3
"""Check local assets, page links and fragment targets across the published site."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

DOCS = Path(__file__).resolve().parents[1] / "docs"
BASE = "https://practical-ai.pro/"


class References(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.refs = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag == "a" and attrs.get("name"):
            self.ids.add(attrs["name"])
        for key in ("href", "src", "poster"):
            if attrs.get(key):
                self.refs.append(attrs[key])
        if attrs.get("srcset"):
            self.refs.extend(part.strip().split()[0] for part in attrs["srcset"].split(",") if part.strip())


def check():
    pages = {}
    for path in sorted(DOCS.rglob("*.html")):
        parsed = References()
        parsed.feed(path.read_text(encoding="utf-8"))
        pages[path.resolve()] = parsed
    errors = []
    checked = 0
    for path, parsed in pages.items():
        current = BASE + path.relative_to(DOCS).as_posix()
        for ref in parsed.refs:
            url = urlsplit(urljoin(current, ref))
            if url.scheme not in ("http", "https") or url.netloc not in ("practical-ai.pro", "www.practical-ai.pro"):
                continue
            target = (DOCS / unquote(url.path).lstrip("/")).resolve()
            if not target.is_relative_to(DOCS):
                errors.append(f"{path.relative_to(DOCS)}: path escapes site: {ref}")
                continue
            if target.is_dir():
                target /= "index.html"
            checked += 1
            if not target.is_file():
                errors.append(f"{path.relative_to(DOCS)}: missing target {ref}")
            elif url.fragment and target in pages and unquote(url.fragment) not in pages[target].ids:
                errors.append(f"{path.relative_to(DOCS)}: missing anchor {ref}")
    if errors:
        raise SystemExit("\n".join(sorted(set(errors))))
    print(f"PASS: {len(pages)} HTML pages, {checked} local page/asset/fragment references")


if __name__ == "__main__":
    check()
