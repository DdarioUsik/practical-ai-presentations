#!/usr/bin/env python3
"""Check the nine sales pages, metadata, and local navigation before deploy."""
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
    routes = [(lang, route) for lang in ("en", "ru") for route in ("", "for-hr", "programs", "about")]
    routes.append(("ru", "for-schools"))
    for lang, route in routes:
            url_path = ("/ru" if lang == "ru" else "") + "/" + (route + "/" if route else "")
            path = DOCS / url_path.lstrip("/") / "index.html"
            parser = Page()
            html = path.read_text(encoding="utf-8")
            parser.feed(html)
            checked += 1
            expected = BASE + url_path
            if parser.lang != lang: errors.append(f"{url_path}: lang {parser.lang}")
            if parser.canonical != expected: errors.append(f"{url_path}: canonical {parser.canonical}")
            if not parser.title or not parser.description: errors.append(f"{url_path}: metadata missing")
            if parser.h1 != 1: errors.append(f"{url_path}: {parser.h1} H1 elements")
            if len(parser.schemas) != 1: errors.append(f"{url_path}: JSON-LD count {len(parser.schemas)}")
            if route == "for-schools":
                if parser.hreflang.get("ru") != expected or parser.hreflang.get("x-default") != expected or "en" in parser.hreflang:
                    errors.append(f"{url_path}: Russian-only language alternates mismatch")
            else:
                for other in ("en", "ru"):
                    alternate = BASE + ("/ru" if other == "ru" else "") + "/" + (route + "/" if route else "")
                    if parser.hreflang.get(other) != alternate: errors.append(f"{url_path}: {other} alternate mismatch")
            if route == "" and parser.sections[:2] != ["", "programs"]:
                errors.append(f"{url_path}: programs must be the second section")
            if 'href="#main-content"' not in html or 'id="main-content"' not in html:
                errors.append(f"{url_path}: keyboard skip target missing")
            if route != "for-schools" and ('https://wa.me/34627184000?text=' not in html or 'https://www.linkedin.com/in/danielusik/' not in html):
                errors.append(f"{url_path}: WhatsApp primary or LinkedIn alternative missing")
            if lang == "ru" and 'href="/ru/for-schools/"' not in html:
                errors.append(f"{url_path}: Russian school navigation missing")
            if lang == "en" and 'href="/for-schools/"' in html:
                errors.append(f"{url_path}: untranslated school route linked from English page")
            if route in ("", "about"):
                names = ("Danil Usik", "Svetlana Galakhova", "Julia Krylova") if lang == "en" else ("Данил Усик", "Светлана Галахова", "Юлия Крылова")
                if html.count('class="team-card"') != 3 or any(name not in html for name in names):
                    errors.append(f"{url_path}: three named core-team profiles missing")
                if any(profile not in html for profile in ('https://www.linkedin.com/in/danielusik/', 'https://www.linkedin.com/in/svetlana-galakhova/', 'https://www.linkedin.com/in/juliakrl/')):
                    errors.append(f"{url_path}: core-team profile links missing")
            if route == "" and ("class=\"quote-grid\"" not in html or "class=\"proof-facts\"" not in html):
                errors.append(f"{url_path}: case metrics or participant quotes missing")
            if route == "":
                proof_terms = ("Reports and presentations", "Market and competitor research", "ERP formula debugging", "HR routine with voice input") if lang == "en" else ("Отчёты и презентации", "Анализ рынка и конкурентов", "Отладка формул в ERP", "HR-рутина с голосовым вводом")
                if html.count('class="proof-metric"') != 4 or any(term not in html for term in proof_terms):
                    errors.append(f"{url_path}: four explained case results missing")
            if route != "for-schools" and (html.count('class="program-visual"') != 3 or html.count('class="program-fit"') != 3):
                errors.append(f"{url_path}: program thumbnails or audience details missing")
            if route == "for-schools":
                school_requirements = (
                    'class="school-format-card"',
                    'class="school-practice-grid"',
                    'Работы и личные данные учеников остаются внутри школы',
                    'сам принимает решение об оценке',
                    'Обсудить программу',
                )
                if any(requirement not in html for requirement in school_requirements):
                    errors.append(f"{url_path}: school offer, active contact, learning example, or privacy copy missing")
                if any(term in html for term in ('school-draft-notice', 'school-cta-pending', 'school-contact-pending', 'Требует подтверждения', 'локальный черновик')):
                    errors.append(f"{url_path}: internal draft-only release note remains on the public school page")
                if not any(ref.startswith("https://wa.me/") for ref in parser.refs) or not any(ref.startswith("https://www.linkedin.com/in/") for ref in parser.refs):
                    errors.append(f"{url_path}: active WhatsApp and LinkedIn school contact links missing")
                if html.count('class="school-format-card') != 4:
                    errors.append(f"{url_path}: four school program duration cards missing")
                school_prices = ('$1,500', '$3,000', '$4,500', '$9,000', 'за группу до 15 человек', 'для 200 человек стоит $9,000', 'Отдельно обсудим стоимость для групп другого размера, место проведения и расходы на выезд')
                if any(price not in html for price in school_prices) or html.count('class="school-format-card') != 4:
                    errors.append(f"{url_path}: approved school format pricing missing or incomplete")
                if 'Без публичной цены' in html:
                    errors.append(f"{url_path}: outdated no-public-price copy remains")
                if 'href="/"' not in html or 'hreflang="en"' in html:
                    errors.append(f"{url_path}: school page should switch to the English home page without claiming a translation")
                if 'class="school-page"' not in html:
                    errors.append(f"{url_path}: school page styles are not scoped")
            if '<figcaption>Illustration</figcaption>' in html or '<figcaption>Иллюстрация</figcaption>' in html:
                errors.append(f"{url_path}: obsolete illustration label")
            language_label = "RU" if lang == "en" else "EN"
            if f'class="lang-switch"' not in html or f'>{language_label}</a>' not in html:
                errors.append(f"{url_path}: language switch label missing")
            if route in ("", "programs", "about") and f'/assets/brand/workflow-method-{lang}.svg' not in html:
                errors.append(f"{url_path}: localized method visual missing")
            if route in ("", "programs", "about") and f'/assets/brand/workflow-method-{lang}-mobile.svg' not in html:
                errors.append(f"{url_path}: readable mobile method visual missing")
            if route == "" and 'class="case-image"' in html:
                errors.append(f"{url_path}: synthetic image remains in the evidence block")
            for ref in parser.refs:
                parsed = urlsplit(ref)
                if parsed.scheme or parsed.netloc or not parsed.path or ref.startswith("#"):
                    continue
                target = (DOCS / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else (path.parent / unquote(parsed.path))
                if target.is_dir(): target /= "index.html"
                if not target.is_file(): errors.append(f"{url_path}: missing {ref}")
    guide_count = 0
    for lang in ("en", "ru"):
        root = DOCS / ("ru" if lang == "ru" else "") / "blog"
        for path in [root / "index.html", *sorted(root.glob("*/index.html"))]:
            if path.parent.name == "ai-my-voice":
                continue
            slug = "" if path.parent == root else path.parent.name + "/"
            url_path = ("/ru" if lang == "ru" else "") + "/blog/" + slug
            html = path.read_text(encoding="utf-8")
            parser = Page()
            parser.feed(html)
            guide_count += 1
            if parser.lang != lang or parser.canonical != BASE + url_path or parser.h1 != 1:
                errors.append(f"{url_path}: language, canonical or H1 mismatch")
            if 'class="site-blog"' not in html or '/assets/brand/blog-bridge.css' not in html:
                errors.append(f"{url_path}: shared editorial styles missing")
            if html.count('class="site-header"') != 1 or html.count('class="site-footer"') != 1:
                errors.append(f"{url_path}: shared header/footer missing")
            if 'href="#main-content"' not in html or 'id="main-content"' not in html:
                errors.append(f"{url_path}: keyboard skip target missing")
            if 'https://wa.me/34627184000?text=' not in html or 'https://www.linkedin.com/in/danielusik/' not in html:
                errors.append(f"{url_path}: WhatsApp primary or LinkedIn alternative missing")
            nav_paths = ("for-hr", "programs", "about", "blog", "for-schools") if lang == "ru" else ("for-hr", "programs", "about", "blog")
            for nav_path in nav_paths:
                if f'href="{("/ru" if lang == "ru" else "")}/{nav_path}/"' not in html:
                    errors.append(f"{url_path}: {nav_path} navigation missing")
            other = "ru" if lang == "en" else "en"
            other_url_path = ("/ru" if other == "ru" else "") + "/blog/" + slug
            if parser.hreflang.get(other) != BASE + other_url_path:
                errors.append(f"{url_path}: language alternate mismatch")
            if f'class="lang-switch" href="{other_url_path}"' not in html:
                errors.append(f"{url_path}: language switch mismatch")
            for ref in parser.refs:
                parsed = urlsplit(ref)
                if parsed.scheme or parsed.netloc or not parsed.path or ref.startswith("#"):
                    continue
                target = (DOCS / unquote(parsed.path).lstrip("/")) if parsed.path.startswith("/") else (path.parent / unquote(parsed.path))
                if target.is_dir(): target /= "index.html"
                if not target.is_file(): errors.append(f"{url_path}: missing {ref}")
    legacy = (DOCS / "blog/ai-my-voice/index.html").read_text(encoding="utf-8")
    if legacy.count('class="site-header"') != 1 or legacy.count('class="site-footer"') != 1:
        errors.append("/blog/ai-my-voice/: shared header/footer missing")
    if errors:
        raise SystemExit("\n".join(errors))
    print(f"PASS: {checked} sales pages and {guide_count + 1} editorial pages; shared navigation, metadata, language links and local assets")


if __name__ == "__main__":
    check()
