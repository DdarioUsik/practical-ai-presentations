#!/usr/bin/env python3
"""Build the sales-led Practical AI site as crawlable EN/RU static pages."""
from __future__ import annotations

from html import escape
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = "https://practical-ai.pro"

COPY = {
    "en": {
        "nav": ["For HR & L&D", "Programs", "How we work", "Guides"],
        "discuss": "Discuss training for your team",
        "language": "Русский",
        "hero_eyebrow": "Practical AI · for business teams",
        "hero_h1": "Corporate AI training built around <em>your team’s real work.</em>",
        "hero_lede": "We train business teams to use AI in the work they already do. Bring a recurring task; your team practises an AI-supported step, reviews the result and leaves with a clear next test.",
        "hero_cta": "Discuss AI training for your team",
        "hero_secondary": "Explore the programs",
        "hero_note": "For HR, L&D and functional leaders · guided practice with human review",
        "flow_top": "What your team works through", "flow_status": "Working model",
        "flow_steps": [("Choose a real team task", "Start with a repeatable workflow"), ("Map the AI step", "Inputs, output and quality criteria"), ("Practise and review", "Use agreed tools; a person checks the result"), ("Take a next step", "Keep a workflow card and a plan to test it")],
        "flow_output": "Visible output", "flow_output_text": "a team workflow, review checklist and next test",
        "programs_eyebrow": "Educational programs · second step", "programs_h2": "Choose the right starting pace for your team.",
        "programs_intro": "One day to explore, one week to test a workflow, or four weeks to build regular practice. We shape the work around your team's task and agreed tools.",
        "programs": [
            ("01 · One day", "AI Team Lab", "A practical workshop to explore real tasks and choose one useful AI workflow.", ["Bring representative team tasks", "Try an AI step with human review", "Leave with a task map and next test"], "Discuss a team lab"),
            ("02 · One week · recommended start", "AI Workflow Sprint", "A guided sprint to map and test one repeatable process with your team.", ["Map the process and its owner", "Practise one AI-supported step", "Take away a workflow card and review checklist"], "Discuss a one-week sprint"),
            ("03 · Four weeks", "Team Practice Program", "Supported practice across several roles and work weeks.", ["Work on real tasks between sessions", "Review outputs together", "Create a shared team playbook"], "Discuss a team program"),
        ],
        "proof_eyebrow": "Real team work", "proof_h2": "Training starts with work people recognize.",
        "proof_p": "In one published Practical AI team case, five ShildPanel leaders practised with reports, competitor research, ERP formulas and HR routines. The example shows the kind of tasks a team can bring into training; the scope and results of a new program are agreed separately.",
        "proof_tag": "Team case · 5 participants", "proof_title": "A shared method across different roles.",
        "proof_facts": [("Report and presentation", "60 → 12 min"), ("Market research", "−70%"), ("ERP formulas", "9 h → 15 min"), ("HR routine", "−30 min/day")],
        "proof_note": "Figures reported in the published ShildPanel team case; they describe those tasks, not a typical program outcome.",
        "proof_photo": "Illustrative image of a team reviewing an AI workflow", "proof_visual_note": "Workflow illustration · client results shown separately",
        "quotes_eyebrow": "In their own words", "quotes_h2": "What the team said after putting AI to work.", "quotes_intro": "Selected remarks from the ShildPanel team case. English translations of the original Russian comments.",
        "quotes": [("Practice, practice… Keep building your skills, everyone.", "Alexander", "Operations Director · ShildPanel"), ("What we created is a tool I can now delegate.", "Ilya", "Marketing and Analytics · ShildPanel"), ("Whisper is something I use almost every day. It’s great.", "Elizaveta", "Head of HR · ShildPanel")],
        "method_eyebrow": "How the learning works", "method_h2": "From a team task to a reviewed way of working.",
        "method_intro": "Every program connects a business task, an AI step, human judgment and a practical next action.",
        "method_steps": [("01", "Choose a task", "Name the process owner and the result the team needs."), ("02", "Design a workflow", "Define inputs, approved tools and the expected output."), ("03", "Review the result", "Use clear quality criteria and human judgment."), ("04", "Keep what works", "Document the pattern and choose the next test.")],
        "team_eyebrow": "The team behind the training", "team_h2": "The right expertise for the work in front of you.", "team_p": "Practical AI brings learning design, hands-on AI practice and review together around your team's task. We shape each program with the people who own the work, so participants can try a useful step and judge its output together.", "team_link": "See how we work →", "team_facets": ["Learning design", "Hands-on practice", "Human review"],
        "guides_eyebrow": "Practical guides", "guides_h2": "Answers for the people choosing AI training.",
        "guides": [("Corporate learning", "How to prepare a team for AI training", "Start with roles, workflows and review standards.", "/blog/corporate-ai-training/"), ("Project teams", "AI workflows for project managers", "Meetings, updates, risk reviews and human ownership.", "/blog/ai-for-project-managers/"), ("Finance teams", "AI in finance work", "Reporting, formulas and variance summaries with review.", "/blog/ai-for-finance-teams/")],
        "closing_h2": "Which team task would you like to improve with AI?", "closing_cta": "Discuss a first step",
        "footer_p": "Practical AI · corporate AI training built around real work",
        "hr_eyebrow": "For HR and learning leaders", "hr_h1": "AI training your team can use in its work.",
        "hr_intro": "Choose a program around a real team task, agreed tools, clear review and a defined next step. Practical AI helps HR and L&D turn interest in AI into a focused learning brief.",
        "hr_questions_h2": "What should the first program solve?", "hr_questions_p": "A useful brief starts with the work, not the workshop length.",
        "hr_questions": [("Who is learning?", "Name the team, roles and process owner."), ("What work will they bring?", "Choose a recurring task with a visible output."), ("How will they check it?", "Agree on tools, data boundaries and human review."), ("What happens afterward?", "Define a small test for the next working week.")],
        "hr_next_h2": "A clear first brief makes the training useful.", "hr_next_p": "Tell us the team, one repeatable task and the result you want to see. We can then choose a lab, sprint or longer program together.",
        "program_page_eyebrow": "Corporate AI learning", "program_page_h1": "Practical AI training programs for business teams.",
        "program_page_intro": "Three ways to practise on real work. Start with the team task and choose a duration that gives people enough time to try, review and reuse a useful AI step.",
        "about_eyebrow": "How Practical AI works", "about_h1": "A team approach to practical AI learning.", "about_lead": "We bring learning, business and AI practice together around your team's work. The task defines the format and the mix of expertise involved.",
        "about_method_h2": "One shared method", "about_method_p": "We start with a recurring task and the people responsible for it. Together we map an AI step, practise on a representative example, review the output and document a next test for normal work.",
        "about_background_h2": "A team around the task", "about_background_p": "Program roles follow the team's needs, tools and workflow. Practical AI coordinates the learning design, working sessions and review so each group has a clear path from its first task to a practical next step.",
        "meta_home": ("Corporate AI Training for Business Teams | Practical AI", "Hands-on corporate AI training for business teams. One-day labs, one-week workflow sprints and four-week programs built around real work."),
        "meta_hr": ("AI Training for HR and L&D Teams | Practical AI", "Plan practical AI training for employees around real workflows, agreed tools, human review and a clear next step."),
        "meta_programs": ("Corporate AI Training Programs | Practical AI", "Compare Practical AI's one-day team lab, one-week AI workflow sprint and four-week team practice program."),
        "meta_about": ("How Practical AI Works | Team Approach to AI Training", "Meet the Practical AI team approach to corporate AI training: learning design, real workflows, hands-on practice and human review."),
    },
    "ru": {
        "nav": ["Для HR и L&D", "Программы", "Как мы работаем", "Руководства"],
        "discuss": "Обсудить обучение команды", "language": "English",
        "hero_eyebrow": "Practical AI · для бизнес-команд",
        "hero_h1": "Корпоративное AI-обучение <em>на задачах вашей команды.</em>",
        "hero_lede": "Обучаем команды применять AI в привычной работе. Берём повторяющуюся задачу, отрабатываем AI-шаг, проверяем результат и определяем следующий тест.",
        "hero_cta": "Обсудить обучение команды", "hero_secondary": "Посмотреть программы",
        "hero_note": "Для HR, L&D и руководителей функций · практика с проверкой человеком",
        "flow_top": "Как работает команда", "flow_status": "Рабочая модель",
        "flow_steps": [("Выбираем задачу команды", "Начинаем с повторяющегося процесса"), ("Размечаем AI-шаг", "Входные данные, результат и критерии качества"), ("Практикуемся и проверяем", "Согласованные инструменты и оценка специалиста"), ("Определяем следующий шаг", "Сохраняем сценарий и план его проверки")],
        "flow_output": "Осязаемый результат", "flow_output_text": "сценарий команды, чек-лист проверки и следующий тест",
        "programs_eyebrow": "Образовательные программы · второй экран", "programs_h2": "Выберите подходящий старт для команды.",
        "programs_intro": "Один день для знакомства с задачами, неделя для проверки процесса или четыре недели для регулярной практики. Работаем на задачах команды и согласованных инструментах.",
        "programs": [
            ("01 · Один день", "AI-лаборатория", "Практический воркшоп: разбираем реальные задачи и выбираем один полезный AI-сценарий.", ["Задачи участников", "Пробный AI-шаг с проверкой", "Карта задач и следующий тест"], "Обсудить лабораторию"),
            ("02 · Одна неделя · рекомендуемый старт", "AI-спринт по процессу", "С поддержкой разбираем и проверяем один повторяющийся процесс команды.", ["Карта процесса и ответственный", "Практика одного AI-шага", "Карточка сценария и чек-лист проверки"], "Обсудить недельный спринт"),
            ("03 · Четыре недели", "Программа командной практики", "Практика для нескольких ролей на протяжении рабочих недель.", ["Задачи между занятиями", "Совместная проверка результатов", "Общая база практик команды"], "Обсудить программу"),
        ],
        "proof_eyebrow": "Реальная работа команды", "proof_h2": "Учимся на задачах, которые люди узнают.",
        "proof_p": "В опубликованном кейсе Practical AI пять руководителей «ШильдПанель» работали с отчётами, анализом конкурентов, ERP-формулами и HR-рутиной. Это пример задач для обучения; объём и ожидаемый результат новой программы согласуем отдельно.",
        "proof_tag": "Командный кейс · 5 участников", "proof_title": "Общий подход для разных ролей.",
        "proof_facts": [("Отчёт и презентация", "60 → 12 мин"), ("Анализ рынка", "−70%"), ("Формулы в ERP", "9 ч → 15 мин"), ("HR-рутина", "−30 мин/день")],
        "proof_note": "Данные опубликованного кейса команды «ШильдПанель» относятся к конкретным задачам участников.",
        "proof_photo": "Иллюстрация совместной работы над AI-сценарием", "proof_visual_note": "Иллюстрация процесса · результаты клиента показаны отдельно",
        "quotes_eyebrow": "Слова участников", "quotes_h2": "Что говорила команда после практики с AI.", "quotes_intro": "Фрагменты отзывов участников группового обучения «ШильдПанель».",
        "quotes": [("Практика, практика… Набивайте руку, ребята.", "Александр", "Операционный директор · «ШильдПанель»"), ("Для меня то, что мы создали, инструмент, который я теперь смогу делегировать.", "Илья", "Маркетинг и аналитика · «ШильдПанель»"), ("Whisper — это точно то, что я использую почти ежедневно, это круто.", "Елизавета", "Руководитель HR · «ШильдПанель»")],
        "method_eyebrow": "Как устроена практика", "method_h2": "От задачи команды к проверенному способу работы.",
        "method_intro": "В каждой программе соединяем рабочую задачу, AI-шаг, оценку специалиста и следующий тест.",
        "method_steps": [("01", "Выбираем задачу", "Фиксируем ответственного и нужный результат."), ("02", "Собираем сценарий", "Определяем материалы, инструменты и формат ответа."), ("03", "Проверяем результат", "Используем критерии качества и оценку специалиста."), ("04", "Сохраняем практику", "Документируем сценарий и выбираем следующий тест.")],
        "team_eyebrow": "Команда Practical AI", "team_h2": "Собираем экспертизу под задачу вашей команды.", "team_p": "В Practical AI соединяем разработку программы, практику с AI и проверку результата вокруг работы вашей команды. Вместе с людьми, которые отвечают за процесс, выстраиваем обучение так, чтобы участники попробовали полезный шаг и оценили его результат.", "team_link": "Как мы работаем →", "team_facets": ["Программа обучения", "Практика на задачах", "Проверка результата"],
        "guides_eyebrow": "Практические руководства", "guides_h2": "Ответы для тех, кто выбирает AI-обучение.",
        "guides": [("Обучение команд", "Как подготовить команду к AI-обучению", "Роли, процессы и критерии проверки.", "/ru/blog/corporate-ai-training/"), ("Проектные команды", "AI-сценарии для менеджеров проектов", "Встречи, статусы, риски и ответственность человека.", "/ru/blog/ai-for-project-managers/"), ("Финансовые команды", "AI в работе финансовой команды", "Отчёты, формулы и проверка результата.", "/ru/blog/ai-for-finance-teams/")],
        "closing_h2": "Какую задачу вашей команды стоит улучшить с AI?", "closing_cta": "Обсудить первый шаг",
        "footer_p": "Practical AI · корпоративное AI-обучение на реальных задачах",
        "hr_eyebrow": "Для HR и руководителей обучения", "hr_h1": "AI-обучение, которое команда применяет в работе.",
        "hr_intro": "Выбирайте программу вокруг задачи команды, согласованных инструментов, ясной проверки и следующего шага. Practical AI помогает HR и L&D превратить интерес к AI в конкретный учебный проект.",
        "hr_questions_h2": "Какую задачу решит первая программа?", "hr_questions_p": "Полезный бриф начинается с работы команды, а затем определяет длительность обучения.",
        "hr_questions": [("Кто учится?", "Команда, роли и ответственный за процесс."), ("С чем работают?", "Повторяющаяся задача с видимым результатом."), ("Как проверяют?", "Инструменты, границы данных и оценка специалиста."), ("Что делают после?", "Небольшой тест на следующей рабочей неделе.")],
        "hr_next_h2": "Ясный первый бриф делает обучение полезным.", "hr_next_p": "Расскажите о команде, одной повторяющейся задаче и результате, который хотите увидеть. Вместе выберем лабораторию, спринт или более длительную программу.",
        "program_page_eyebrow": "Корпоративное AI-обучение", "program_page_h1": "Практические AI-программы для бизнес-команд.",
        "program_page_intro": "Три формата практики на реальной работе. Начинаем с задачи команды и выбираем длительность, достаточную для пробы, проверки и повторного применения AI-шага.",
        "about_eyebrow": "Как работает Practical AI", "about_h1": "Командный подход к практическому AI-обучению.", "about_lead": "Объединяем разработку образовательных программ, понимание бизнес-процессов и практику с AI вокруг работы вашей команды. Задача определяет формат и состав специалистов.",
        "about_method_h2": "Общий метод", "about_method_p": "Начинаем с повторяющейся задачи и людей, которые за неё отвечают. Вместе размечаем AI-шаг, практикуемся на понятном примере, проверяем результат и документируем следующий тест для повседневной работы.",
        "about_background_h2": "Команда под задачу", "about_background_p": "Роли в программе зависят от команды, её инструментов и процесса. Practical AI координирует разработку программы, рабочие встречи и проверку результата, чтобы группа прошла понятный путь от первой задачи к следующему практическому шагу.",
        "meta_home": ("Корпоративное AI-обучение для команд | Practical AI", "Практическое AI-обучение для бизнес-команд на реальных задачах: однодневная лаборатория, недельный спринт и четырёхнедельная программа."),
        "meta_hr": ("AI-обучение для HR и L&D | Practical AI", "Как организовать AI-обучение сотрудников на рабочих процессах: задачи, согласованные инструменты, проверка и следующий шаг."),
        "meta_programs": ("Программы корпоративного AI-обучения | Practical AI", "Сравните однодневную AI-лабораторию, недельный спринт и четырёхнедельную программу командной практики."),
        "meta_about": ("Как работает Practical AI | Командное AI-обучение", "Командный подход Practical AI к корпоративному AI-обучению: программа под рабочие задачи, практика и проверка результата."),
    },
}


