#!/usr/bin/env python3
"""Build the sales-led Practical AI site as crawlable EN/RU static pages."""
from __future__ import annotations

from html import escape
import hashlib
import json
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
BASE = "https://practical-ai.pro"
PROGRAM_IMAGES = ["program-team-lab.jpg", "program-workflow-sprint.jpg", "program-team-practice.jpg"]
WHATSAPP_NUMBER = "34627184000"
TEAM_PROFILES = [
    {"name": "Danil Usik", "ru_name": "Данил Усик", "photo": "danil-usik.jpg", "linkedin": "https://www.linkedin.com/in/danielusik/"},
    {"name": "Svetlana Galakhova", "ru_name": "Светлана Галахова", "photo": "svetlana-galakhova.jpg", "linkedin": "https://www.linkedin.com/in/svetlana-galakhova/"},
    {"name": "Julia Krylova", "ru_name": "Юлия Крылова", "photo": "julia-krylova.jpg", "linkedin": "https://www.linkedin.com/in/juliakrl/"},
]

COPY = {
    "en": {
        "nav": ["For HR & L&D", "Programs", "Our team", "Guides"],
        "discuss": "Talk to Danil",
        "language": "RU",
        "hero_eyebrow": "Practical AI · for business teams",
        "hero_h1": "Corporate AI training built around <em>your team’s real work.</em>",
        "hero_lede": "Bring the reports, research or management tasks your team handles every week. We help participants build an AI workflow, check its output and document a playbook for the next working day.",
        "hero_cta": "Talk to Danil on WhatsApp",
        "hero_secondary": "Explore the programs",
        "hero_note": "Start with your team size and one task you want to improve.",
        "hero_team": "Meet your core team",
        "telegram_alt": "Or message on Telegram",
        "flow_top": "What your team works through", "flow_status": "Working model",
        "flow_steps": [("Choose a real team task", "Start with a repeatable workflow"), ("Map the AI step", "Inputs, output and quality criteria"), ("Practise and review", "Use agreed tools; a person checks the result"), ("Take a next step", "Keep a workflow card and a plan to test it")],
        "flow_output": "Visible output", "flow_output_text": "a team workflow, review checklist and next test",
        "programs_eyebrow": "Program formats", "programs_h2": "Choose the right starting pace for your team.",
        "programs_intro": "A company-wide day for up to 150 people, a focused week for a small leadership group, or four weeks of practice for around 15 middle managers.",
        "program_image_alts": ["Large company AI learning session in an auditorium", "Small leadership group reviewing a management workflow", "Middle managers working together in an AI practice workshop"],
        "program_audiences": ["Company-wide teams", "CEO & leadership team", "Middle managers"],
        "program_sizes": ["Up to 150 people", "Small group", "Around 15 people"],
        "programs": [
            ("01 · One day", "Company AI Lab", "A company-wide introduction to practical AI through tasks from different teams.", ["Examples from several functions", "Guided practice on familiar tasks", "A shortlist of use cases to take forward"], "Discuss a company lab"),
            ("02 · One week", "AI Leadership Sprint", "A focused sprint for the CEO and leadership team around one management workflow.", ["Choose a leadership priority", "Test one AI-supported process", "Leave with a pilot plan and review criteria"], "Discuss a leadership sprint"),
            ("03 · Four weeks", "Middle Management Program", "Applied AI practice for managers across functions and working weeks.", ["Work on recurring tasks between sessions", "Review results across teams", "Build a shared management playbook"], "Discuss the manager program"),
        ],
        "proof_eyebrow": "Published team case", "proof_h2": "What changed in one team’s daily work.",
        "proof_p": "Five ShildPanel leaders applied AI to four different work tasks. Each figure below describes a reported change in task time in that case.",
        "proof_tag": "ShildPanel · 5 participants", "proof_title": "Four tasks. Four specific results.",
        "proof_before": "Before", "proof_after": "With AI", "proof_result": "Reported result",
        "proof_results": [
            {"task": "Reports and presentations", "detail": "Time to prepare a report and presentation", "before": "60 min", "after": "12 min", "note": "Preparation time fell from one hour to twelve minutes."},
            {"task": "Market and competitor research", "detail": "Time spent researching markets and competitors", "value": "70% less time", "note": "The case reports a 70% reduction in research time."},
            {"task": "ERP formula debugging", "detail": "Time to debug formulas in the ERP system", "before": "9 hours", "after": "15 min", "note": "One formula task took fifteen minutes instead of nine hours."},
            {"task": "HR routine with voice input", "detail": "Time spent on a daily HR routine", "value": "30 min saved / day", "note": "Voice input freed about thirty minutes each day."},
        ],
        "proof_note": "Source: published Practical AI case with ShildPanel. These are results for the tasks above, not an average or a promise for a new team.",
        "proof_roles": "Operations · Business development · Marketing · HR · Management", "proof_case_h3": "Five leaders. Different daily work.", "proof_case_link": "Read what participants said", "proof_count_unit": "participants",
        "quotes_eyebrow": "In their own words", "quotes_h2": "What the team said after putting AI to work.", "quotes_intro": "Selected remarks from the ShildPanel team case. English translations of the original Russian comments.",
        "quotes": [("Now I have a playbook I can hand to my team to put into practice.", "Alexander", "Operations Director"), ("What we created is a tool I can now delegate.", "Ilya", "Marketing and Analytics"), ("Whisper is something I use almost every day. It’s great.", "Elizaveta", "Head of HR")],
        "method_eyebrow": "How the learning works", "method_h2": "From a team task to a reviewed way of working.",
        "method_intro": "Every program connects a business task, an AI step, human judgment and a practical next action.",
        "method_visual_alt": "Example weekly team update: meeting notes, action items and CRM status become an AI draft; a manager checks figures, context and owners before sharing it.",
        "method_steps": [("01", "Choose a task", "Name the process owner and the result the team needs."), ("02", "Design a workflow", "Define inputs, approved tools and the expected output."), ("03", "Review the result", "Use clear quality criteria and human judgment."), ("04", "Keep what works", "Document the pattern and choose the next test.")],
        "team_eyebrow": "The core team", "team_h2": "Meet your Practical AI team.",
        "team_p": "Danil is your first contact. Our core team brings business training, AI implementation and commercial experience into the work with your people.",
        "team_link": "Discuss your team’s needs with Danil",
        "team_roles": ["Founder · Business training", "AI strategy · Hands-on practice", "Marketing · Business development"],
        "team_bios": ["10+ years in B2B sales and business development, with experience in team facilitation. Connects your business priorities with practical AI learning.", "AIHUB.WORKS co-founder and AI implementation practitioner. Turns complex AI concepts into clear workflows and leads hands-on practice.", "Experience across fintech, blockchain and e-commerce, including marketing, fundraising and investor communication. Brings a commercial perspective to the team."],
        "guides_eyebrow": "Practical guides", "guides_h2": "Answers for the people choosing AI training.",
        "guides": [("Corporate learning", "How to prepare a team for AI training", "Start with roles, workflows and review standards.", "/blog/corporate-ai-training/"), ("Project teams", "AI workflows for project managers", "Meetings, updates, risk reviews and human ownership.", "/blog/ai-for-project-managers/"), ("Finance teams", "AI in finance work", "Reporting, formulas and variance summaries with review.", "/blog/ai-for-finance-teams/")],
        "closing_eyebrow": "Start with a conversation",
        "closing_h2": "Let’s find the right AI starting point for your team.",
        "closing_p": "Share your team size, a recurring task and the timing you have in mind. We’ll discuss your priorities and tools, then choose a training format together.",
        "closing_cta": "Message Danil on WhatsApp",
        "contact_role": "Founder · your first contact",
        "footer_p": "Practical AI · corporate AI training built around real work",
        "hr_eyebrow": "For HR and learning leaders", "hr_h1": "AI training your team can use in its work.",
        "hr_intro": "Choose a program around a real team task, agreed tools, clear review and a defined next step. Practical AI helps HR and L&D turn interest in AI into a focused learning brief.",
        "hr_questions_h2": "What should the first program solve?", "hr_questions_p": "A useful brief starts with the work, not the workshop length.",
        "hr_questions": [("Who is learning?", "Name the team, roles and process owner."), ("What work will they bring?", "Choose a recurring task with a visible output."), ("How will they check it?", "Agree on tools, data boundaries and human review."), ("What happens afterward?", "Define a small test for the next working week.")],
        "hr_next_h2": "A clear first brief makes the training useful.", "hr_next_p": "Tell us the team, one repeatable task and the result you want to see. We can then choose a lab, sprint or longer program together.",
        "program_page_eyebrow": "Corporate AI learning", "program_page_h1": "Practical AI training programs for business teams.",
        "program_page_intro": "Choose a company-wide lab, a small leadership sprint or four weeks of practice for middle managers. Each format starts with real work and a clear next step.",
        "about_eyebrow": "The people behind Practical AI", "about_h1": "A core team with business and AI experience.", "about_lead": "Get to know the people behind the program. We combine business training, AI implementation and commercial experience around the work your team wants to improve.",
        "about_method_h2": "One shared method", "about_method_p": "We start with a recurring task and the people responsible for it. Together we map an AI step, practise on a representative example, review the output and document a next test for normal work.",
        "about_background_h2": "A team around the task", "about_background_p": "Program roles follow the team's needs, tools and workflow. Practical AI coordinates the learning design, working sessions and review so each group has a clear path from its first task to a practical next step.",
        "meta_home": ("Corporate AI Training for Business Teams | Practical AI", "Hands-on corporate AI training for business teams. One-day labs, one-week workflow sprints and four-week programs built around real work."),
        "meta_hr": ("AI Training for HR and L&D Teams | Practical AI", "Plan practical AI training for employees around real workflows, agreed tools, human review and a clear next step."),
        "meta_programs": ("Corporate AI Training Programs | Practical AI", "Compare a company-wide AI lab for up to 150 people, a small leadership sprint and a four-week program for around 15 middle managers."),
        "meta_about": ("Our Team | Danil Usik, Svetlana Galakhova & Julia Krylova | Practical AI", "Meet the Practical AI core team, explore their experience and discuss corporate AI training with Danil Usik."),
    },
    "ru": {
        "nav": ["Для HR и L&D", "Программы", "Команда", "Руководства"],
        "discuss": "Написать Данилу", "language": "EN",
        "hero_eyebrow": "Practical AI · для бизнес-команд",
        "hero_h1": "Корпоративное AI-обучение <em>на задачах вашей команды.</em>",
        "hero_lede": "Берём отчёты, исследования и управленческие задачи, с которыми команда работает каждую неделю. Помогаем участникам собрать AI-сценарий, проверить результат и оформить плейбук для следующего рабочего дня.",
        "hero_cta": "Написать Данилу в WhatsApp", "hero_secondary": "Посмотреть программы",
        "hero_note": "Начните с размера команды и одной задачи, которую хотите улучшить.",
        "hero_team": "Познакомиться с командой",
        "telegram_alt": "Или написать в Telegram",
        "flow_top": "Как работает команда", "flow_status": "Рабочая модель",
        "flow_steps": [("Выбираем задачу команды", "Начинаем с повторяющегося процесса"), ("Размечаем AI-шаг", "Входные данные, результат и критерии качества"), ("Практикуемся и проверяем", "Согласованные инструменты и оценка специалиста"), ("Определяем следующий шаг", "Сохраняем сценарий и план его проверки")],
        "flow_output": "Осязаемый результат", "flow_output_text": "сценарий команды, чек-лист проверки и следующий тест",
        "programs_eyebrow": "Форматы программ", "programs_h2": "Выберите подходящий старт для команды.",
        "programs_intro": "Один день для всей компании до 150 человек, недельный спринт для небольшой группы руководителей или четыре недели практики для примерно 15 руководителей среднего звена.",
        "program_image_alts": ["Большая группа сотрудников на AI-обучении в зале", "Небольшая группа руководителей разбирает управленческий процесс", "Руководители среднего звена работают вместе на AI-практикуме"],
        "program_audiences": ["Вся компания", "CEO и руководство", "Руководители среднего звена"],
        "program_sizes": ["До 150 человек", "Небольшая группа", "Около 15 человек"],
        "programs": [
            ("01 · Один день", "AI-лаборатория для компании", "Однодневное знакомство с прикладным AI на задачах разных команд.", ["Примеры из разных функций", "Практика на знакомых задачах", "Список сценариев для продолжения"], "Обсудить лабораторию"),
            ("02 · Одна неделя", "AI-спринт для руководства", "Короткий спринт для CEO и команды руководителей вокруг одного управленческого процесса.", ["Выбор управленческой задачи", "Проверка одного AI-сценария", "План пилота и критерии оценки"], "Обсудить спринт"),
            ("03 · Четыре недели", "Программа для среднего звена", "Прикладная AI-практика для руководителей разных функций на протяжении четырёх недель.", ["Повторяющиеся задачи между занятиями", "Совместная проверка результатов", "Общий плейбук для руководителей"], "Обсудить программу"),
        ],
        "proof_eyebrow": "Опубликованный кейс", "proof_h2": "Что изменилось в работе одной команды.",
        "proof_p": "Пять руководителей ShildPanel применили AI к четырём разным рабочим задачам. Каждая цифра ниже показывает изменение времени на конкретную задачу в этом кейсе.",
        "proof_tag": "ShildPanel · 5 участников", "proof_title": "Четыре задачи. Четыре результата.",
        "proof_before": "Было", "proof_after": "С AI", "proof_result": "Результат в кейсе",
        "proof_results": [
            {"task": "Отчёты и презентации", "detail": "Время подготовки отчёта и презентации", "before": "60 мин", "after": "12 мин", "note": "Подготовка заняла 12 минут вместо одного часа."},
            {"task": "Анализ рынка и конкурентов", "detail": "Время на исследование рынка и конкурентов", "value": "на 70% меньше времени", "note": "В кейсе отмечено сокращение времени на анализ на 70%."},
            {"task": "Отладка формул в ERP", "detail": "Время на отладку формул в ERP-системе", "before": "9 часов", "after": "15 мин", "note": "Одна задача с формулами заняла 15 минут вместо 9 часов."},
            {"task": "HR-рутина с голосовым вводом", "detail": "Время на ежедневную HR-рутину", "value": "30 мин в день свободнее", "note": "Голосовой ввод высвободил около 30 минут в день."},
        ],
        "proof_note": "Источник: опубликованный кейс Practical AI с командой ShildPanel. Это результаты конкретных задач, а не средний показатель или обещание новой команде.",
        "proof_roles": "Операционный блок · Развитие · Маркетинг · HR · Управление", "proof_case_h3": "Пять руководителей. Разные рабочие задачи.", "proof_case_link": "Прочитать слова участников", "proof_count_unit": "участников",
        "quotes_eyebrow": "Слова участников", "quotes_h2": "Что говорила команда после практики с AI.", "quotes_intro": "Фрагменты отзывов участников группового обучения ShildPanel.",
        "quotes": [("Теперь у меня есть плейбук, который я могу передать команде, чтобы она могла всё реализовать.", "Александр", "Операционный директор"), ("Для меня то, что мы создали, инструмент, который я теперь смогу делегировать.", "Илья", "Маркетинг и аналитика"), ("Whisper — это точно то, что я использую почти ежедневно, это круто.", "Елизавета", "Руководитель HR")],
        "method_eyebrow": "Как устроена практика", "method_h2": "От задачи команды к проверенному способу работы.",
        "method_intro": "В каждой программе соединяем рабочую задачу, AI-шаг, оценку специалиста и следующий тест.",
        "method_visual_alt": "Пример еженедельного статуса: заметки, задачи и данные CRM становятся AI-черновиком; руководитель проверяет цифры, контекст и ответственных.",
        "method_steps": [("01", "Выбираем задачу", "Фиксируем ответственного и нужный результат."), ("02", "Собираем сценарий", "Определяем материалы, инструменты и формат ответа."), ("03", "Проверяем результат", "Используем критерии качества и оценку специалиста."), ("04", "Сохраняем практику", "Документируем сценарий и выбираем следующий тест.")],
        "team_eyebrow": "Основная команда", "team_h2": "Команда Practical AI.",
        "team_p": "Первую задачу вы обсуждаете с Данилом. В нашей команде соединяются опыт бизнес-обучения, внедрения AI и развития бизнеса — вокруг работы ваших сотрудников.",
        "team_link": "Обсудить задачи команды с Данилом",
        "team_roles": ["Основатель · Бизнес-обучение", "AI-стратегия · Практика", "Маркетинг · Развитие бизнеса"],
        "team_bios": ["Более 10 лет в B2B-продажах и развитии бизнеса, опыт работы с группами. Соединяет бизнес-задачи вашей команды с практическим AI-обучением.", "Сооснователь AIHUB.WORKS и практик внедрения AI. Переводит сложные AI-концепции в понятные рабочие сценарии и ведёт практику.", "Опыт в финтехе, блокчейне и электронной коммерции: маркетинг, привлечение инвестиций и общение с инвесторами. Привносит в работу команды взгляд со стороны бизнеса."],
        "guides_eyebrow": "Практические руководства", "guides_h2": "Ответы для тех, кто выбирает AI-обучение.",
        "guides": [("Обучение команд", "Как подготовить команду к AI-обучению", "Роли, процессы и критерии проверки.", "/ru/blog/corporate-ai-training/"), ("Проектные команды", "AI-сценарии для менеджеров проектов", "Встречи, статусы, риски и ответственность человека.", "/ru/blog/ai-for-project-managers/"), ("Финансовые команды", "AI в работе финансовой команды", "Отчёты, формулы и проверка результата.", "/ru/blog/ai-for-finance-teams/")],
        "closing_eyebrow": "Начнём с разговора",
        "closing_h2": "Найдём подходящий старт с AI для вашей команды.",
        "closing_p": "Расскажите о размере команды, повторяющейся задаче и желаемых сроках. Обсудим приоритеты и инструменты, затем вместе выберем формат обучения.",
        "closing_cta": "Написать Данилу в WhatsApp",
        "contact_role": "Основатель · ваш первый контакт",
        "footer_p": "Practical AI · корпоративное AI-обучение на реальных задачах",
        "hr_eyebrow": "Для HR и руководителей обучения", "hr_h1": "AI-обучение, которое команда применяет в работе.",
        "hr_intro": "Выбирайте программу вокруг задачи команды, согласованных инструментов, ясной проверки и следующего шага. Practical AI помогает HR и L&D превратить интерес к AI в конкретный учебный проект.",
        "hr_questions_h2": "Какую задачу решит первая программа?", "hr_questions_p": "Полезный бриф начинается с работы команды, а затем определяет длительность обучения.",
        "hr_questions": [("Кто учится?", "Команда, роли и ответственный за процесс."), ("С чем работают?", "Повторяющаяся задача с видимым результатом."), ("Как проверяют?", "Инструменты, границы данных и оценка специалиста."), ("Что делают после?", "Небольшой тест на следующей рабочей неделе.")],
        "hr_next_h2": "Ясный первый бриф делает обучение полезным.", "hr_next_p": "Расскажите о команде, одной повторяющейся задаче и результате, который хотите увидеть. Вместе выберем лабораторию, спринт или более длительную программу.",
        "program_page_eyebrow": "Корпоративное AI-обучение", "program_page_h1": "Практические AI-программы для бизнес-команд.",
        "program_page_intro": "Выберите лабораторию для всей компании, короткий спринт для руководства или четырёхнедельную практику для среднего звена. Каждый формат строится вокруг реальной работы.",
        "about_eyebrow": "Люди за Practical AI", "about_h1": "Команда с опытом в бизнесе и AI.", "about_lead": "Познакомьтесь с людьми, которые стоят за программой. Соединяем бизнес-обучение, внедрение AI и развитие бизнеса вокруг задач вашей команды.",
        "about_method_h2": "Общий метод", "about_method_p": "Начинаем с повторяющейся задачи и людей, которые за неё отвечают. Вместе размечаем AI-шаг, практикуемся на понятном примере, проверяем результат и документируем следующий тест для повседневной работы.",
        "about_background_h2": "Команда под задачу", "about_background_p": "Роли в программе зависят от команды, её инструментов и процесса. Practical AI координирует разработку программы, рабочие встречи и проверку результата, чтобы группа прошла понятный путь от первой задачи к следующему практическому шагу.",
        "meta_home": ("Корпоративное AI-обучение для команд | Practical AI", "Практическое AI-обучение для бизнес-команд на реальных задачах: однодневная лаборатория, недельный спринт и четырёхнедельная программа."),
        "meta_hr": ("AI-обучение для HR и L&D | Practical AI", "Как организовать AI-обучение сотрудников на рабочих процессах: задачи, согласованные инструменты, проверка и следующий шаг."),
        "meta_programs": ("Программы корпоративного AI-обучения | Practical AI", "Сравните AI-лабораторию до 150 человек, спринт для небольшой группы руководителей и четырёхнедельную программу для примерно 15 руководителей среднего звена."),
        "meta_about": ("Команда | Данил Усик, Светлана Галахова и Юлия Крылова | Practical AI", "Познакомьтесь с основной командой Practical AI и обсудите корпоративное AI-обучение с Данилом Усиком."),
    },
}


