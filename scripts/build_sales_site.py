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
        "linkedin_alt": "Or connect on LinkedIn",
        "flow_top": "What your team works through", "flow_status": "Working model",
        "flow_steps": [("Choose a real team task", "Start with a repeatable workflow"), ("Map the AI step", "Inputs, output and quality criteria"), ("Practise and review", "Use agreed tools; a person checks the result"), ("Take a next step", "Keep a workflow card and a plan to test it")],
        "flow_output": "Visible output", "flow_output_text": "a team workflow, review checklist and next test",
        "programs_eyebrow": "Program formats", "programs_h2": "Choose the right starting pace for your team.",
        "programs_intro": "A company-wide day for up to 150 people, a focused week for a small leadership group, or four weeks of practice for around 15 middle managers.",
        "school_teaser_eyebrow": "For private schools · program in Russian",
        "school_teaser_h2": "Build practical AI skills across your school team in four weeks.",
        "school_teaser_p": "Teachers, school leaders and administrative staff work on everyday tasks, create AI assistants and learn to review their outputs. The program includes 8 hours of online sessions and about 10 hours of practice. Full details are available in Russian.",
        "school_teaser_stat": "4 weeks",
        "school_teaser_stat_detail": "8 hours online · about 10 hours of practice",
        "school_teaser_cta": "Explore the program in Russian",
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
        "nav": ["Для HR и обучения", "Программы", "Команда", "Статьи"],
        "discuss": "Написать Данилу", "language": "EN",
        "hero_eyebrow": "Practical AI · для бизнес-команд",
        "hero_h1": "Корпоративное AI-обучение <em>на задачах вашей команды.</em>",
        "hero_lede": "Берём отчёты, исследования и управленческие задачи, с которыми команда работает каждую неделю. Помогаем участникам собрать AI-сценарий, проверить результат и оформить плейбук для следующего рабочего дня.",
        "hero_cta": "Написать Данилу в WhatsApp", "hero_secondary": "Посмотреть программы",
        "hero_note": "Начните с размера команды и одной задачи, которую хотите улучшить.",
        "hero_team": "Познакомиться с командой",
        "linkedin_alt": "Или написать в LinkedIn",
        "flow_top": "Как работает команда", "flow_status": "Рабочая модель",
        "flow_steps": [("Выбираем задачу команды", "Начинаем с повторяющегося процесса"), ("Размечаем AI-шаг", "Входные данные, результат и критерии качества"), ("Практикуемся и проверяем", "Согласованные инструменты и оценка специалиста"), ("Определяем следующий шаг", "Сохраняем сценарий и план его проверки")],
        "flow_output": "Осязаемый результат", "flow_output_text": "сценарий команды, чек-лист проверки и следующий тест",
        "programs_eyebrow": "Форматы программ", "programs_h2": "Выберите подходящий старт для команды.",
        "programs_intro": "Один день для всей компании до 150 человек, недельный спринт для небольшой группы руководителей или четыре недели практики для примерно 15 руководителей среднего звена.",
        "school_teaser_eyebrow": "Для частных школ",
        "school_teaser_h2": "Команда школы осваивает ИИ за четыре недели.",
        "school_teaser_p": "Учителя, руководители и сотрудники администрации разбирают задачи из своей работы, создают ИИ-помощников и учатся проверять их ответы. В программу входят 8 часов онлайн-занятий и около 10 часов практики.",
        "school_teaser_stat": "4 недели",
        "school_teaser_stat_detail": "8 часов онлайн · около 10 часов практики",
        "school_teaser_cta": "Посмотреть программу для школ",
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
        "footer_p": "Practical AI · обучение команд работе с ИИ на реальных задачах",
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
        "meta_for-schools": ("Повышение квалификации команды школы за 4 недели | Practical AI", "Практическая программа работы с ИИ для учителей, академических руководителей и административных команд частных школ."),
    },
}


def u(lang: str, route: str = "") -> str:
    return ("/ru" if lang == "ru" else "") + "/" + (route + "/" if route else "")


def contact(lang: str, topic: str = "team", channel: str = "whatsapp") -> str:
    if channel == "linkedin":
        return TEAM_PROFILES[0]["linkedin"]
    messages = {
        "en": {"team": "Hello! I’d like to discuss AI training for my team.", "lab": "Hello! I’d like to discuss a company-wide AI lab.", "sprint": "Hello! I’d like to discuss a one-week AI leadership sprint.", "program": "Hello! I’d like to discuss a four-week middle management program."},
        "ru": {"team": "Здравствуйте! Хочу обсудить AI-обучение для моей команды.", "lab": "Здравствуйте! Хочу обсудить AI-лабораторию для всей компании.", "sprint": "Здравствуйте! Хочу обсудить недельный AI-спринт для руководства.", "program": "Здравствуйте! Хочу обсудить четырёхнедельную программу для руководителей среднего звена.", "school": "Здравствуйте! Хочу обсудить обучение работе с ИИ для команды школы."},
    }
    destination = f"https://wa.me/{WHATSAPP_NUMBER}?text="
    return destination + quote(messages[lang][topic], safe="")


def esc(value: str) -> str:
    return escape(value, quote=True)


def style_ref(name: str = "sales-site.css") -> str:
    version = hashlib.sha256((DOCS / "assets" / "brand" / name).read_bytes()).hexdigest()[:10]
    return f"/assets/brand/{name}?v={version}"