def u(lang: str, route: str = "") -> str:
    return ("/ru" if lang == "ru" else "") + "/" + (route + "/" if route else "")


def contact(lang: str, topic: str = "team") -> str:
    messages = {
        "en": {"team": "Hello! I’d like to discuss AI training for my team.", "lab": "Hello! I’d like to discuss an AI team lab.", "sprint": "Hello! I’d like to discuss a one-week AI workflow sprint.", "program": "Hello! I’d like to discuss a four-week team practice program."},
        "ru": {"team": "Здравствуйте! Хочу обсудить AI-обучение для моей команды.", "lab": "Здравствуйте! Хочу обсудить AI-лабораторию для команды.", "sprint": "Здравствуйте! Хочу обсудить недельный AI-спринт по процессу.", "program": "Здравствуйте! Хочу обсудить четырёхнедельную программу практики для команды."},
    }
    return "https://t.me/Danil_alto?text=" + quote(messages[lang][topic])


def esc(value: str) -> str:
    return escape(value, quote=True)


def schema(lang: str, route: str) -> dict:
    org = {"@type": "Organization", "@id": BASE + "/#organization", "name": "Practical AI", "url": BASE + "/", "logo": BASE + "/assets/brand/logo-primary.svg"}
    webpage = {"@type": "WebPage", "@id": BASE + u(lang, route) + "#webpage", "url": BASE + u(lang, route), "inLanguage": lang, "isPartOf": {"@id": BASE + "/#website"}}
    graph = [org, {"@type": "WebSite", "@id": BASE + "/#website", "name": "Practical AI", "url": BASE + "/", "publisher": {"@id": BASE + "/#organization"}}, webpage]
    if route != "about":
        graph.append({"@type": "Service", "name": "Corporate AI training" if lang == "en" else "Корпоративное AI-обучение", "serviceType": "Corporate AI training", "provider": {"@id": BASE + "/#organization"}, "url": BASE + u(lang, route)})
    return {"@context": "https://schema.org", "@graph": graph}


