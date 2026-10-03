#!/usr/bin/env python3
"""Build bilingual corporate pages from the approved homepage and brand masters."""
from __future__ import annotations

import ast
from html import escape, unescape
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
SOURCE = (ROOT / "site-source/home.en.html").read_text(encoding="utf-8")
RU_TITLE = "Practical AI — AI-обучение для бизнес-команд"
RU_DESCRIPTION = "Практическое AI-обучение для команд на задачах компании: рабочие сценарии, проверка результата и понятный следующий шаг."
EN_TITLE = "Practical AI — practical AI training for business teams"
EN_DESCRIPTION = "Hands-on AI training for business teams, built around company workflows, shared practice and human review."
BASE = "https://practical-ai.pro/"


def replace_once(text: str, old: str, new: str) -> str:
    if text.count(old) != 1:
        raise ValueError(f"Expected exactly one match: {old[:72]!r}; found {text.count(old)}")
    return text.replace(old, new)


def remove_translation_script(text: str) -> str:
    pattern = re.compile(r'<script>\s*const russianCopy = .*?</script>', re.S)
    text, count = pattern.subn("", text)
    if count != 1:
        raise ValueError(f"Expected one translation script, found {count}")
    return text


def translation_data() -> tuple[dict[str, str], dict[str, str]]:
    copy_match = re.search(r'const russianCopy = (\{.*?\});', SOURCE, re.S)
    aria_match = re.search(r'const russianAriaCopy = (\{.*?\});', SOURCE, re.S)
    if not copy_match or not aria_match:
        raise ValueError("Homepage translation maps were not found")
    copy = json.loads(copy_match.group(1))
    aria = ast.literal_eval(aria_match.group(1))
    copy = {unescape(k): v for k, v in copy.items()}
    copy.update({
        "Reviews": "Отзывы",
        "AI capability for the whole company": "AI-практика для всей компании",
        "Turn AI access into": "Превратите доступ к AI в",
        "team capability.": "навык команды.",
        "Role-based learning": "Обучение по ролям",
        "Shared practices": "Общие практики",
        "Next-step roadmap": "План следующего шага",
        "What participants say": "Что говорят участники",
        "People remember the moment AI helped with real work.": "Участники запоминают момент, когда AI помог с настоящей задачей.",
        "Feedback from business team programmes and individual practice with Practical AI.": "Отзывы о командных программах и индивидуальной практике Practical AI.",
        "Operations Director": "Операционный директор",
        "Marketing Director": "Директор по маркетингу",
        "Production lead": "Руководитель производства",
        "Commercial director": "Коммерческий директор",
        "Development lead": "Руководитель отдела развития",
        "Product & Project": "Продукт и проекты",
        "Everyday work": "Повседневная работа",
        "From individual tasks to shared workflows.": "От личных задач к общим рабочим процессам.",
        "Practice starts with a familiar task, then grows into a repeatable way of working together.": "Практика начинается со знакомой задачи, затем становится повторяемым способом совместной работы.",
        "One task from a team member’s role": "Одна задача из роли участника",
        "Focused practice with familiar work": "Прицельная практика на знакомой работе",
        "One workflow, shared across the team": "Один процесс для всей команды",
        "Build shared practices across the team": "Формируем общие практики команды",
        "03 / PRACTICE": "03 / ПРАКТИКА",
        "04 / CONTINUE": "04 / ПРОДОЛЖЕНИЕ",
        "One everyday task": "Одна повседневная задача",
        "What your team takes away": "Что остаётся у команды",
        "One tested workflow step": "Один проверенный шаг процесса",
        "A workflow card, review checklist and team workflow diagram showing where AI helps, who checks the result and what to test next.": "Карта сценария, чек-лист проверки и схема процесса: где помогает AI, кто проверяет результат и что тестировать дальше.",
        "One-Week AI Workflow Sprint": "Недельный AI-спринт по рабочему процессу",
        "One workflow, tested and mapped": "Один описанный и проверенный процесс",
        "A process map, tested AI step, quality checklist, named process owner and a clear next-step decision.": "Карта процесса, проверенный AI-шаг, чек-лист качества, ответственный и решение о следующем этапе.",
        "Several functions": "Несколько функций",
        "A shared team playbook": "Общая база практик команды",
        "Role-based workflow cards, a shared review standard and a prioritized list for the next pilot.": "Карточки процессов по ролям, общий стандарт проверки и список задач для следующего пилота.",
        "Community partner · Tech Connect VLC": "Партнёр сообщества · Tech Connect VLC",
        "Practical AI collaborates with Tech Connect VLC on local meetups focused on practical AI use cases.": "Practical AI проводит вместе с Tech Connect VLC встречи о практическом применении AI.",
        "One-Week AI Workflow Sprint · Program": "Недельный AI-спринт · Программа",
        "How do we choose between the one-week sprint and four-week program?": "Как выбрать между недельным спринтом и четырёхнедельной программой?",
        "Choose the sprint to test one workflow with a focused team. Choose the four-week program to build AI practice across several roles with guided follow-up.": "Недельный спринт подходит для проверки одного процесса с небольшой командой. Четырёхнедельная программа помогает выстроить практику в нескольких ролях с сопровождением.",
    })
    return copy, aria