def schema(lang: str, route: str) -> dict:
    org = {"@type": "Organization", "@id": BASE + "/#organization", "name": "Practical AI", "url": BASE + "/", "logo": BASE + "/assets/brand/logo-primary.svg", "founder": {"@type": "Person", "name": "Danil Usik", "sameAs": TEAM_PROFILES[0]["linkedin"]}}
    webpage = {"@type": "WebPage", "@id": BASE + u(lang, route) + "#webpage", "url": BASE + u(lang, route), "inLanguage": lang, "isPartOf": {"@id": BASE + "/#website"}}
    graph = [org, {"@type": "WebSite", "@id": BASE + "/#website", "name": "Practical AI", "url": BASE + "/", "publisher": {"@id": BASE + "/#organization"}}, webpage]
    if route != "about":
        if lang == "ru" and route == "for-schools":
            graph.append({"@type": "Service", "name": "Повышение квалификации команды школы по работе с ИИ", "serviceType": "AI training for adult school staff", "provider": {"@id": BASE + "/#organization"}, "url": BASE + u(lang, route)})
        else:
            graph.append({"@type": "Service", "name": "Corporate AI training" if lang == "en" else "Корпоративное AI-обучение", "serviceType": "Corporate AI training", "provider": {"@id": BASE + "/#organization"}, "url": BASE + u(lang, route)})
    return {"@context": "https://schema.org", "@graph": graph}


def site_header(lang: str, route: str, switch_route: str | None = None) -> str:
    c = COPY[lang]
    other = "ru" if lang == "en" else "en"
    nav_routes = ["for-hr", "programs", "about", "blog"]
    nav_items = list(zip(nav_routes, c["nav"]))
    if lang == "ru":
        nav_items.append(("for-schools", "Для школ"))
    nav = "".join(f'<a href="{u(lang, route_name)}"' + (' aria-current="page"' if route == route_name else '') + f'>{esc(label)}</a>' for route_name, label in nav_items)
    lang_label = "Переключить язык на русский" if lang == "en" else "Switch language to English"
    home_label = "Practical AI home" if lang == "en" else "Practical AI — на главную"
    skip_label = "Skip to main content" if lang == "en" else "Перейти к содержанию"
    if lang == "ru" and route == "for-schools":
        contact_label = "Связаться с командой Practical AI"
        contact_text = "Связаться с командой Practical AI"
        contact_short = "Связаться с командой Practical AI"
        contact_url = "#contact"
        header_contact = f'<a class="button button--small" aria-label="{contact_label}" href="{contact_url}"><span class="contact-label">{esc(contact_text)}</span><span class="contact-short" aria-hidden="true">{contact_short}</span></a>'
    else:
        contact_label = "Message Danil on WhatsApp" if lang == "en" else "Написать Данилу в WhatsApp"
        contact_text = c["discuss"]
        contact_short = "WhatsApp"
        contact_url = contact(lang)
        header_contact = f'<a class="button button--small" aria-label="{contact_label}" href="{contact_url}" target="_blank" rel="noopener noreferrer"><span class="contact-label">{esc(contact_text)}</span><span class="contact-short" aria-hidden="true">{contact_short}</span><span aria-hidden="true">↗</span></a>'
    return f'<header class="site-header"><a class="skip-link" href="#main-content">{skip_label}</a><div class="wrap nav"><a href="{u(lang)}" aria-label="{home_label}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a><nav class="nav-links" aria-label="{"Main navigation" if lang == "en" else "Основная навигация"}">{nav}</nav><div class="nav-end"><a class="lang-switch" href="{u(other,switch_route if switch_route is not None else route)}" lang="{other}" aria-label="{lang_label}">{esc(c["language"])}</a>{header_contact}</div></div></header>'


def site_footer(lang: str, route: str = "") -> str:
    c = COPY[lang]
    nav_items = list(zip(["for-hr", "programs", "about", "blog"], c["nav"]))
    if lang == "ru":
        nav_items.append(("for-schools", "Для школ"))
    nav = "".join(f'<a href="{u(lang, route_name)}"' + (' aria-current="page"' if route == route_name else '') + f'>{esc(label)}</a>' for route_name, label in nav_items)
    footer_label = "Footer navigation" if lang == "en" else "Навигация в подвале"
    if lang == "ru" and route == "for-schools":
        whatsapp_contact = contact(lang, "school")
    else:
        whatsapp_contact = contact(lang)
    linkedin_contact = contact(lang, channel="linkedin")
    if lang == "ru" and route == "for-schools":
        contacts = f'<div class="footer-contact"><a href="{whatsapp_contact}" target="_blank" rel="noopener noreferrer">Связаться с командой Practical AI</a></div>'
    else:
        contacts = f'<div class="footer-contact"><a href="{whatsapp_contact}" target="_blank" rel="noopener noreferrer">WhatsApp ↗</a><a href="{linkedin_contact}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div>'
    return f'<footer class="site-footer"><div class="wrap footer-inner"><div class="footer-brand"><a href="{u(lang)}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a><p>{esc(c["footer_p"])}</p></div><div class="footer-column"><nav class="footer-links" aria-label="{footer_label}">{nav}</nav>{contacts}</div></div></footer>'


def shell(lang: str, route: str, body: str) -> str:
    c = COPY[lang]
    key = "home" if not route else route.replace("for-hr", "hr")
    title, description = c["meta_" + key]
    title, description = esc(title), esc(description)
    canonical = BASE + u(lang, route)
    site_name = "Practical AI"
    if lang == "ru" and route == "for-schools":
        alternates = f'<link rel="alternate" hreflang="ru" href="{canonical}"><link rel="alternate" hreflang="x-default" href="{canonical}">'
        body_class = ' class="school-page"'
    else:
        alternates = f'<link rel="alternate" hreflang="en" href="{BASE + u("en",route)}"><link rel="alternate" hreflang="ru" href="{BASE + u("ru",route)}"><link rel="alternate" hreflang="x-default" href="{BASE + u("en",route)}">'
        body_class = ""
    return f'''<!doctype html>
<html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#17213d"><meta name="robots" content="index,follow,max-image-preview:large">
<title>{title}</title><meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">{alternates}
<meta property="og:type" content="website"><meta property="og:site_name" content="{site_name}"><meta property="og:title" content="{title}"><meta property="og:description" content="{description}"><meta property="og:url" content="{canonical}"><meta property="og:locale" content="{'en_US' if lang == 'en' else 'ru_RU'}"><meta property="og:image" content="{BASE}/assets/brand/social-card.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{title}"><meta name="twitter:description" content="{description}"><meta name="twitter:image" content="{BASE}/assets/brand/social-card.png">
<link rel="icon" type="image/svg+xml" href="/assets/brand/symbol-primary.svg"><link rel="stylesheet" href="{style_ref()}">
<script type="application/ld+json">{json.dumps(schema(lang,route),ensure_ascii=False,separators=(',',':'))}</script>
</head><body{body_class}>
{site_header(lang,route,switch_route="" if lang == "ru" and route == "for-schools" else None)}
<main id="main-content" tabindex="-1">{body}</main>
{site_footer(lang,route)}
</body></html>'''