def shell(lang: str, route: str, body: str) -> str:
    c = COPY[lang]
    key = "home" if not route else route.replace("for-hr", "hr")
    title, description = c["meta_" + key]
    title, description = esc(title), esc(description)
    canonical = BASE + u(lang, route)
    other = "ru" if lang == "en" else "en"
    nav_routes = ["for-hr", "programs", "about", "blog"]
    nav = "".join(f'<a href="{u(lang, route_name)}"' + (' aria-current="page"' if route == route_name else '') + f'>{esc(label)}</a>' for route_name, label in zip(nav_routes, c["nav"]))
    lang_label = "Переключить язык на русский" if lang == "en" else "Switch language to English"
    home_label = "Practical AI home" if lang == "en" else "Practical AI — на главную"
    site_name = "Practical AI"
    return f'''<!doctype html>
<html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#17213d"><meta name="robots" content="index,follow,max-image-preview:large">
<title>{title}</title><meta name="description" content="{description}">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{BASE + u('en',route)}"><link rel="alternate" hreflang="ru" href="{BASE + u('ru',route)}"><link rel="alternate" hreflang="x-default" href="{BASE + u('en',route)}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{site_name}"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="{'en_US' if lang == 'en' else 'ru_RU'}"><meta property="og:image" content="{BASE}/assets/brand/social-card.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{description}"><meta name="twitter:image" content="{BASE}/assets/brand/social-card.png">
<link rel="icon" type="image/svg+xml" href="/assets/brand/symbol-primary.svg"><link rel="stylesheet" href="/assets/brand/sales-site.css">
<script type="application/ld+json">{json.dumps(schema(lang,route),ensure_ascii=False,separators=(',',':'))}</script>
</head><body>
<header class="site-header"><div class="wrap nav"><a href="{u(lang)}" aria-label="{home_label}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a><nav class="nav-links" aria-label="{'Main navigation' if lang == 'en' else 'Основная навигация'}">{nav}</nav><div class="nav-end"><a class="lang-switch" href="{u(other,route)}" lang="{other}" aria-label="{lang_label}">{esc(c['language'])}</a><a class="button button--small" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c['discuss'])} ↗</a></div></div></header>
<main>{body}</main>
<footer class="site-footer"><div class="wrap footer-inner"><a href="{u(lang)}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a><p>{esc(c['footer_p'])}</p><nav class="footer-links" aria-label="Footer">{nav}</nav></div></footer>
</body></html>'''