def u(lang: str, route: str = "") -> str:
    return ("/ru" if lang == "ru" else "") + "/" + (route + "/" if route else "")


def contact(lang: str, topic: str = "team", channel: str = "whatsapp") -> str:
    messages = {
        "en": {"team": "Hello! I’d like to discuss AI training for my team.", "lab": "Hello! I’d like to discuss a company-wide AI lab.", "sprint": "Hello! I’d like to discuss a one-week AI leadership sprint.", "program": "Hello! I’d like to discuss a four-week middle management program."},
        "ru": {"team": "Здравствуйте! Хочу обсудить AI-обучение для моей команды.", "lab": "Здравствуйте! Хочу обсудить AI-лабораторию для всей компании.", "sprint": "Здравствуйте! Хочу обсудить недельный AI-спринт для руководства.", "program": "Здравствуйте! Хочу обсудить четырёхнедельную программу для руководителей среднего звена."},
    }
    destination = f"https://wa.me/{WHATSAPP_NUMBER}?text=" if channel == "whatsapp" else "https://t.me/Danil_alto?text="
    return destination + quote(messages[lang][topic], safe="")


def esc(value: str) -> str:
    return escape(value, quote=True)


def style_ref(name: str = "sales-site.css") -> str:
    version = hashlib.sha256((DOCS / "assets" / "brand" / name).read_bytes()).hexdigest()[:10]
    return f"/assets/brand/{name}?v={version}"