def school_page() -> str:
    return '''


<section class="hero school-hero"><div class="wrap school-hero-grid"><div class="school-hero-copy"><span class="eyebrow">Повышение квалификации команды частной школы</span><h1>За четыре недели каждый участник создаёт и проверяет ИИ-помощника для своей задачи.</h1><p class="hero-lede">Команда школы осваивает ИИ на рабочих задачах: от выбора сценария до проверки ответов помощника и оценки результата.</p><div class="hero-actions"><a class="button button--dark" href="#contact">Связаться с командой Practical AI</a><a class="button button--light" href="#program">К программе ↓</a></div><p class="hero-note">Занятия проходят онлайн. Очное обучение в вашей школе обсуждаем отдельно.</p></div><aside class="school-offer-card school-result-card"><span class="school-offer-label">Результат для участника</span><strong class="school-offer-price">ИИ-помощник</strong><p>Рабочий прототип для одной задачи участника, проверка ответов и план дальнейшего применения.</p><ul><li>инструкции под конкретную задачу;</li><li>критерии проверки ответов;</li><li>практика на материалах, согласованных со школой.</li></ul></aside></div></section>

<section class="section school-role-section" id="program"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Для разных ролей в школе</span><h2>У каждой роли в школе — свои задачи для работы с ИИ.</h2></div><p>Задачи учителей, руководителей учебной части и администрации различаются. После диагностики подберём содержание программы под задачи каждой группы.</p></div><div class="school-role-grid"><article class="school-role-card"><span>Учителя</span><h3>Учебные материалы и обратная связь</h3><p>Черновики заданий для разных уровней подготовки, варианты объяснений и упражнений, критерии оценки и комментарии к письменным работам.</p><small>Учитель сверяет материалы с программой и решает, что использовать.</small></article><article class="school-role-card"><span>Руководители учебной части</span><h3>Методическая работа и учебная документация</h3><p>Наведение порядка в методических материалах, подготовка отчётов и разбор обезличенных данных об учебном процессе.</p><small>Руководитель учебной части сверяет выводы с документами и учитывает контекст школы.</small></article><article class="school-role-card"><span>Руководство и администрация</span><h3>Бюджет, документы и решения</h3><p>Сводки по обезличенным данным, подготовка вопросов к совещаниям, поиск информации в документах школы и черновики регламентов.</p><small>Руководитель сверяет данные и сам принимает решение.</small></article></div></div></section>

<section class="section school-demos" id="examples"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Практика в школе</span><h2>Примеры рабочих задач с ИИ</h2></div><p>Демонстрационные примеры подготовлены на синтетических данных.</p></div><div class="school-demo-grid"><details class="school-demo-card"><summary class="school-demo-head"><span>Пример для учителя</span></summary><div class="school-demo-content"><h3>Задания о круговороте воды для 5-го класса</h3><div class="school-demo-flow"><div><b>Исходная задача</b><p>Подготовить три варианта задания к одной учебной цели для учащихся с разным уровнем подготовки.</p></div><div class="school-artifact"><b>Черновик ИИ-помощника</b><ol><li>Базовый уровень: расположить этапы круговорота воды по порядку.</li><li>Средний уровень: объяснить, как вода из лужи испаряется и становится частью облака.</li><li>Повышенная сложность: придумать опыт, который показывает испарение и конденсацию.</li></ol></div><div><b>Проверка педагога</b><p>Сверить задания с темой урока, возрастом и требованиями программы; при необходимости изменить формулировки.</p></div></div></div></details><details class="school-demo-card"><summary class="school-demo-head"><span>Пример для директора</span></summary><div class="school-demo-content"><h3>Записка к обсуждению бюджета школы</h3><div class="school-demo-flow"><div><b>Исходная задача</b><p>В таблице уже рассчитаны плановые и фактические суммы. С помощью ИИ подготовить короткую записку с вопросами к совещанию.</p></div><div class="school-artifact"><b>Фрагмент черновика</b><p>«По статье „Учебные материалы“ расходы превысили план на 6 условных единиц. Уточнить период закупок и причину у ответственного сотрудника». </p><p class="school-artifact-note">Число условное. Суммы и выводы сверяет ответственный за бюджет.</p></div><div><b>Проверка руководителя</b><p>Сверить сумму с исходной таблицей, уточнить контекст и выбрать вопросы для встречи.</p></div></div></div></details></div></div></section>

<section class="section school-preparation"><div class="wrap"><div class="section-head"><div><span class="eyebrow">До начала занятий</span><h2>Сначала изучаем задачи школы и собираем программу обучения.</h2></div><p>Учебная часть длится четыре недели. Диагностика и подготовка проходят до её начала.</p></div><div class="school-prep-grid"><article><span>01 · до 1 недели</span><h3>Диагностика</h3><p>Проводим интервью с собственником школы, руководителями и частью сотрудников. Остальная команда проходит структурированный опрос.</p><ul><li>карта процессов, на которые уходит больше всего времени;</li><li>задачи, где сотрудникам может помочь ИИ;</li><li>рекомендации по составу учебных групп и программе для разных ролей;</li><li>план дальнейшего развития команды.</li></ul><p>Результаты диагностики передаём школе.</p></article><article><span>02 · до 2 недель</span><h3>Подготовка программы</h3><p>Определяем, какие задачи возьмут участники, что они уже умеют, кто будет учиться вместе и как пройдут занятия.</p><ul><li>согласуем сервисы и способы проверки;</li><li>выберем материалы, которые можно использовать;</li><li>согласуем объём поддержки и критерии оценки;</li><li>подготовим задания для разных ролей.</li></ul></article></div><p class="school-start-note"><strong>Когда начнутся занятия?</strong> Занятия обычно начинаются через месяц после подписания договора, предоплаты и получения материалов от школы.</p></div></section>

<section class="section school-month" id="month"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Четыре недели практики</span><h2>За четыре недели участник создаёт и проверяет ИИ-помощника для своей задачи.</h2></div><p>Темы и расписание уточним после диагностики.</p></div><div class="school-week-grid"><article><span>Неделя 1</span><h3>Выбираете задачу</h3><p>Разбираетесь в возможностях ИИ, выбираете задачу, с которой регулярно сталкиваетесь, и решаете, как оценить результат.</p></article><article><span>Неделя 2</span><h3>Собираете помощника</h3><p>Готовите инструкции, подбираете материалы и настраиваете первую версию ИИ-помощника.</p></article><article><span>Неделя 3</span><h3>Проверяете помощника</h3><p>Применяете его в своей работе, сверяете ответы и вносите правки.</p></article><article><span>Неделя 4</span><h3>Показываете результат</h3><p>Показываете помощника команде, объясняете, как проверять его ответы, и выбираете следующую задачу.</p></article></div><div class="school-workload"><div><strong>8 часов</strong><span>интерактивных онлайн-занятий на участника</span></div><div><strong>около 10 часов</strong><span>практики на задачах сотрудников</span></div><p>Участник практикуется на своих задачах. График согласуем со школой.</p></div></div></section>

<section class="section school-assessment"><div class="wrap school-assessment-grid"><div><span class="eyebrow">Как оцениваем результат</span><h2>Проверяем, что участник умеет делать после обучения.</h2><p>Каждый участник разбирает свою задачу, показывает созданного помощника и объясняет, как использует и проверяет его ответы.</p><p>Участникам, которые посещают занятия и выполняют практику, поможем довести помощника до рабочего прототипа в пределах заранее согласованного объёма. Школа организует участие команды в занятиях.</p></div><ol class="school-assessment-list"><li>Самостоятельно выбрать подходящую задачу.</li><li>Безопасно работать с ИИ и материалами школы.</li><li>Настроить ИИ-помощника для выбранной задачи.</li><li>Проверить ответы помощника на примере рабочей задачи.</li><li>Повторить процесс самостоятельно и настроить его для похожей задачи.</li></ol></div><div class="wrap school-results-note"><strong>По итогам программы школа получит:</strong> индивидуальные оценки навыков участников, помощников, созданных ими во время обучения, учебные материалы, описание рабочих сценариев и рекомендации. Показатели выберем заранее: время выполнения задачи, качество результата и нагрузка команды. Экономию времени и финансовый эффект оценим отдельно по данным школы.</div></section>

<section class="section school-team"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Кто работает с командой</span><h2>Кто будет вести программу</h2></div><p>Диагностику и подготовку программы ведёт команда Practical AI. Состав преподавателей для конкретного потока фиксируем до заключения договора.</p></div><div class="school-team-grid"><article class="team-card"><div class="team-card-header"><div class="team-portrait"><img src="/assets/team/danil-usik.jpg" alt="Данил Усик" width="64" height="64" loading="lazy" decoding="async"></div><div class="team-card-heading"><span class="team-role">Основатель · бизнес-обучение</span><h3>Данил Усик</h3></div></div><div class="team-card-body"><p>Данил больше 10 лет занимается B2B-продажами и развитием бизнеса, работает с группами. В программе координирует диагностику и подготовку.</p><a class="card-link" href="https://www.linkedin.com/in/danielusik/" target="_blank" rel="noopener noreferrer">Профиль в LinkedIn ↗</a></div></article><article class="team-card"><div class="team-card-header"><div class="team-portrait"><img src="/assets/team/svetlana-galakhova.jpg" alt="Светлана Галахова" width="64" height="64" loading="lazy" decoding="async"></div><div class="team-card-heading"><span class="team-role">Стратегия ИИ · практические занятия</span><h3>Светлана Галахова</h3></div></div><div class="team-card-body"><p>Сооснователь AIHUB.WORKS и практик внедрения ИИ. Помогает превращать сложные идеи об ИИ в понятные рабочие решения и ведёт практические занятия.</p><a class="card-link" href="https://www.linkedin.com/in/svetlana-galakhova/" target="_blank" rel="noopener noreferrer">Профиль в LinkedIn ↗</a></div></article><article class="team-card"><div class="team-card-header"><div class="team-portrait"><img src="/assets/team/julia-krylova.jpg" alt="Юлия Крылова" width="64" height="64" loading="lazy" decoding="async"></div><div class="team-card-heading"><span class="team-role">Маркетинг · развитие бизнеса</span><h3>Юлия Крылова</h3></div></div><div class="team-card-body"><p>Опыт в финтехе, блокчейне и электронной коммерции: маркетинг, привлечение инвестиций и общение с инвесторами.</p><a class="card-link" href="https://www.linkedin.com/in/juliakrl/" target="_blank" rel="noopener noreferrer">Профиль в LinkedIn ↗</a></div></article></div></div></section>

<section class="section school-faq" id="faq"><div class="wrap"><div class="section-head"><div><span class="eyebrow">Перед стартом программы</span><h2>Частые вопросы</h2></div><p>Ответы о формате, содержании занятий и работе с материалами школы.</p></div><div class="school-faq-grid"><details><summary>Как вы работаете с данными школы?</summary><p>Для упражнений используем синтетические или обезличенные данные. Если нужны материалы школы, заранее согласуем их состав и сервисы; Практика проходит без личных данных учащихся.</p></details><details><summary>Какой технический опыт нужен для занятий?</summary><p>Можно начать без технического опыта: выберем рабочую задачу и освоим нужные инструменты по шагам.</p></details><details><summary>Что делать, если сотрудники уже используют ChatGPT?</summary><p>Опыт работы с ChatGPT поможет двигаться быстрее. На занятиях сотрудники учатся создавать помощников для задач школы, проверять ответы и повторно использовать удачные решения.</p></details><details><summary>Можно ли обучать учителей, руководство и администрацию одновременно?</summary><p>Да. После диагностики распределим участников по ролям и задачам, затем составим расписание потоков.</p></details><details><summary>Как вы учитываете предмет и возраст учащихся?</summary><p>Подбираем задания с учётом предмета, возраста и требований школы. Для практики используем синтетические и обезличенные материалы или заранее согласованные примеры.</p></details><details><summary>На каком языке проходят занятия?</summary><p>Язык программы согласуем при подготовке и подтвердим до начала занятий.</p></details><details><summary>Сколько времени займёт обучение?</summary><p>За четыре недели участник проходит 8 часов онлайн-занятий и посвящает около 10 часов практике на своих задачах.</p></details><details><summary>Когда участники выполняют практические задания?</summary><p>Участники практикуются на задачах из своей работы. Расписание и нагрузку согласуем со школой заранее.</p></details><details><summary>Кто отвечает за качество материалов?</summary><p>Сотрудник проверяет черновик ИИ по согласованным критериям. Педагог принимает решение об учебных материалах, а руководитель — об управленческих выводах.</p></details><details><summary>Что школа получит по итогам?</summary><p>По итогам школа получит индивидуальные оценки навыков участников, помощников, созданных ими во время обучения, учебные материалы, описание рабочих сценариев и рекомендации. Права на материалы зафиксируем в договоре.</p></details><details><summary>Какую поддержку участники получают во время практики?</summary><p>Участникам, которые посещают занятия и выполняют практику, поможем довести помощника до рабочего прототипа в пределах заранее согласованного объёма. Школа организует участие сотрудников в занятиях.</p></details><details><summary>Будут ли созданные помощники работать после обучения?</summary><p>Участники получат инструкции, чтобы повторить и изменить сценарий. Дальнейшая работа помощника зависит от выбранного сервиса и лицензии.</p></details><details><summary>Нужны ли платные лицензии?</summary><p>До начала выберем сервисы и уточним, какие подписки нужны. Расходы на них отдельно укажем в предложении.</p></details><details><summary>Когда начинаются занятия?</summary><p>Планируем начать примерно через месяц после подписания договора, предоплаты и получения материалов от школы. Онлайн-программа длится четыре недели.</p></details><details><summary>Можно ли пройти обучение очно?</summary><p>Основная программа проходит онлайн. Очное обучение в вашей школе обсуждаем отдельно. Стоимость рассчитываем индивидуально — с учётом программы и места проведения.</p></details></div></div></section>

<section class="section school-pricing-section" id="pricing"><div class="wrap school-pricing-grid"><div><span class="eyebrow">Стоимость программы</span><h2>Стоимость обучения команды школы</h2><p>Диагностика стоит €2 000. Если школа заключит договор на обучение, зачтём эту сумму в стоимость программы. Ориентир стоимости программы — $700 за каждого сотрудника, который участвует в обучении. Итоговая стоимость зависит от состава команды и числа потоков. Точный расчёт подготовим после диагностики.</p><a class="school-download-link school-download-link--dark" href="/assets/downloads/practical-ai-school-program.pdf" download>Скачать программу (PDF) ↓</a></div><div class="school-price-card"><span>Ориентир для одного сотрудника</span><strong>$700</strong><ul><li>программа практики под задачи участников;</li><li>8 часов онлайн-занятий на участника;</li><li>около 10 часов самостоятельной практики на задачах сотрудников;</li><li>обратная связь, итоговая оценка и демонстрация результата;</li><li>передача материалов и рекомендаций в объёме, закреплённом договором.</li></ul><p>Состав участников, число потоков, язык занятий, объём поддержки, налоги и график оплаты зафиксируем в предложении.</p></div></div></section>

<section class="closing school-closing" id="contact"><div class="wrap school-contact-layout"><div class="closing-copy"><span class="eyebrow">Следующий шаг</span><h2>Обсуждаем программу повышения квалификации для вашей школы.</h2><p>На встрече уточним роли участников, язык обучения и сроки. После диагностики подготовим предложение с количеством потоков, форматом поддержки и общей стоимостью.</p></div><form class="school-intake-form" id="school-intake-form"><label>Название школы<input name="school" autocomplete="organization" required placeholder="Например, школа ..."></label><label>Сколько сотрудников планируют участвовать?<input name="participants" type="number" min="1" inputmode="numeric" placeholder="Примерное количество"></label><label>Какие сотрудники будут учиться?<input name="roles" placeholder="Учителя, руководители, администрация"></label><label>На каком языке удобно учиться?<input name="language" placeholder="Укажите язык"></label><label>Когда хотели бы начать?<input name="start" placeholder="Месяц или ориентировочная дата"></label><div class="school-form-actions"><button class="button button--dark" type="submit" name="intent" value="Связаться с командой Practical AI">Связаться с командой Practical AI</button></div><p class="school-cta-status">WhatsApp откроет черновик сообщения с вашими ответами. Вы сможете проверить его и отправить.</p></form></div></section>


<div class="school-sticky-cta"><a class="button button--dark" href="#contact">Связаться с командой Practical AI</a></div>
<script>
(() => {
  const stickyCta = document.querySelector('.school-sticky-cta');
  const schoolHero = document.querySelector('.school-hero');
  if (stickyCta && schoolHero && 'IntersectionObserver' in window) {
    const observer = new IntersectionObserver(([entry]) => {
      stickyCta.classList.toggle('is-visible', !entry.isIntersecting);
    });
    observer.observe(schoolHero);
  } else if (stickyCta) {
    stickyCta.classList.add('is-visible');
  }
  const form = document.getElementById('school-intake-form');
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const data = new FormData(form);
    const intent = event.submitter?.value || 'Обсудить программу';
    const message = [
      'Здравствуйте! Хочу обсудить обучение команды школы работе с ИИ за четыре недели.',
      `Запрос: ${intent}.`,
      `Школа: ${data.get('school') || 'уточним на встрече'}.`,
      `Участники: ${data.get('participants') || 'уточним на встрече'}.`,
      `Роли: ${data.get('roles') || 'уточним на встрече'}.`,
      `Предпочтительный язык: ${data.get('language') || 'согласуем'}.`,
      `Желаемый старт: ${data.get('start') || 'обсудим'}.`,
      'Формат: один учебный поток или программа для всей школы. Число потоков определим после диагностики.'
    ].join('\\n');
    const url = `https://wa.me/__WHATSAPP_NUMBER__?text=${encodeURIComponent(message)}`;
    window.open(url, '_blank', 'noopener,noreferrer');
  });
})();
</script>'''.replace("__WHATSAPP_NUMBER__", WHATSAPP_NUMBER)