def program_cards(lang: str) -> str:
    c = COPY[lang]
    topics = ["lab", "sprint", "program"]
    return '<div class="program-grid">' + "".join(
        f'<article class="program-card' + (' program-card--lead' if i == 1 else '') + f'" id="{topics[i]}"><span class="program-tag">{esc(tag)}</span><h3>{esc(name)}</h3><p>{esc(description)}</p><ul>' + "".join(f'<li>{esc(item)}</li>' for item in bullets) + f'</ul><a class="card-link" href="{contact(lang,topics[i])}" target="_blank" rel="noopener noreferrer">{esc(cta)} ↗</a></article>'
        for i, (tag, name, description, bullets, cta) in enumerate(c["programs"])
    ) + '</div>'


def closing(lang: str) -> str:
    c = COPY[lang]
    return f'<section class="closing"><div class="wrap closing-inner"><h2>{esc(c["closing_h2"])}</h2><a class="button button--dark" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c["closing_cta"])} ↗</a></div></section>'


def evidence_teaser(lang: str) -> str:
    c = COPY[lang]
    label = "Explore the team case and participant quotes" if lang == "en" else "Посмотреть результаты кейса и слова участников"
    quote_text, quote_name, quote_role = c["quotes"][0]
    return f'<section class="section evidence-teaser"><div class="wrap evidence-teaser-grid"><div><span class="eyebrow">{esc(c["proof_tag"])}</span><h2>{esc(c["proof_h2"])}</h2><p>{esc(c["proof_p"])}</p><a class="card-link" href="{u(lang)}#case">{esc(label)} →</a></div><figure><blockquote>“{esc(quote_text)}”</blockquote><figcaption>{esc(quote_name)} · {esc(quote_role)}</figcaption></figure></div></section>'