def schema(lang: str, route: str) -> dict:
    org = {"@type": "Organization", "@id": BASE + "/#organization", "name": "Practical AI", "url": BASE + "/", "logo": BASE + "/assets/brand/logo-primary.svg", "telephone": "+34627184000", "founder": {"@type": "Person", "name": "Danil Usik", "sameAs": TEAM_PROFILES[0]["linkedin"]}}
    webpage = {"@type": "WebPage", "@id": BASE + u(lang, route) + "#webpage", "url": BASE + u(lang, route), "inLanguage": lang, "isPartOf": {"@id": BASE + "/#website"}}
    graph = [org, {"@type": "WebSite", "@id": BASE + "/#website", "name": "Practical AI", "url": BASE + "/", "publisher": {"@id": BASE + "/#organization"}}, webpage]
    if route != "about":
        graph.append({"@type": "Service", "name": "Corporate AI training" if lang == "en" else "Корпоративное AI-обучение", "serviceType": "Corporate AI training", "provider": {"@id": BASE + "/#organization"}, "url": BASE + u(lang, route)})
    return {"@context": "https://schema.org", "@graph": graph}


def site_header(lang: str, route: str, switch_route: str | None = None) -> str:
    c = COPY[lang]
    other = "ru" if lang == "en" else "en"
    nav_routes = ["for-hr", "programs", "about", "blog"]
    nav = "".join(f'<a href="{u(lang, route_name)}"' + (' aria-current="page"' if route == route_name else '') + f'>{esc(label)}</a>' for route_name, label in zip(nav_routes, c["nav"]))
    lang_label = "Переключить язык на русский" if lang == "en" else "Switch language to English"
    home_label = "Practical AI home" if lang == "en" else "Practical AI — на главную"
    skip_label = "Skip to main content" if lang == "en" else "Перейти к содержанию"
    contact_label = "Message Danil on WhatsApp" if lang == "en" else "Написать Данилу в WhatsApp"
    return f'<header class="site-header"><a class="skip-link" href="#main-content">{skip_label}</a><div class="wrap nav"><a href="{u(lang)}" aria-label="{home_label}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a><nav class="nav-links" aria-label="{"Main navigation" if lang == "en" else "Основная навигация"}">{nav}</nav><div class="nav-end"><a class="lang-switch" href="{u(other,switch_route if switch_route is not None else route)}" lang="{other}" aria-label="{lang_label}">{esc(c["language"])}</a><a class="button button--small" aria-label="{contact_label}" href="{contact(lang)}" target="_blank" rel="noopener noreferrer"><span class="contact-label">{esc(c["discuss"])}</span><span class="contact-short" aria-hidden="true">WhatsApp</span><span aria-hidden="true">↗</span></a></div></div></header>'