def school_program_download() -> str:
    return '''<!doctype html><html lang="ru"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Программа повышения квалификации команды школы | Practical AI</title><style>
@page{size:A4;margin:14mm}*{box-sizing:border-box}body{margin:0;color:#1b2944;font-family:Arial,Helvetica,sans-serif;font-size:10pt;line-height:1.45}.sheet{max-width:180mm;margin:0 auto}.brand{display:flex;align-items:center;justify-content:space-between;margin-bottom:9mm;color:#65738a;font-size:9pt}.brand b{color:#1b2944;font-size:12pt}.tag{padding:5px 9px;border:1px solid #d9e1ea;border-radius:999px;font-size:8pt}h1{max-width:160mm;margin:0 0 4mm;font-size:26pt;line-height:1.08;letter-spacing:-.035em}.lead{max-width:158mm;margin:0;color:#53627a;font-size:12pt;line-height:1.45}.facts{display:grid;grid-template-columns:repeat(3,1fr);gap:8px;margin:7mm 0;padding:12px;border-radius:12px;background:#1b2944;color:#fff}.fact strong,.fact span{display:block}.fact strong{color:#f4d447;font-size:15pt;line-height:1.1}.fact span{margin-top:4px;color:#d7e0eb;font-size:8pt}.section{margin-top:6mm}.section h2{margin:0 0 3mm;font-size:15pt;line-height:1.2}.roles,.examples{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.card{padding:10px 11px;border:1px solid #dce4ed;border-radius:10px;background:#f8fafc}.card b{display:block;margin-bottom:4px;font-size:9pt}.card p{margin:0;color:#59677b;font-size:8.5pt}.examples{grid-template-columns:repeat(2,1fr)}.flow{display:grid;grid-template-columns:repeat(2,1fr);gap:8px}.step{display:flex;gap:8px;padding:9px 10px;border:1px solid #dce4ed;border-radius:9px}.num{flex:0 0 24px;display:grid;place-items:center;width:24px;height:24px;border-radius:7px;background:#f4d447;font-size:8pt;font-weight:700}.step b{display:block;margin-bottom:2px;font-size:9pt}.step p{margin:0;color:#59677b;font-size:8.5pt}.checks{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.assessment{break-before:page}.people{display:grid;grid-template-columns:repeat(3,1fr);gap:8px}.person{padding:9px 10px;border-radius:9px;background:#f3f6f9}.person b{display:block;margin-bottom:3px;font-size:9pt}.person span{display:block;color:#59677b;font-size:8pt}.price{margin-top:7mm;padding:13px 15px;border:1px solid #d5deea;border-radius:12px;background:#f3f6f9;color:#1b2944;break-inside:avoid}.price h2{margin:0 0 5px;color:#1b2944;font-size:15pt}.price-grid{display:grid;grid-template-columns:1fr 1fr;gap:10px}.price strong{color:#806b09;font-size:17pt}.price p{margin:4px 0;color:#46556b;font-size:8.5pt}.foot{margin-top:6mm;padding-top:4mm;border-top:1px solid #dce4ed;color:#46556b;font-size:8.5pt}.foot a{color:#1b2944;text-decoration:none}.print{position:fixed;right:18px;bottom:18px;border:0;border-radius:999px;padding:12px 17px;background:#1b2944;color:#fff;font:700 13px Arial,sans-serif;cursor:pointer}@media print{.print{display:none}.sheet{max-width:none}.section,.card,.step,.person{break-inside:avoid}}
</style></head><body><main class="sheet"><div class="brand"><b>Practical AI</b><span class="tag">Для частных школ</span></div><h1>За четыре недели участники создают и проверяют ИИ-помощников для своих задач.</h1><p class="lead">Практическая программа повышения квалификации учителей, руководителей и административной команды школы. Онлайн-занятия и практика строятся вокруг задач сотрудников.</p><div class="facts"><div class="fact"><strong>4 недели</strong><span>занятий и практики</span></div><div class="fact"><strong>8 часов</strong><span>онлайн-занятий на участника</span></div><div class="fact"><strong>около 10 часов</strong><span>самостоятельной практики</span></div></div><section class="section"><h2>У каждой роли свои задачи для работы с ИИ</h2><div class="roles"><div class="card"><b>Учителя</b><p>Подготовка заданий, вариантов объяснений и критериев оценки; черновики обратной связи.</p></div><div class="card"><b>Руководители учебной части</b><p>Методические материалы, учебная документация и разбор обезличенных данных.</p></div><div class="card"><b>Руководство и администрация</b><p>Сводки, документы, вопросы к совещаниям и подготовка управленческих решений.</p></div></div></section><section class="section"><h2>Примеры рабочих задач</h2><div class="examples"><div class="card"><b>Для учителя · задания о круговороте воды</b><p>ИИ готовит три варианта задания для 5-го класса. Педагог сверяет содержание с темой урока и программой.</p></div><div class="card"><b>Для директора · записка к обсуждению бюджета</b><p>ИИ составляет вопросы к совещанию по данным таблицы. Руководитель проверяет суммы и учитывает контекст.</p></div></div></section><section class="section"><h2>Как проходит программа</h2><div class="flow"><div class="step"><span class="num">01</span><div><b>Диагностика задач школы</b><p>Интервью и опрос сотрудников, карта процессов и приоритетные задачи.</p></div></div><div class="step"><span class="num">02</span><div><b>Подготовка программы</b><p>Формируем группы, выбираем задачи для практики, сервисы, расписание и критерии.</p></div></div><div class="step"><span class="num">03</span><div><b>Четыре недели обучения</b><p>Участники выбирают задачу, создают помощника, проверяют его и показывают команде.</p></div></div><div class="step"><span class="num">04</span><div><b>Оценка результата</b><p>Проверяем, может ли участник повторить процесс и применить помощника на рабочем примере.</p></div></div></div></section><section class="section assessment"><h2>Как оцениваем результат</h2><p class="check">Каждый участник показывает помощника на примере своей задачи и объясняет, как проверяет его ответы.</p><div class="checks"><div class="card"><b>Навыки участников</b><p>Школа получает индивидуальную оценку того, что сотрудник может сделать самостоятельно.</p></div><div class="card"><b>Рабочие материалы</b><p>Помощники, описания сценариев и рекомендации для дальнейшей практики.</p></div><div class="card"><b>Изменения в работе</b><p>Критерии выбираем заранее: время выполнения, качество результата и нагрузка команды.</p></div></div></section><section class="section"><h2>Кто работает с командой</h2><div class="people"><div class="person"><b>Данил Усик</b><span>Координирует диагностику и подготовку программы. Более 10 лет опыта в B2B-продажах и развитии бизнеса.</span></div><div class="person"><b>Светлана Галахова</b><span>Сооснователь AIHUB.WORKS, практик внедрения ИИ и ведущая практических занятий.</span></div><div class="person"><b>Юлия Крылова</b><span>Опыт в финтехе, блокчейне и электронной коммерции: маркетинг, инвестиции и деловые коммуникации.</span></div></div></section><section class="price"><h2>Стоимость</h2><div class="price-grid"><div><strong>$700</strong><p>Ориентир за одного участника. Итог зависит от состава команды и числа потоков.</p></div><div><strong>€2 000</strong><p>Диагностика школы. Если школа заключит договор на обучение, стоимость диагностики зачтём в стоимость программы.</p></div></div></section><div class="foot">Занятия проходят онлайн. Очное обучение обсуждаем отдельно; его стоимость рассчитываем индивидуально. Практика проходит без личных данных учащихся; для упражнений используем синтетические или обезличенные данные. Сервисы, график, состав команды и условия закрепим в предложении.<br><a href="https://practical-ai.pro/ru/for-schools/">practical-ai.pro/ru/for-schools/</a></div></main><button class="print" onclick="window.print()">Сохранить как PDF</button></body></html>'''

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
    return f'<section class="closing" id="contact"><div class="wrap closing-inner"><div class="closing-copy"><span class="eyebrow">{esc(c["closing_eyebrow"])}</span><h2>{esc(c["closing_h2"])}</h2><p>{esc(c["closing_p"])}</p></div><div class="contact-card"><div class="contact-person"><img src="/assets/team/danil-usik.jpg" alt="{name}" width="64" height="64" loading="lazy"><div><strong>{name}</strong><span>{esc(c["contact_role"])}</span></div></div><a class="button button--dark" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c["closing_cta"])} ↗</a><div class="contact-alternatives"><a href="{contact(lang,channel='linkedin')}" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div></div></section>'