def home(lang: str) -> str:
    c = COPY[lang]
    steps = "".join(f'<div class="flow-step"><span class="num">{i:02}</span><div><b>{esc(title)}</b><small>{esc(detail)}</small></div></div>' for i, (title, detail) in enumerate(c["flow_steps"], 1))
    method = "".join(f'<article class="method-card"><span class="step">{number}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p></article>' for number, title, detail in c["method_steps"])
    guides = "".join(f'<a class="guide-card" href="{url}"><span>{esc(tag)}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p><b>{"Read guide" if lang == "en" else "Читать руководство"} ↗</b></a>' for tag, title, detail, url in c["guides"])
    proof_facts = "".join(f'<div class="proof-metric"><b>{esc(value)}</b><span>{esc(label)}</span></div>' for label, value in c["proof_facts"])
    quotes = "".join(f'<figure class="quote-card"><blockquote>“{esc(words)}”</blockquote><figcaption><b>{esc(name)}</b><span>{esc(role)}</span></figcaption></figure>' for words, name, role in c["quotes"])
    facets = "".join(f'<li><span>0{i}</span>{esc(facet)}</li>' for i, facet in enumerate(c["team_facets"], 1))
    return f'''<section class="hero"><div class="wrap hero-grid"><div><span class="eyebrow">{esc(c['hero_eyebrow'])}</span><h1>{c['hero_h1']}</h1><p class="hero-lede">{esc(c['hero_lede'])}</p><div class="hero-actions"><a class="button" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c['hero_cta'])} ↗</a><a class="button button--ghost" href="#programs">{esc(c['hero_secondary'])} ↓</a></div><p class="hero-note">{esc(c['hero_note'])}</p></div><div class="flow-card"><div class="flow-top"><span>{esc(c['flow_top'])}</span><span>● {esc(c['flow_status'])}</span></div>{steps}<div class="flow-output"><b>{esc(c['flow_output'])}</b> · {esc(c['flow_output_text'])}</div></div></div></section>
<section class="section programs" id="programs"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['programs_eyebrow'])}</span><h2>{esc(c['programs_h2'])}</h2></div><p>{esc(c['programs_intro'])}</p></div>{program_cards(lang)}</div></section>
<section class="section proof" id="case"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['proof_eyebrow'])}</span><h2>{esc(c['proof_h2'])}</h2></div><p>{esc(c['proof_p'])}</p></div><div class="case-layout"><figure class="case-image"><img src="/assets/corporate/cross-functional-workflow-review.jpg" alt="{esc(c['proof_photo'])}" width="1448" height="1086" loading="lazy"><figcaption>{esc(c['proof_visual_note'])}</figcaption></figure><div class="proof-panel"><div class="case-panel-head"><img src="/assets/img/shildpanel-logo.svg" alt="ШильдПанель" loading="lazy"><span class="case-tag">{esc(c['proof_tag'])}</span></div><h3>{esc(c['proof_title'])}</h3><div class="proof-facts">{proof_facts}</div><p class="proof-note">{esc(c['proof_note'])}</p></div></div></div></section>
<section class="section quotes" id="reviews"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['quotes_eyebrow'])}</span><h2>{esc(c['quotes_h2'])}</h2></div><p>{esc(c['quotes_intro'])}</p></div><div class="quote-grid">{quotes}</div></div></section>
<section class="section method"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['method_eyebrow'])}</span><h2>{esc(c['method_h2'])}</h2></div><p>{esc(c['method_intro'])}</p></div><div class="method-grid">{method}</div></div></section>
<section class="section team-section"><div class="wrap team-grid"><div class="team-panel"><img src="/assets/brand/symbol-reverse.svg" alt="" width="128" height="128" loading="lazy"><ol>{facets}</ol></div><div><span class="eyebrow">{esc(c['team_eyebrow'])}</span><h2>{esc(c['team_h2'])}</h2><p>{esc(c['team_p'])}</p><a class="card-link" href="{u(lang,'about')}">{esc(c['team_link'])}</a></div></div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['guides_eyebrow'])}</span><h2>{esc(c['guides_h2'])}</h2></div></div><div class="guide-grid">{guides}</div></div></section>{closing(lang)}'''