def site_footer(lang: str, route: str = "") -> str:
    c = COPY[lang]
    nav = "".join(f'<a href="{u(lang, route_name)}"' + (' aria-current="page"' if route == route_name else '') + f'>{esc(label)}</a>' for route_name, label in zip(["for-hr", "programs", "about", "blog"], c["nav"]))
    footer_label = "Footer navigation" if lang == "en" else "Навигация в подвале"
    return f'<footer class="site-footer"><div class="wrap footer-inner"><div class="footer-brand"><a href="{u(lang)}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a><p>{esc(c["footer_p"])}</p></div><div class="footer-column"><nav class="footer-links" aria-label="{footer_label}">{nav}</nav><div class="footer-contact"><a href="{contact(lang)}" target="_blank" rel="noopener noreferrer">WhatsApp · +34 627 184 000 ↗</a><a href="{contact(lang,channel='telegram')}" target="_blank" rel="noopener noreferrer">Telegram ↗</a></div></div></div></footer>'


def shell(lang: str, route: str, body: str) -> str:
    c = COPY[lang]
    key = "home" if not route else route.replace("for-hr", "hr")
    title, description = c["meta_" + key]
    title, description = esc(title), esc(description)
    canonical = BASE + u(lang, route)
    site_name = "Practical AI"
    return f'''<!doctype html>
<html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#17213d"><meta name="robots" content="index,follow,max-image-preview:large">
<title>{title}</title><meta name="description" content="{description}">
<link rel="canonical" href="{canonical}"><link rel="alternate" hreflang="en" href="{BASE + u('en',route)}"><link rel="alternate" hreflang="ru" href="{BASE + u('ru',route)}"><link rel="alternate" hreflang="x-default" href="{BASE + u('en',route)}">
<meta property="og:type" content="website"><meta property="og:site_name" content="{site_name}"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="{'en_US' if lang == 'en' else 'ru_RU'}"><meta property="og:image" content="{BASE}/assets/brand/social-card.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{description}"><meta name="twitter:image" content="{BASE}/assets/brand/social-card.png">
<link rel="icon" type="image/svg+xml" href="/assets/brand/symbol-primary.svg"><link rel="stylesheet" href="{style_ref()}">
<script type="application/ld+json">{json.dumps(schema(lang,route),ensure_ascii=False,separators=(',',':'))}</script>
</head><body>
{site_header(lang,route)}
<main id="main-content" tabindex="-1">{body}</main>
{site_footer(lang,route)}
</body></html>'''