def translate_visible_html(text: str) -> str:
    copy, aria = translation_data()
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        protected.append(match.group(0))
        return f"@@PROTECTED_{len(protected) - 1}@@"

    text = re.sub(r'<(?:script|style)\b[^>]*>.*?</(?:script|style)>', protect, text, flags=re.S | re.I)
    parts = re.split(r'(<[^>]+>)', text)
    hit = 0
    for i, part in enumerate(parts):
        if not part or part.startswith("<") or part.startswith("@@PROTECTED_"):
            continue
        value = unescape(part.strip())
        if value in copy:
            leading = part[:len(part) - len(part.lstrip())]
            trailing = part[len(part.rstrip()):]
            parts[i] = leading + escape(copy[value], quote=False) + trailing
            hit += 1
    if hit < 100:
        raise ValueError(f"Too few translated visible strings: {hit}")
    text = "".join(parts)

    def translate_attr(match: re.Match[str]) -> str:
        name, raw = match.group(1), match.group(2)
        value = aria.get(unescape(raw), unescape(raw))
        return f'{name}="{escape(value, quote=True)}"'

    text = re.sub(r'\b(aria-label|alt|title)="([^"]*)"', translate_attr, text)
    for i, chunk in enumerate(protected):
        text = text.replace(f"@@PROTECTED_{i}@@", chunk)
    return text


def metadata(text: str, language: str) -> str:
    is_ru = language == "ru"
    page_url = BASE + ("ru/" if is_ru else "")
    title = RU_TITLE if is_ru else EN_TITLE
    description = RU_DESCRIPTION if is_ru else EN_DESCRIPTION
    text = replace_once(text, '<html lang="en">', f'<html lang="{language}">') if is_ru else text
    text = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', text, count=1)
    text = re.sub(r'(<meta name="description" content=")[^"]*', lambda m: m.group(1) + description, text, count=1)
    for property_name, value in [
        ("og:title", title), ("og:description", description),
        ("og:locale", "ru_RU" if is_ru else "en_US"), ("og:url", page_url),
        ("twitter:title", title), ("twitter:description", description),
    ]:
        text = re.sub(rf'(<meta property="{property_name}" content=")[^"]*', lambda m, v=value: m.group(1) + v, text, count=1) if property_name.startswith("og:") else re.sub(rf'(<meta name="{property_name}" content=")[^"]*', lambda m, v=value: m.group(1) + v, text, count=1)
    text = re.sub(r'(<link rel="canonical" href=")[^"]*', lambda m: m.group(1) + page_url, text, count=1)
    text = text.replace('https://practical-ai.pro/assets/corporate/hero-team-workflow.jpg"', 'https://practical-ai.pro/assets/brand/social-card.png"')
    text = re.sub(r'(<meta property="og:locale:alternate" content=")[^"]*', lambda m: m.group(1) + ('en_US' if is_ru else 'ru_RU'), text, count=1)
    text = replace_once(text, 'hreflang="ru" href="https://practical-ai.pro/?lang=ru"', 'hreflang="ru" href="https://practical-ai.pro/ru/"')
    text = replace_once(text, '<meta name="theme-color" content="#17213d">', '<meta name="theme-color" content="#17213d">\n  <meta name="robots" content="index,follow,max-image-preview:large">')
    return text