def page_hero(lang: str, eyebrow: str, h1: str, intro: str) -> str:
    return f'<section class="page-hero"><div class="wrap"><span class="eyebrow">{esc(eyebrow)}</span><h1>{esc(h1)}</h1><p>{esc(intro)}</p><a class="button" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(COPY[lang]["discuss"])} ↗</a></div></section>'


def hr(lang: str) -> str:
    c = COPY[lang]
    questions = "".join(f'<div class="question"><b>{esc(title)}</b><span>{esc(detail)}</span></div>' for title, detail in c["hr_questions"])
    return page_hero(lang,c["hr_eyebrow"],c["hr_h1"],c["hr_intro"]) + f'<section class="section"><div class="wrap content-grid"><div><span class="eyebrow">{esc(c["hr_eyebrow"])}</span><h2>{esc(c["hr_questions_h2"])}</h2><p>{esc(c["hr_questions_p"])}</p></div><div class="question-list">{questions}</div></div></section><section class="section programs"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["programs_eyebrow"])}</span><h2>{esc(c["programs_h2"])}</h2></div></div>{program_cards(lang)}</div></section>{evidence_teaser(lang)}<section class="section proof"><div class="wrap content-grid"><h2>{esc(c["hr_next_h2"])}</h2><div><p>{esc(c["hr_next_p"])}</p><a class="button button--dark" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c["closing_cta"])} ↗</a></div></div></section>{closing(lang)}'


