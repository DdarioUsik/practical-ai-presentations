#!/usr/bin/env python3
"""Check the eight sales pages, metadata, and local navigation before deploy."""
from __future__ import annotations

from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json

DOCS = Path(__file__).resolve().parents[1] / "docs"
BASE = "https://practical-ai.pro"


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.lang = ""
        self.title = ""
        self.description = ""
        self.canonical = ""
        self.hreflang: dict[str, str] = {}
        self.h1 = 0
        self.refs: list[str] = []
        self.sections: list[str] = []
        self.schemas: list[dict] = []
        self._title = False
        self._script = False
        self._schema = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "html": self.lang = a.get("lang", "")
        if tag == "title": self._title = True
        if tag == "h1": self.h1 += 1
        if tag == "section": self.sections.append(a.get("id", ""))
        if tag == "meta" and a.get("name") == "description": self.description = a.get("content", "")
        if tag == "link" and a.get("rel") == "canonical": self.canonical = a.get("href", "")
        if tag == "link" and a.get("hreflang"): self.hreflang[a["hreflang"]] = a.get("href", "")
        if tag == "script" and a.get("type") == "application/ld+json": self._script = True; self._schema = ""
        for key in ("href", "src"):
            if a.get(key): self.refs.append(a[key])

    def handle_endtag(self, tag):
        if tag == "title": self._title = False
        if tag == "script" and self._script:
            self.schemas.append(json.loads(self._schema))
            self._script = False

    def handle_data(self, data):
        if self._title: self.title += data
        if self._script: self._schema += data


def check() -> None:
    errors = []
    checked = 0
    for lang in ("en", "ru"):
        for route in ("", "for-hr", "programs", "about"):
            url_path = ("/ru" if lang == "ru" else "") + "/" + (route + "/" if route else "")
            path = DOCS / url_path.lstrip("/") / "index.html"
            parser = Page()
            parser.feed(path.read_text(encoding="utf-8"))
            checked += 1
            expected = BASE + url_path
            if parser.lang != lang: errors.append(f"{url_path}: lang {parser.lang}")
            if parser.canonical != expected: errors.append(f"{url_path}: canonical {parser.canonical}")
            if not parser.title or not parser.description: errors.append(f"{url_path}: metadata missing")
            if parser.h1 != 1: errors.append(f"{url_path}: {parser.h1} H1 elements")
            if len(parser.schemas) != 1: errors.append(f"{url_path}: JSON-LD count {len(parser.schemas)}")
            for other in ("en", "ru"):
                alternate = BASE + ("/ru" if other == "ru" else "") + "/" + (route + "/" if route else "")
                if parser.hreflang.get(other) != alternate: errors.append(f"{url_path}: {other} alternate mismatch")
            if route == "" and parser.sections[:2] != ["", "programs"]:
                errors.append(f"{url_path}: programs must be the second section")
            for ref in parser.refs:
                parsed = urlsplit(ref)
                if parsed.scheme or parsed.netloc or not parsed.path or ref.startswith("#"):
                    continue
                target = (DOCS / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else (path.parent / unquote(parsed.path))
                if target.is_dir(): target /= "index.html"
                if not target.is_file(): errors.append(f"{url_path}: missing {ref}")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {checked} sales pages; metadata, EN/RU alternates, JSON-LD, second section and local links")


if __name__ == "__main__":
    check()