def team_section(lang: str) -> str:
    c = COPY[lang]
    cards = []
    for index, member in enumerate(TEAM_PROFILES):
        name = member["name"] if lang == "en" else member["ru_name"]
        linkedin_label = f"View {name} on LinkedIn" if lang == "en" else f"Профиль {name} в LinkedIn"
        cards.append(f'<article class="team-card"><div class="team-card-header"><div class="team-portrait"><img src="/assets/team/{member["photo"]}" alt="{name}" width="64" height="64" loading="lazy" decoding="async"></div><div class="team-card-heading"><span class="team-role">{esc(c["team_roles"][index])}</span><h3>{name}</h3></div></div><div class="team-card-body"><p>{esc(c["team_bios"][index])}</p><a class="card-link" href="{member["linkedin"]}" aria-label="{linkedin_label}" target="_blank" rel="noopener noreferrer">LinkedIn <span aria-hidden="true">↗</span></a></div></article>')
    return f'<section class="section team-section" id="team"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c["team_eyebrow"])}</span><h2>{esc(c["team_h2"])}</h2></div><p>{esc(c["team_p"])}</p></div><div class="team-cards">{"".join(cards)}</div><div class="team-next"><a class="card-link" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c["team_link"])} ↗</a></div></div></section>'


def evidence_teaser(lang: str) -> str:
    c = COPY[lang]
    label = "Explore the team case and participant quotes" if lang == "en" else "Посмотреть результаты кейса и слова участников"
    quote_text, quote_name, quote_role = c["quotes"][0]
    return f'<section class="section evidence-teaser"><div class="wrap evidence-teaser-grid"><div><span class="eyebrow">{esc(c["proof_tag"])}</span><h2>{esc(c["proof_h2"])}</h2><p>{esc(c["proof_p"])}</p><a class="card-link" href="{u(lang)}#case">{esc(label)} →</a></div><figure><blockquote>“{esc(quote_text)}”</blockquote><figcaption>{esc(quote_name)} · {esc(quote_role)}</figcaption></figure></div></section>'