def programs(lang: str) -> str:
    c = COPY[lang]
    method = "".join(f'<article class="method-card"><span class="step">{number}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p></article>' for number, title, detail in c["method_steps"])
    return page_hero(lang,c["program_page_eyebrow"],c["program_page_h1"],c["program_page_intro"]) + f'<section class="section programs"><div class="wrap">{program_cards(lang)}</div></section><section class="section method"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["method_eyebrow"])}</span><h2>{esc(c["method_h2"])}</h2></div><p>{esc(c["method_intro"])}</p></div><div class="method-grid">{method}</div></div></section>{evidence_teaser(lang)}{closing(lang)}'


def about(lang: str) -> str:
    c = COPY[lang]
    method = "".join(f'<article class="method-card"><span class="step">{number}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p></article>' for number, title, detail in c["method_steps"])
    return f'<section class="section editorial"><div class="wrap"><span class="eyebrow">{esc(c["about_eyebrow"])}</span><h1>{esc(c["about_h1"])}</h1><p class="lead">{esc(c["about_lead"])}</p><div class="content-grid"><div><h2>{esc(c["about_method_h2"])}</h2><p>{esc(c["about_method_p"])}</p></div><div><h2>{esc(c["about_background_h2"])}</h2><p>{esc(c["about_background_p"])}</p></div></div></div></section><section class="section method"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["method_eyebrow"])}</span><h2>{esc(c["method_h2"])}</h2></div><p>{esc(c["method_intro"])}</p></div><div class="method-grid">{method}</div></div></section>{evidence_teaser(lang)}<section class="section programs"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["programs_eyebrow"])}</span><h2>{esc(c["programs_h2"])}</h2></div></div>{program_cards(lang)}</div></section>{closing(lang)}'