def program_cards(lang: str) -> str:
    c = COPY[lang]
    topics = ["lab", "sprint", "program"]
    return '<div class="program-grid">' + "".join(
        f'<article class="program-card' + (' program-card--lead' if i == 1 else '') + f'" id="{topics[i]}"><div class="program-card-body"><div class="program-card-header"><figure class="program-visual"><img src="/assets/corporate/{PROGRAM_IMAGES[i]}" alt="{esc(c["program_image_alts"][i])}" width="384" height="384" loading="lazy" decoding="async"></figure><div><span class="program-tag">{esc(tag)}</span><h3>{esc(name)}</h3></div></div><div class="program-fit"><span>{esc(c["program_audiences"][i])}</span><b>{esc(c["program_sizes"][i])}</b></div><p>{esc(description)}</p><ul>' + "".join(f'<li>{esc(item)}</li>' for item in bullets) + f'</ul><a class="card-link" href="{contact(lang,topics[i])}" target="_blank" rel="noopener noreferrer">{esc(cta)} ↗</a></div></article>'
        for i, (tag, name, description, bullets, cta) in enumerate(c["programs"])
    ) + '</div>'


def method_visual(lang: str) -> str:
    c = COPY[lang]
    return f'<figure class="method-visual"><picture><source media="(max-width: 600px)" srcset="/assets/brand/workflow-method-{lang}-mobile.svg"><img src="/assets/brand/workflow-method-{lang}.svg" alt="{esc(c["method_visual_alt"])}" width="1200" height="650" loading="lazy" decoding="async"></picture></figure>'