def home(language: str) -> str:
    is_ru = language == "ru"
    text = remove_translation_script(SOURCE)
    if is_ru:
        text = translate_visible_html(text)
    text = metadata(text, language)
    prefix = "../" if is_ru else ""
    text = replace_once(text, "  </style>\n</head>", f'  </style>\n  <link rel="stylesheet" href="{prefix}assets/brand/brand.css">\n  <link rel="icon" type="image/svg+xml" href="{prefix}assets/brand/symbol-primary.svg">\n</head>')
    if is_ru:
        text = text.replace('src="assets/', 'src="../assets/')
        text = text.replace('data-src="assets/', 'data-src="../assets/')
    text = text.replace('<span class="logo-pill">Practical AI</span>', f'<img class="brand-lockup" src="{prefix}assets/brand/logo-primary.svg" alt="Practical AI" width="760" height="152">', 1)
    text = replace_once(text, '<strong><span class="logo-pill">Practical AI</span></strong>', f'<strong><img class="brand-lockup" src="{prefix}assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></strong>')
    text = text.replace('<span class="logo-pill">Practical AI</span>', f'<img class="brand-lockup" src="{prefix}assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152">', 1)
    toggle = '<button class="language-toggle" type="button" data-language-toggle aria-label="Switch language to Russian" aria-pressed="false">RU</button>'
    if is_ru:
        toggle = re.search(r'<button class="language-toggle"[^>]*>RU</button>', text).group(0)
    link = '<a class="language-toggle" href="../" lang="en" aria-label="Switch language to English">EN</a>' if is_ru else '<a class="language-toggle" href="ru/" lang="ru" aria-label="Switch language to Russian">RU</a>'
    text = replace_once(text, toggle, link)
    messages = {
        "en": {"team": "Hello! I’d like to discuss an AI workflow for my team.", "sprint": "Hello! I’d like to discuss the one-week AI Workflow Sprint for my team.", "teamlab": "Hello! I’d like to discuss the four-week Team Practice Program for my company."},
        "ru": {"team": "Привет! Хочу обсудить AI-сценарий для моей команды.", "sprint": "Привет! Хочу обсудить недельный AI Workflow Sprint для команды.", "teamlab": "Привет! Хочу обсудить четырёхнедельную программу командной AI-практики."},
    }
    text = re.sub(r'(<a\b[^>]*data-tg="(team|sprint|teamlab)"[^>]*href=")[^"]*', lambda m: m.group(1) + 'https://t.me/Danil_alto?text=' + quote(messages[language][m.group(2)]), text)
    if is_ru:
        text = re.sub(r'(data-article="([^"]+)" href=")blog/[^" ]+', lambda m: m.group(1) + 'blog/' + m.group(2) + '/', text)
        text = text.replace('data-blog-index href="blog/"', 'data-blog-index href="blog/"')
    person = '<section class="founder-strip"><div class="wrap founder-strip-inner"><span class="founder-label">' + ('Основатель и ведущий' if is_ru else 'Founder and lead') + '</span><p>' + ('Данил Усик развивает Practical AI и ведёт практическое обучение команд.' if is_ru else 'Danil Usik leads Practical AI and works with teams on applied AI learning.') + '</p><a href="https://t.me/Danil_alto" target="_blank" rel="noreferrer">' + ('Связаться с Данилом ↗' if is_ru else 'Contact Danil ↗') + '</a></div></section>'
    text = replace_once(text, '  </main>', f'    {person}\n  </main>')
    schema = {"@context": "https://schema.org", "@type": "Organization", "name": "Practical AI", "url": BASE, "logo": BASE + "assets/brand/logo-primary.svg", "founder": {"@type": "Person", "name": "Danil Usik"}}
    text = replace_once(text, '</head>', '<script type="application/ld+json">' + json.dumps(schema, ensure_ascii=False) + '</script>\n</head>')
    return text


def blog_pages() -> None:
    pages = [DOCS / "blog/index.html", *sorted((DOCS / "blog").glob("*/index.html")), DOCS / "ru/blog/index.html", *sorted((DOCS / "ru/blog").glob("*/index.html"))]
    for path in pages:
        if path.parent.name == "ai-my-voice":
            continue
        text = path.read_text(encoding="utf-8")
        depth = len(path.relative_to(DOCS).parts) - 1
        prefix = "../" * depth
        if "assets/brand/brand.css" not in text:
            text = re.sub(r'(<link rel="stylesheet" href="[^"]*assets/blog.css">)', rf'\1<link rel="stylesheet" href="{prefix}assets/brand/brand.css"><link rel="icon" type="image/svg+xml" href="{prefix}assets/brand/symbol-primary.svg">', text, count=1)
        if 'property="og:image"' not in text:
            text = text.replace('</head>', '<meta property="og:image" content="https://practical-ai.pro/assets/brand/social-card.png">\n</head>', 1)
        text = re.sub(r'<a class="logo-pill"([^>]*)>Practical AI</a>', lambda m: f'<a class="brand-link"{m.group(1)}><img class="brand-lockup" src="{prefix}assets/brand/' + ('logo-reverse.svg' if 'site-footer' in text[max(0, m.start()-100):m.start()] else 'logo-primary.svg') + '" alt="Practical AI" width="760" height="152"></a>', text)
        if "/ru/blog/" in str(path):
            text = re.sub(r'href="(?:\.\./)+\?lang=ru', lambda m: 'href="' + '../' * (m.group(0).count('../') - 1), text)
        path.write_text(text, encoding="utf-8")


def sitemap() -> None:
    path = DOCS / "sitemap.xml"
    text = path.read_text(encoding="utf-8")
    if f"<loc>{BASE}ru/</loc>" not in text:
        text = replace_once(text, "</urlset>", f"  <url>\n    <loc>{BASE}ru/</loc>\n  </url>\n</urlset>")
        path.write_text(text, encoding="utf-8")


def main() -> None:
    (DOCS / "index.html").write_text(home("en"), encoding="utf-8")
    (DOCS / "ru/index.html").write_text(home("ru"), encoding="utf-8")
    blog_pages()
    sitemap()
    print("Built EN/RU homepages, corporate blog branding and sitemap")


if __name__ == "__main__":
    main()
