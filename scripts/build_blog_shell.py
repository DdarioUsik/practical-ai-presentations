#!/usr/bin/env python3
"""Keep the editorial pages in the shared Practical AI site shell."""
from __future__ import annotations

import re
from pathlib import Path

from build_sales_site import DOCS, site_footer, site_header


def replace_once(html: str, pattern: str, replacement: str, path: Path) -> str:
    updated, count = re.subn(pattern, lambda _: replacement, html, count=1, flags=re.S)
    if count != 1:
        raise ValueError(f"Expected one match for {pattern!r} in {path}")
    return updated


def build_page(path: Path, lang: str, slug: str) -> None:
    html = path.read_text(encoding="utf-8")
    route = f"blog/{slug}" if slug else "blog"
    html = replace_once(
        html,
        r'<header class="(?:blog-nav|site-header)">.*?</header>',
        site_header(lang, "blog", route),
        path,
    )
    html = replace_once(
        html,
        r'<footer class="site-footer">.*?</footer>',
        site_footer(lang, "blog"),
        path,
    )
    html = replace_once(
        html,
        r'<link rel="stylesheet" href="[^"]*/assets/brand/(?:brand|sales-site)\.css">(?:<link rel="stylesheet" href="/assets/brand/blog-bridge\.css">)?',
        '<link rel="stylesheet" href="/assets/brand/sales-site.css"><link rel="stylesheet" href="/assets/brand/blog-bridge.css">',
        path,
    )
    html = replace_once(html, r'<body(?: class="site-blog")?>', '<body class="site-blog">', path)
    old_label, new_label = ("Blog", "Guides") if lang == "en" else ("Блог", "Руководства")
    html = html.replace(f'>{old_label}</a>', f'>{new_label}</a>').replace(f'>{old_label}</span>', f'>{new_label}</span>')
    path.write_text(html, encoding="utf-8")


def build_legacy_article(path: Path) -> None:
    html = path.read_text(encoding="utf-8")
    html = replace_once(html, r'<header class="(?:nav|site-header)">.*?</header>', site_header("ru", "blog", "blog"), path)
    html = replace_once(html, r'<body class="(?:personal-article|personal-article site-blog)">', '<body class="personal-article site-blog">', path)
    html = html.replace('  <link rel="stylesheet" href="../../assets/brand/brand.css" />\n', '')
    styles = '<link rel="stylesheet" href="/assets/brand/sales-site.css"><link rel="stylesheet" href="/assets/brand/blog-bridge.css">'
    if styles not in html:
        html = html.replace('</head>', f'{styles}\n</head>', 1)
    footer = site_footer("ru", "blog")
    if '<footer class="site-footer">' in html:
        html = replace_once(html, r'<footer class="site-footer">.*?</footer>', footer, path)
    else:
        html = html.replace('</body>', footer + '\n</body>', 1)
    html = html.replace('href="../">← Blog', 'href="/ru/blog/">← Руководства')
    path.write_text(html, encoding="utf-8")


def main() -> None:
    count = 0
    for lang in ("en", "ru"):
        root = DOCS / ("ru" if lang == "ru" else "") / "blog"
        for path in [root / "index.html", *sorted(root.glob("*/index.html"))]:
            if path.parent.name == "ai-my-voice":
                continue
            build_page(path, lang, "" if path.parent == root else path.parent.name)
            count += 1
    build_legacy_article(DOCS / "blog/ai-my-voice/index.html")
    print(f"Unified {count + 1} editorial pages with the shared site shell")


if __name__ == "__main__":
    main()