def closing(lang: str) -> str:
    c = COPY[lang]
    name = "Danil Usik" if lang == "en" else "Данил Усик"
    return f'<section class="closing" id="contact"><div class="wrap closing-inner"><div class="closing-copy"><span class="eyebrow">{esc(c["closing_eyebrow"])}</span><h2>{esc(c["closing_h2"])}</h2><p>{esc(c["closing_p"])}</p></div><div class="contact-card"><div class="contact-person"><img src="/assets/team/danil-usik.jpg" alt="{name}" width="64" height="64" loading="lazy"><div><strong>{name}</strong><span>{esc(c["contact_role"])}</span></div></div><a class="button button--dark" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c["closing_cta"])} ↗</a><div class="contact-alternatives"><span>+34 627 184 000</span><a href="{contact(lang,channel='telegram')}" target="_blank" rel="noopener noreferrer">Telegram ↗</a></div></div></div></section>'


def team_section(lang: str) -> str:
    c = COPY[lang]
    cards = []
    for index, member in enumerate(TEAM_PROFILES):
        name = member["name"] if lang == "en" else member["ru_name"]
        linkedin_label = f"View {name} on LinkedIn" if lang == "en" else f"Профиль {name} в LinkedIn"
        cards.append(f'<article class="team-card"><div class="team-portrait"><img src="/assets/team/{member["photo"]}" alt="{name}" width="400" height="400" loading="lazy" decoding="async"></div><div class="team-card-body"><span class="team-role">{esc(c["team_roles"][index])}</span><h3>{name}</h3><p>{esc(c["team_bios"][index])}</p><a class="card-link" href="{member["linkedin"]}" aria-label="{linkedin_label}" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span></a></div></article>')
    return f'<section class="section team-section" id="team"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["team_eyebrow"])}</span><h2>{esc(c["team_h2"])}</h2></div><p>{esc(c["team_p"])}</p></div><div class="team-cards">{"".join(cards)}</div><div class="team-next"><a class="card-link" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c["team_link"])} ↗</a></div></div></section>'