def main() -> None:
    page_makers = {"": home, "for-hr": hr, "programs": programs, "about": about}
    for lang in ("en", "ru"):
        for route, maker in page_makers.items():
            target = DOCS / ("ru" if lang == "ru" else "") / route / "index.html"
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(shell(lang,route,maker(lang)) + "\n", encoding="utf-8")
    sitemap = DOCS / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    for lang in ("en", "ru"):
        for route in page_makers:
            url = BASE + u(lang,route)
            if f"<loc>{url}</loc>" not in text:
                text = text.replace("</urlset>", f"  <url><loc>{url}</loc></url>\n</urlset>")
    sitemap.write_text(text, encoding="utf-8")
    blog_pages = [DOCS / "blog/index.html", *sorted((DOCS / "blog").glob("*/index.html")), DOCS / "ru/blog/index.html", *sorted((DOCS / "ru/blog").glob("*/index.html"))]
    for path in blog_pages:
        if path.parent.name == "ai-my-voice":
            continue
        html = path.read_text(encoding="utf-8")
        header, marker, rest = html.partition("</header>")
        if marker:
            updated = header.replace("logo-primary.svg", "logo-reverse.svg", 1) + marker + rest
            if updated != html:
                path.write_text(updated, encoding="utf-8")
    print("Built eight sales-led static pages and updated sitemap")


if __name__ == "__main__":
    main()