def school_home_teaser(lang: str) -> str:
    c = COPY[lang]
    link_attributes = ' lang="ru" hreflang="ru"' if lang == "en" else ""
    return f'<section class="section school-home-teaser" id="school-program"><div class="wrap school-home-teaser-grid"><div><span class="eyebrow">{esc(c["school_teaser_eyebrow"])}</span><h2>{esc(c["school_teaser_h2"])}</h2><p>{esc(c["school_teaser_p"])}</p></div><aside class="school-home-teaser-card"><strong>{esc(c["school_teaser_stat"])}</strong><span>{esc(c["school_teaser_stat_detail"])}</span><a class="button button--dark" href="/ru/for-schools/"{link_attributes}>{esc(c["school_teaser_cta"])} ↗</a></aside></div></section>'


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
    return f'''<section class="hero"><div class="wrap hero-grid"><div><span class="eyebrow">{esc(c['hero_eyebrow'])}</span><h1>{c['hero_h1']}</h1><p class="hero-lede">{esc(c['hero_lede'])}</p><div class="hero-actions"><a class="button" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(c['hero_cta'])} ↗</a><a class="button button--ghost" href="#programs">{esc(c['hero_secondary'])} ↓</a></div><p class="hero-note">{esc(c['hero_note'])}</p><div class="hero-contact-options"><a href="{contact(lang,channel='linkedin')}" target="_blank" rel="noopener noreferrer">{esc(c['linkedin_alt'])} ↗</a><a href="#team">{esc(c['hero_team'])} ↓</a></div></div><div class="flow-card"><div class="flow-top"><span>{esc(c['flow_top'])}</span><span>● {esc(c['flow_status'])}</span></div>{steps}<div class="flow-output"><b>{esc(c['flow_output'])}</b> · {esc(c['flow_output_text'])}</div></div></div></section>
<section class="section programs" id="programs"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['programs_eyebrow'])}</span><h2>{esc(c['programs_h2'])}</h2></div><p>{esc(c['programs_intro'])}</p></div>{program_cards(lang)}</div></section>
{school_home_teaser(lang)}
<section class="section proof" id="case"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['proof_eyebrow'])}</span><h2>{esc(c['proof_h2'])}</h2></div><p>{esc(c['proof_p'])}</p></div><div class="case-layout"><div class="case-story"><div class="case-company"><img src="/assets/img/shildpanel-mark.svg" alt="" width="70" height="76" loading="lazy"><div><strong>ShildPanel</strong><span>Production Company</span></div></div><span class="case-story-number">5<span> / {esc(c['proof_count_unit'])}</span></span><h3>{esc(c['proof_case_h3'])}</h3><p>{esc(c['proof_roles'])}</p><a class="card-link" href="#reviews">{esc(c['proof_case_link'])} →</a></div><div class="proof-panel"><span class="case-tag">{esc(c['proof_tag'])}</span><h3>{esc(c['proof_title'])}</h3><div class="proof-facts">{proof_facts}</div></div></div></div></section>
<section class="section quotes" id="reviews"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['quotes_eyebrow'])}</span><h2>{esc(c['quotes_h2'])}</h2></div><p>{esc(c['quotes_intro'])}</p></div><div class="quote-grid">{quotes}</div></div></section>
{team_section(lang)}
<section class="section method"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['method_eyebrow'])}</span><h2>{esc(c['method_h2'])}</h2></div><p>{esc(c['method_intro'])}</p></div><div class="method-grid">{method}</div>{method_visual(lang)}</div></section>
<section class="section"><div class="wrap"><div class="section-head"><div><span class="eyebrow">{esc(c['guides_eyebrow'])}</span><h2>{esc(c['guides_h2'])}</h2></div></div><div class="guide-grid">{guides}</div></div></section>{closing(lang)}'''