def evidence_teaser(lang: str) -> str:
    c = COPY[lang]
    label = "Explore the team case and participant quotes" if lang == "en" else "Посмотреть результаты кейса и слова участников"
    quote_text, quote_name, quote_role = c["quotes"][0]
    return f'<section class="section evidence-teaser"><div class="wrap evidence-teaser-grid"><div><span class="eyebrow">{esc(c["proof_tag"])}</span><h2>{esc(c["proof_h2"])}</h2><p>{esc(c["proof_p"])}</p><a class="card-link" href="{u(lang)}#case">{esc(label)} →</a></div><figure><blockquote>“{esc(quote_text)}”</blockquote><figcaption>{esc(quote_name)} · {esc(quote_role)}</figcaption></figure></div></section>'


def proof_cards(lang: str) -> str:
    c = COPY[lang]
    cards = []
    for number, result in enumerate(c["proof_results"], 1):
        if "before" in result:
            measure = (
                f'<div class="proof-comparison"><div><span>{esc(c["proof_before"])}</span><strong>{esc(result["before"])}</strong></div>'
                f'<span class="proof-arrow" aria-hidden="true">→</span><div><span>{esc(c["proof_after"])}</span><strong>{esc(result["after"])}</strong></div></div>'
            )
        else:
            measure = f'<div class="proof-single"><span>{esc(c["proof_result"])}</span><strong>{esc(result["value"])}</strong></div>'
        cards.append(
            f'<article class="proof-metric"><span class="proof-index">{number:02}</span><h4>{esc(result["task"])}</h4>'
            f'<p class="proof-task">{esc(result["detail"])}</p>{measure}<p class="proof-explanation">{esc(result["note"])}</p></article>'
        )
    return "".join(cards)


def home(lang: str) -> str:
    c = COPY[lang]
    steps = "".join(f'<div class="flow-step"><span class="num">{i:02}</span><div><b>{esc(title)}</b><small>{esc(detail)}</small></div></div>' for i, (title, detail) in enumerate(c["flow_steps"], 1))
    method = "".join(f'<article class="method-card"><span class="step">{number}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p></article>' for number, title, detail in c["method_steps"])
    guides = "".join(f'<a class="guide-card" href="{url}"><span>{esc(tag)}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p><b>{"Read guide" if lang == "en" else "Читать руководство"} ↗</b></a>' for tag, title, detail, url in c["guides"])
    proof_facts = proof_cards(lang)
    quotes = "".join(f'<figure class="quote-card"><blockquote>“{esc(words)}”</blockquote><figcaption><b>{esc(name)}</b><span>{esc(role)}</span></figcaption></figure>' for words, name, role in c["quotes"])
    return f'''<section class="hero"><div class="wrap hero-grid"><div><span class="eyebrow">{esc(c['hero_eyebrow'])}</span><h1>{c['hero_h1']}</h1><p class="hero-lede">{esc(c['hero_lede'])}</p><div class="hero-actions"><a class="button" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c['hero_cta'])} ↗</a><a class="button button--ghost" href="#programs">{esc(c['hero_secondary'])} ↓</a></div><p class="hero-note">{esc(c['hero_note'])}</p><div class="hero-contact-options"><a href="{contact(lang,channel='telegram')}" target="_blank" rel="noopener noreferrer">{esc(c['telegram_alt'])} ↗</a><a href="#team">{esc(c['hero_team'])} ↓</a></div></div><div class="flow-card"><div class="flow-top"><span>{esc(c['flow_top'])}</span><span>● {esc(c['flow_status'])}</span></div>{steps}<div class="flow-output"><b>{esc(c['flow_output'])}</b> · {esc(c['flow_output_text'])}</div></div></div></section>
<section class="section programs" id="programs"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['programs_eyebrow'])}</span><h2>{esc(c['programs_h2'])}</h2></div><p>{esc(c['programs_intro'])}</p></div>{program_cards(lang)}</div></section>
<section class="section proof" id="case"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['proof_eyebrow'])}</span><h2>{esc(c['proof_h2'])}</h2></div><p>{esc(c['proof_p'])}</p></div><div class="case-layout"><div class="case-story"><div class="case-company"><img src="/assets/img/shildpanel-mark.svg" alt="" width="70" height="76" loading="lazy"><div><strong>ShildPanel</strong><span>Production Company</span></div></div><span class="case-story-number">5<span> / {esc(c['proof_count_unit'])}</span></span><h3>{esc(c['proof_case_h3'])}</h3><p>{esc(c['proof_roles'])}</p><a class="card-link" href="#reviews">{esc(c['proof_case_link'])} →</a></div><div class="proof-panel"><span class="case-tag">{esc(c['proof_tag'])}</span><h3>{esc(c['proof_title'])}</h3><div class="proof-facts">{proof_facts}</div></div></div></div></section>
<section class="section quotes" id="reviews"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['quotes_eyebrow'])}</span><h2>{esc(c['quotes_h2'])}</h2></div><p>{esc(c['quotes_intro'])}</p></div><div class="quote-grid">{quotes}</div></div></section>
{team_section(lang)}
<section class="section method"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['method_eyebrow'])}</span><h2>{esc(c['method_h2'])}</h2></div><p>{esc(c['method_intro'])}</p></div><div class="method-grid">{method}</div>{method_visual(lang)}</div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['guides_eyebrow'])}</span><h2>{esc(c['guides_h2'])}</h2></div></div><div class="guide-grid">{guides}</div></div></section>{closing(lang)}'''


