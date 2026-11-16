"""Shared destinations and contact controls for public Practical AI pages."""
import os
import re
from pathlib import Path
from urllib.parse import urlsplit

DOCS = Path(__file__).resolve().parents[1] / "docs"
EMAIL = "mailto:argentinausik@gmail.com"
WHATSAPP = "https://wa.me/34627184000"
ASSET = '<link rel="stylesheet" href="/assets/brand/site-chrome.css"><script src="/assets/site-engagement.js" defer></script>'


def destinations(lang):
    if lang == "ru":
        return [
            ("/ru/programs/", "Обучение"), ("/ru/#cases", "Кейсы"),
            ("/ru/about/", "Команда"), ("/ru/for-schools/", "Для школ"),
            ("/ru/blog/", "Статьи"), ("/corporate-trainings/", "Внедрение (EN)"),
        ]
    return [
        ("/programs/", "Training"), ("/#cases", "Case studies"),
        ("/about/", "Team"), ("/for-schools/", "Schools"),
        ("/blog/", "Guides"), ("/corporate-trainings/", "Corporate rollout"),
    ]


def contact_links(lang, route):
    prefix = "/ru" if lang == "ru" else ""
    form = "#contact" if route == "for-schools" else prefix + "/assessment/#assessment-form"
    labels = ("Заполнить заявку", "Написать на почту", "Данил в WhatsApp") if lang == "ru" else (
        "Fill in the enquiry form", "Email Danil", "Message Danil on WhatsApp")
    return "".join(
        f'<a href="{url}" data-contact="{channel}">{label}</a>'
        for url, label, channel in zip((form, EMAIL, WHATSAPP), labels, ("form", "email", "whatsapp"))
    )


def standalone_header(lang, route):
    root = "/ru/" if lang == "ru" else "/"
    label = "Основное меню" if lang == "ru" else "Main menu"
    menu = "Меню" if lang == "ru" else "Menu"
    links = "".join(f'<a href="{url}">{name}</a>' for url, name in destinations(lang))
    switch = '<a href="/" lang="en">EN</a>' if lang == "ru" else '<a href="/ru/" lang="ru">RU</a>'
    form = contact_links(lang, route).split("</a>", 1)[0] + "</a>"
    return (
        f'<header class="pa-public-header"><div class="pa-public-bar">'
        f'<a href="{root}"><img src="/assets/brand/glass/wordmark.svg" alt="Practical AI" width="470" height="140"></a>'
        f'<div class="pa-public-links" role="navigation" aria-label="{label}">{links}{form}</div>'
        f'<details class="pa-public-menu"><summary>{menu}</summary>'
        f'<div role="navigation" aria-label="{label}">{links}{form}</div></details>{switch}</div></header>'
    )


def add_public_chrome():
    ga4_id = os.environ.get("PRACTICAL_AI_GA4_ID", "")
    if ga4_id and not re.fullmatch(r"G-[A-Z0-9]+", ga4_id):
        raise ValueError("PRACTICAL_AI_GA4_ID must be a GA4 measurement ID")
    tag = f'<meta name="pa-ga4-id" content="{ga4_id}">' if ga4_id else ""
    locations = re.findall(r"<loc>([^<]+)</loc>", (DOCS / "sitemap.xml").read_text())
    for location in locations:
        route = urlsplit(location).path.strip("/")
        target = DOCS / route
        if target.is_dir():
            target /= "index.html"
        html = target.read_text()
        if re.search(r'<meta[^>]+http-equiv=["\']refresh', html, re.I):
            continue
        html = html.replace(ASSET, "")
        html = re.sub(r'<meta name="pa-ga4-id" content="[^"]*">', "", html)
        html = re.sub(r'<header class="pa-public-header">.*?</header>', "", html, count=1, flags=re.S)
        html = re.sub(r'<div id="pa-contact-links" class="pa-contact-links">.*?</div>', "", html, count=1, flags=re.S)
        lang = "ru" if re.search(r'<html\b[^>]*\blang=["\']ru', html) else "en"
        page_route = route.removeprefix("ru/")
        if 'class="site-header' not in html:
            html = re.sub(r"(<body\b[^>]*>)", lambda match: match[1] + standalone_header(lang, page_route), html, count=1)
        html = re.sub(r"</head>", tag + ASSET + "</head>", html, count=1, flags=re.I)
        contact = f'<div id="pa-contact-links" class="pa-contact-links">{contact_links(lang,page_route)}</div>'
        html = re.sub(r"</body>", contact + "</body>", html, count=1, flags=re.I)
        target.write_text(html)