def page_hero(lang: str, eyebrow: str, h1: str, intro: str) -> str:
    return f'<section class="page-hero"><div class="wrap"><span class="eyebrow">{esc(eyebrow)}</span><h1>{esc(h1)}</h1><p>{esc(intro)}</p><a class="button" href="{contact(lang)}" target="_blank" rel="noopener noreferrer">{esc(COPY[lang]["discuss"])} ↗</a><div class="page-contact-options"><a href="{contact(lang,channel='linkedin')}" target="_blank" rel="noopener noreferrer">{esc(COPY[lang]["linkedin_alt"])} ↗</a></div></div></section>'


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
    school_target = DOCS / "ru" / "for-schools" / "index.html"
    school_target.parent.mkdir(parents=True, exist_ok=True)
    school_target.write_text(shell("ru", "for-schools", school_page()) + "\n", encoding="utf-8")
    school_program_target = DOCS / "assets" / "downloads" / "practical-ai-school-program.html"
    school_program_target.parent.mkdir(parents=True, exist_ok=True)
    school_program_target.write_text(school_program_download() + "\n", encoding="utf-8")
    sitemap = DOCS / "sitemap.xml"
    text = sitemap.read_text(encoding="utf-8")
    for lang in ("en", "ru"):
        for route in page_makers:
            url = BASE + u(lang,route)
            if f"<loc>{url}</loc>" not in text:
                text = text.replace("</urlset>", f"  <url><loc>{url}</loc></url>\n</urlset>")
    school_url = BASE + u("ru", "for-schools")
    if f"<loc>{school_url}</loc>" not in text:
        text = text.replace("</urlset>", f"  <url><loc>{school_url}</loc></url>\n</urlset>")
    sitemap.write_text(text, encoding="utf-8")
    print("Built nine sales-led static pages and updated sitemap")


if __name__ == "__main__":
    main()