def page_hero(lang: str, eyebrow: str, h1: str, intro: str) -> str:
    return f'<section class="page-hero"><div class="wrap"><span class="eyebrow">{esc(eyebrow)}</span><h1>{esc(h1)}</h1><p>{esc(intro)}</p><a class="button" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(COPY[lang]["discuss"])} ↗</a><div class="page-contact-options"><a href="{contact(lang,channel='telegram')}" target="_blank" rel="noopener noreferrer">{esc(COPY[lang]["telegram_alt"])} ↗</a></div></div></section>'


def hr(lang: str) -> str:
    c = COPY[lang]
    questions = "".join(f'<div class="question"><b>{esc(title)}</b><span>{esc(detail)}</span></div>' for title, detail in c["hr_questions"])
    return page_hero(lang,c["hr_eyebrow"],c["hr_h1"],c["hr_intro"]) + f'<section class="section"><div class="wrap content-grid"><div><span class="eyebrow">{esc(c["hr_eyebrow"])}</span><h2>{esc(c["hr_questions_h2"])}</h2><p>{esc(c["hr_questions_p"])}</p></div><div class="question-list">{questions}</div></div></section><section class="section programs"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["programs_eyebrow"])}</span><h2>{esc(c["programs_h2"])}</h2></div></div>{program_cards(lang)}</div></section>{evidence_teaser(lang)}<section class="section proof"><div class="wrap content-grid"><h2>{esc(c["hr_next_h2"])}</h2><div><p>{esc(c["hr_next_p"])}</p><a class="button button--dark" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c["closing_cta"])} ↗</a></div></div></section>{closing(lang)}'


def programs(lang: str) -> str:
    c = COPY[lang]
    method = "".join(f'<article class="method-card"><span class="step">{number}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p></article>' for number, title, detail in c["method_steps"])
    return page_hero(lang,c["program_page_eyebrow"],c["program_page_h1"],c["program_page_intro"]) + f'<section class="section programs"><div class="wrap">{program_cards(lang)}</div></section><section class="section method"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["method_eyebrow"])}</span><h2>{esc(c["method_h2"])}</h2></div><p>{esc(c["method_intro"])}</p></div><div class="method-grid">{method}</div>{method_visual(lang)}</div></section>{evidence_teaser(lang)}{closing(lang)}'


def about(lang: str) -> str:
    c = COPY[lang]
    method = "".join(f'<article class="method-card"><span class="step">{number}</span><h3>{esc(title)}</h3><p>{esc(detail)}</p></article>' for number, title, detail in c["method_steps"])
    return f'<section class="section editorial"><div class="wrap"><span class="eyebrow">{esc(c["about_eyebrow"])}</span><h1>{esc(c["about_h1"])}</h1><p class="lead">{esc(c["about_lead"])}</p><div class="content-grid"><div><h2>{esc(c["about_method_h2"])}</h2><p>{esc(c["about_method_p"])}</p></div><div><h2>{esc(c["about_background_h2"])}</h2><p>{esc(c["about_background_p"])}</p></div></div></div></section>' + team_section(lang) + f'<section class="section method"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["method_eyebrow"])}</span><h2>{esc(c["method_h2"])}</h2></div><p>{esc(c["method_intro"])}</p></div><div class="method-grid">{method}</div>{method_visual(lang)}</div></section>{evidence_teaser(lang)}<section class="section programs"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["programs_eyebrow"])}</span><h2>{esc(c["programs_h2"])}</h2></div></div>{program_cards(lang)}</div></section>{closing(lang)}'


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
    print("Built eight sales-led static pages and updated sitemap")


if __name__ == "__main__":
    main()
