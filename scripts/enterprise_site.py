"""Bilingual enterprise AI adoption homepage and case copy for Practical AI."""
from __future__ import annotations

from html import escape
from urllib.parse import quote


BASE = "https://practical-ai.pro"
CASES = ("shildpanel", "kerama-marazzi")

COPY = {
    "en": {
        "meta": ("Enterprise AI Adoption & Business Transformation | Practical AI",
                 "Build lasting AI capabilities across your business. Discover high-value workflows, develop internal AI champions and measure operational improvements. Start with a 2–3 week assessment."),
        "switch": "RU", "switch_label": "Switch language to Russian", "home_label": "Practical AI home",
        "nav": [("#cases", "Results"), ("#method", "Approach"), ("#roadmap", "Roadmap"), ("#security", "Security"), ("#assessment", "Assessment")],
        "cta": "Discuss the assessment", "menu": "Menu", "skip": "Skip to main content",
        "eyebrow": "Enterprise AI adoption · Practical AI",
        "h1": "Turn AI into a working capability across your company.",
        "lede": "We help business teams identify valuable opportunities, test practical workflows and build the internal capability to keep improving them.",
        "hero_note": "Start with real processes. Agree on boundaries. Measure what changes.",
        "hero_cta": "Discuss the AI assessment", "hero_secondary": "See how we work",
        "hero_team_label": "A DELIVERY TEAM BUILT AROUND YOUR WORK",
        "hero_team_context": "Three perspectives. One practical outcome.",
        "hero_team_statement": "One shared goal: practical AI in everyday processes.",
        "hero_team_roles": [
            ("Business teams", "Priorities · process expertise"),
            ("Practical AI", "Workflow design · implementation"),
            ("IT & Security", "Tools · data · controls")],
        "hero_team_footer": "Shared roadmap · clear owners · measured progress",
        "team_contact_title": "Practical AI delivery team",
        "team_contact_subtitle": "AI strategy · workflows · adoption",
        "hero_badge": "Independent first step", "hero_fee": "€5,000", "hero_duration": "2–3 weeks",
        "hero_scope": "A bounded assessment, with a decision point before any next phase.",
        "pain_eyebrow": "From access to adoption", "pain_title": "Teams already have tasks for AI. The work is building a reliable way to improve them.",
        "pain_intro": "Useful adoption connects day-to-day work, employee capability and the company’s technical and governance boundaries.",
        "pains": [
            ("Repetitive work absorbs skilled time", "Teams compile reports, search across documents and repeat routine coordination every week."),
            ("Useful discoveries stay in separate teams", "Employees experiment independently, while similar workflows get rebuilt and lessons remain hard to share."),
            ("Learning needs a route into daily work", "Adoption grows through real processes, agreed tools, review criteria, clear ownership and follow-through.")],
        "outcomes_eyebrow": "What stays inside your company", "outcomes_title": "Build a repeatable way to improve work with AI.",
        "outcomes_intro": "The work leaves teams with reviewed practices they can use, adapt and improve after the engagement.",
        "outcomes": [
            ("Workflows", "Tested steps for agreed business processes."),
            ("People", "Employees who use approved tools and review the output."),
            ("Ownership", "Internal champions with a defined role and escalation path."),
            ("Reusable knowledge", "Workflow cards, instructions and quality criteria."),
            ("Measurement", "Baselines and follow-up measures for selected processes.")],
        "cases_eyebrow": "Evidence from client work", "cases_title": "Real tasks. Reported outcomes.",
        "cases_intro": "The examples below come from client interviews and project information. They describe specific work in those organisations; each new engagement starts with its own baseline.",
        "case_source": "Reported interview results · task-specific examples",
        "kerama_source": "Programme information · client case",
        "case_shildpanel": "ShildPanel", "case_shild_sub": "Practical AI in production and support workflows",
        "case_shild_desc": "Interview figures from four operational examples across reporting, ERP work, competitor analysis and HR.",
        "shild_metrics": [
            ("Production report", "8 hours", "15 minutes", "Time reported for preparing a production report."),
            ("ERP formulas", "12 hours", "30 minutes", "Time reported for the ERP formula task."),
            ("Competitor analysis", "7 days", "Under 6 hours", "Time reported for a competitor analysis."),
            ("HR routine", "", "About 30 minutes a day", "Daily HR administrative time reported as released." )],
        "case_kerama": "Kerama Marazzi", "case_kerama_sub": "Building internal AI trainers through Train-the-Trainer",
        "case_kerama_desc": "A programme that developed internal capacity through training, mentoring and practical cases.",
        "kerama_metrics": [("4", "internal AI trainers prepared"), ("70 days", "of training and mentoring"), ("50+", "practical cases explored"), ("80 colleagues", "potential reach")],
        "reach_note": "The figure of 80 describes potential reach. The case information reports a potential audience, not 80 confirmed active users.",
        "case_link": "Read the case details", "case_note": "These task-level results are examples, not forecasts or guaranteed outcomes for another organisation.",
        "method_eyebrow": "How the work moves", "method_title": "From a useful experiment to an everyday business practice.",
        "method_intro": "Each workflow connects a process owner, an AI step, human review and a measurable next action.",
        "steps": [
            ("01", "Discover opportunities", "Interview process owners and employees, map recurring work, and record technical, data and governance constraints."),
            ("02", "Build and test workflows", "Work with employees on real tasks using tools and data boundaries agreed with the client."),
            ("03", "Develop internal champions", "Prepare selected employees to support colleagues, share reviewed practices and escalate issues to the right owner."),
            ("04", "Make knowledge reusable", "Document inputs, expected outputs, quality checks, owners and conditions for use."),
            ("05", "Measure and improve", "Compare agreed baseline and follow-up measures, review regular use and select the next improvement.")],
        "method_caption": "A continuous improvement cycle designed to operate inside the organisation.",
        "roadmap_eyebrow": "A staged route", "roadmap_title": "A clear decision after every phase.",
        "roadmap_intro": "Scope, timing and investment for implementation follow the assessment and the client’s approvals.",
        "phases": [
            ("Phase 0", "AI Opportunity & Readiness Assessment", "2–3 weeks · €5,000", "Interview relevant leaders and employees, review selected processes, capture IT and Security boundaries, assess readiness and prioritise opportunities.", "Opportunity Map · Readiness & Risk · preliminary business case · proposed 12-month roadmap", "Decide whether to proceed, which opportunities to test and at what scale."),
            ("Phase 1", "Validate selected opportunities", "First month · scoped after assessment", "Test agreed workflows with small pilot groups and compare results with the starting point. A first measurable pilot outcome can be planned around week four, subject to approvals, data access and process readiness.", "Pilot evidence · updated assumptions · decision on the next phase", "Confirm scope and the evidence needed to continue."),
            ("Phase 2", "Establish repeatable adoption", "Months 2–3 · scope agreed separately", "Extend validated practices, prepare internal champions and build a reviewed workflow library.", "Reusable practices · internal owners · adoption measures", "Select teams and practices for wider use."),
            ("Phase 3", "Scale across functions", "Months 4–6 · scope agreed separately", "Expand suitable practices with business owners and IT, then review adoption and operational effects by function.", "Function-level adoption view · updated priorities", "Choose the next areas using observed evidence."),
            ("Phase 4", "Build company independence", "Months 7–12 · scope agreed separately", "Transfer the discovery and prioritisation method, clarify ownership and establish a routine for reviewing the workflow library.", "Internal operating rhythm · ownership · improvement backlog", "Continue the cycle under the company’s own direction.")],
        "roadmap_decision": "Decision point", "roadmap_outputs": "Typical outputs", "open_phase": "Open phase details",
        "map_eyebrow": "Illustrative example", "map_title": "How an Opportunity Map compares work before investment.",
        "map_label": "Illustrative examples — potential benefits and complexity are hypotheses until the assessment validates them.",
        "map_headers": ["Function", "Opportunity", "Potential benefit", "Complexity", "Possible next step"],
        "map_rows": [
            ("HR", "Employee policy assistant", "Fewer repeated policy questions", "Medium", "Pilot with HR and IT review"),
            ("Finance", "Reporting preparation support", "Less manual consolidation", "Medium", "Workflow pilot with expert review"),
            ("Marketing", "Competitor monitoring", "Less manual research", "Low", "Employee-led test"),
            ("Support", "Ticket classification", "Faster initial triage", "High", "Technical assessment"),
            ("Operations", "Weekly performance report", "Less manual collation", "Medium", "Workflow pilot")],
        "map_cta": "Discuss your Opportunity Map",
        "calc_eyebrow": "Interactive estimate", "calc_title": "Explore the capacity a changed workflow could release.",
        "calc_intro": "Adjust the assumptions to see an illustrative annual capacity estimate for one workflow.",
        "calc_fields": [("users", "Team members using the workflow", "100", "1", "10000", "1"),
                        ("adoption", "Estimated regular use", "60", "0", "100", "1"),
                        ("hours", "Hours per person each week", "2", "0.1", "80", "0.1"),
                        ("weeks", "Working weeks per year", "44", "1", "52", "1"),
                        ("hourly", "Optional loaded hourly cost (€)", "40", "0", "1000", "1")],
        "capacity_label": "Potential capacity per year", "value_label": "Illustrative labour-value equivalent",
        "calc_note": "Illustrative capacity estimate. The monetary figure is a labour-value equivalent, not a forecast of savings, revenue or ROI. Actual value depends on adoption, quality, implementation and support costs, errors, and how released capacity is used.",
        "security_eyebrow": "Security, IT and governance", "security_title": "Adoption stays within agreed business and technical boundaries.",
        "security_intro": "The assessment identifies constraints and decisions for selected workflows. The client’s authorised owners retain approval of tools, data access and controls.",
        "owners": [("Business owner", "Sets the priority, process outcome and operational acceptance criteria."),
                   ("IT and Security", "Approve tools, access, data boundaries and technical controls."),
                   ("Legal and risk owners", "Review obligations and approve the applicable policy boundaries."),
                   ("Practical AI", "Maps workflows, documents assumptions and works to the client’s agreed review criteria.")],
        "security_note": "The assessment supports internal decisions; compliance certification, security products and technical integrations require separate specialist scope.",
        "measure_eyebrow": "Measurement", "measure_title": "Measure each initiative against its own starting point.",
        "measures": ["Time spent on a defined process", "Output quality against agreed criteria", "Regular use and rework", "Employee confidence", "Reviewed workflows in active use"],
        "measure_note": "The assessment agrees relevant KPIs, baselines, data sources and review methods. Targets follow from the selected process and available evidence.",
        "assessment_eyebrow": "A bounded first decision", "assessment_title": "AI Opportunity & Readiness Assessment",
        "assessment_price": "€5,000", "assessment_duration": "2–3 weeks",
        "assessment_intro": "A focused assessment of selected functions and processes. The interview sample and process depth are agreed with your sponsor before work begins.",
        "scope_title": "What the assessment includes", "scope": [
            "Interviews across up to eight agreed functions, with selected leaders and employees", "A short employee survey and review of selected recurring processes", "IT, Security and governance constraints for the selected workflows", "Screening of 10–15 candidate initiatives and prioritisation of 3–5", "Opportunity Map and Readiness & Risk assessment", "Preliminary business case with explicit assumptions", "Proposed 12-month roadmap and executive decision session"],
        "inputs_title": "Client inputs", "inputs": ["An executive sponsor and process owners", "Interview access and available process information", "IT and Security participation on tools, data and feasibility", "Timely feedback on assumptions and findings"],
        "offer_note": "The fee covers the assessment. Implementation, training, integrations and later phases receive a separate scope and agreement. The company decides whether to continue after the assessment.",
        "form_title": "Discuss the assessment", "form_intro": "Share a little context. The fields prepare a message for WhatsApp so you can review it before sending.",
        "form_company": "Company", "form_email": "Work email", "form_role": "Your role (optional)",
        "form_process": "Which process would you like to improve? (optional)", "form_submit": "Prepare WhatsApp message",
        "form_disclosure": "This website does not submit or store the form. It opens WhatsApp with a draft; you review and send the message there.",
        "form_status": "WhatsApp will open with your draft. Review the details and send it there.",
        "faq_eyebrow": "Questions leaders ask", "faq_title": "What to expect from the first step.",
        "faq": [
            ("Is this a training programme?", "The assessment starts with business processes, readiness and constraints. Its findings can point to training, a workflow pilot, technical discovery, governance work or another next step."),
            ("Do we need to choose AI tools first?", "The assessment records your current stack and IT and Security boundaries. Tool choices follow the process, risk and feasibility review."),
            ("What happens after 2–3 weeks?", "You receive the assessment outputs and a decision session. Your company can continue internally or agree a separate next phase with Practical AI."),
            ("Can you guarantee savings or ROI?", "The work establishes baselines, tests assumptions and records observed changes. Financial outcomes follow actual adoption, costs and measured use of released capacity."),
            ("Who owns security and compliance decisions?", "Your authorised IT, Security, Legal and risk owners set and approve the applicable boundaries. Practical AI documents those decisions for the selected workflows."),
            ("Can our current AI programmes continue?", "Yes. Company labs, leadership sprints and role-based programmes remain available as focused formats and supporting pages.")],
        "final_eyebrow": "Start with the work", "final_title": "Choose a first step based on the processes your teams want to improve.",
        "final_text": "A conversation can clarify the business context, functions involved and whether the assessment is a suitable first step.",
        "final_cta": "Discuss the assessment", "programs": "Explore existing programmes", "hr": "For HR & L&D", "team": "Meet the team", "guides": "Read practical guides",
        "footer": "Practical AI · Enterprise AI adoption and business transformation",
        "case_meta": {
            "shildpanel": ("ShildPanel case | Practical AI", "Interview-reported task outcomes across production reporting, ERP formulas, competitor analysis and an HR routine."),
            "kerama-marazzi": ("Kerama Marazzi case | Practical AI", "The programme prepared four internal AI trainers through 70 days of training and mentoring and explored 50+ practical cases.")},
        "case_quote": "“Now I have a playbook I can hand to my team to put into practice.”",
        "case_quote_by": "Alexander · Operations Director",
        "case_detail_note": "Results describe specific reported tasks and programme activity. They are examples for these organisations; outcomes for a new organisation depend on its process, tools, adoption and baseline.",
        "case_back": "Back to the homepage", "case_cta": "Discuss an assessment for your company",
    },
    "ru": {
        "meta": ("AI-трансформация бизнеса и внедрение AI | Practical AI",
                 "Развивайте устойчивые AI-компетенции в компании: находите ценные рабочие сценарии, готовьте внутренних AI-чемпионов и измеряйте изменения. Начните с диагностики на 2–3 недели."),
        "switch": "EN", "switch_label": "Переключить язык на английский", "home_label": "Practical AI — на главную",
        "nav": [("#cases", "Результаты"), ("#method", "Подход"), ("#roadmap", "План"), ("#security", "Безопасность"), ("#assessment", "Диагностика")],
        "cta": "Обсудить диагностику", "menu": "Меню", "skip": "Перейти к содержанию",
        "eyebrow": "AI-трансформация бизнеса · Practical AI",
        "h1": "Превратите AI в рабочую компетенцию всей компании.",
        "lede": "Помогаем бизнес-командам находить ценные возможности для AI, проверять рабочие сценарии и развивать внутреннюю способность улучшать их дальше.",
        "hero_note": "Начинаем с реальных процессов. Согласуем границы. Измеряем изменения.",
        "hero_cta": "Обсудить AI-диагностику", "hero_secondary": "Как устроена работа",
        "hero_team_label": "КОМАНДА ВОКРУГ ВАШИХ ЗАДАЧ",
        "hero_team_context": "Три перспективы. Один практический результат.",
        "hero_team_statement": "Общая цель — практический AI в ежедневных процессах.",
        "hero_team_roles": [
            ("Бизнес-команда", "Приоритеты · знание процессов"),
            ("Practical AI", "Сценарии · внедрение"),
            ("IT и Security", "Инструменты · данные · контроль")],
        "hero_team_footer": "Общий план · ясная ответственность · измеримые изменения",
        "team_contact_title": "Команда Practical AI",
        "team_contact_subtitle": "Стратегия AI · сценарии · внедрение",
        "hero_badge": "Самостоятельный первый этап", "hero_fee": "€5 000", "hero_duration": "2–3 недели",
        "hero_scope": "Ограниченный объём диагностики и решение до перехода к следующему этапу.",
        "pain_eyebrow": "От доступа к внедрению", "pain_title": "У команд уже есть задачи для AI. Важно выстроить надёжный способ улучшать их.",
        "pain_intro": "Практическое внедрение связывает ежедневную работу, компетенции сотрудников и технические и управленческие границы компании.",
        "pains": [
            ("Повторяющаяся работа занимает время специалистов", "Команды каждую неделю собирают отчёты, ищут информацию в документах и вручную координируют рутинные задачи."),
            ("Полезные находки остаются внутри отдельных команд", "Сотрудники экспериментируют самостоятельно, похожие сценарии создаются заново, а опыт сложно передавать."),
            ("Обучению нужен маршрут в ежедневную работу", "Внедрение развивается через реальные процессы, согласованные инструменты, критерии проверки, ответственность и продолжение практики.")],
        "outcomes_eyebrow": "Что остаётся в компании", "outcomes_title": "Создайте повторяемый способ улучшать работу с помощью AI.",
        "outcomes_intro": "После проекта у команд остаются проверенные практики, которые можно применять, адаптировать и развивать дальше.",
        "outcomes": [
            ("Процессы", "Проверенные сценарии для согласованных бизнес-задач."),
            ("Люди", "Сотрудники, которые работают в разрешённых инструментах и проверяют результат."),
            ("Ответственность", "Внутренние AI-чемпионы с определённой ролью и порядком эскалации."),
            ("Повторное использование", "Карточки сценариев, инструкции и критерии качества."),
            ("Измерение", "Исходные и повторные показатели для выбранных процессов.")],
        "cases_eyebrow": "Результаты работы с клиентами", "cases_title": "Реальные задачи. Результаты из интервью.",
        "cases_intro": "Примеры ниже взяты из интервью с клиентами и информации о проектах. Они описывают конкретные задачи этих компаний; для каждого нового проекта мы устанавливаем собственную исходную точку.",
        "case_source": "Результаты из интервью · отдельные примеры задач",
        "kerama_source": "Информация о программе · данные кейса",
        "case_shildpanel": "ShildPanel", "case_shild_sub": "AI в производственных и поддерживающих процессах",
        "case_shild_desc": "Данные интервью по четырём операционным примерам: отчётность, задачи в ERP, анализ конкурентов и HR.",
        "shild_metrics": [
            ("Производственный отчёт", "8 часов", "15 минут", "Время подготовки производственного отчёта по данным интервью."),
            ("Формулы в ERP", "12 часов", "30 минут", "Время выполнения задачи с формулами ERP по данным интервью."),
            ("Анализ конкурентов", "7 дней", "Менее 6 часов", "Время анализа конкурентов по данным интервью."),
            ("HR-рутина", "", "Около 30 минут в день", "По данным интервью, высвобождалось ежедневное время на HR-администрирование.")],
        "case_kerama": "Kerama Marazzi", "case_kerama_sub": "Внутренние AI-тренеры: Train-the-Trainer",
        "case_kerama_desc": "Программа развивала внутреннюю экспертизу через обучение, наставничество и практические кейсы.",
        "kerama_metrics": [("4", "подготовленных внутренних AI-тренера"), ("70 дней", "обучения и наставничества"), ("50+", "рассмотренных практических кейсов"), ("80 коллег", "потенциальный охват")],
        "reach_note": "Показатель 80 описывает потенциальный охват коллег. Это планируемая аудитория; фактическое использование AI 80 сотрудниками в кейсе не подтверждено.",
        "case_link": "Подробнее о кейсе", "case_note": "Результаты относятся к конкретным задачам и описанной программе. Это примеры работы компаний, а не прогноз или гарантированный результат для другой организации.",
        "method_eyebrow": "Как устроена работа", "method_title": "От полезного эксперимента — к повседневной практике компании.",
        "method_intro": "Каждый сценарий связывает владельца процесса, шаг с AI, проверку человеком и измеримое следующее действие.",
        "steps": [
            ("01", "Находим возможности", "Проводим интервью с владельцами процессов и сотрудниками, разбираем повторяющуюся работу, фиксируем технические и управленческие ограничения."),
            ("02", "Создаём и проверяем сценарии", "Вместе с сотрудниками работаем на реальных задачах в согласованных инструментах и границах данных."),
            ("03", "Развиваем AI-чемпионов", "Готовим выбранных сотрудников к поддержке коллег, распространению проверенных практик и передаче вопросов ответственным."),
            ("04", "Сохраняем знания для команды", "Документируем входные данные, ожидаемый результат, критерии проверки, владельца и условия применения."),
            ("05", "Измеряем и улучшаем", "Сравниваем исходные и повторные показатели, оцениваем регулярность использования и выбираем следующее улучшение.")],
        "method_caption": "Цикл постоянного улучшения, который компания развивает внутри своей системы работы.",
        "roadmap_eyebrow": "Поэтапный маршрут", "roadmap_title": "После каждого этапа — понятное решение о продолжении.",
        "roadmap_intro": "Объём, сроки и инвестиции во внедрение определяются после диагностики и согласований клиента.",
        "phases": [
            ("Этап 0", "AI Opportunity & Readiness Assessment", "2–3 недели · €5 000", "Проводим интервью с релевантными руководителями и сотрудниками, разбираем выбранные процессы, фиксируем границы IT и Security, оцениваем готовность и расставляем возможности по приоритету.", "Opportunity Map · Readiness & Risk · предварительный бизнес-кейс · проект дорожной карты на 12 месяцев", "Решение о продолжении, выборе сценариев и масштабе проверки."),
            ("Этап 1", "Проверяем выбранные возможности", "Первый месяц · объём после диагностики", "Тестируем согласованные сценарии с небольшими пилотными группами и сравниваем результат с исходной точкой. Первый измеримый результат пилота можно планировать примерно к четвёртой неделе при наличии согласований, доступа к данным и готовности процесса.", "Данные пилота · уточнённые допущения · решение о следующем этапе", "Подтверждение объёма и данных для продолжения."),
            ("Этап 2", "Выстраиваем повторяемое внедрение", "Месяцы 2–3 · отдельное согласование объёма", "Расширяем подтверждённые практики, готовим внутренних AI-чемпионов и создаём проверенную библиотеку сценариев.", "Переиспользуемые практики · внутренние владельцы · метрики внедрения", "Выбор команд и сценариев для расширения."),
            ("Этап 3", "Масштабируем между функциями", "Месяцы 4–6 · отдельное согласование объёма", "Расширяем подходящие практики вместе с владельцами процессов и IT, оцениваем применение и операционный эффект по функциям.", "Оценка внедрения по функциям · уточнённые приоритеты", "Выбор следующих областей по наблюдаемым результатам."),
            ("Этап 4", "Развиваем самостоятельность компании", "Месяцы 7–12 · отдельное согласование объёма", "Передаём метод выявления и приоритизации возможностей, закрепляем ответственность и устанавливаем порядок обновления библиотеки сценариев.", "Внутренний ритм работы · ответственность · список улучшений", "Продолжение цикла под руководством компании.")],
        "roadmap_decision": "Решение на этапе", "roadmap_outputs": "Типовые результаты", "open_phase": "Подробнее об этапе",
        "map_eyebrow": "Иллюстративный пример", "map_title": "Как сравнивать возможности до инвестиций.",
        "map_label": "Примеры для ориентира: потенциальная польза и сложность — гипотезы до проверки в ходе диагностики.",
        "map_headers": ["Функция", "Возможность", "Потенциальная польза", "Сложность", "Возможный следующий шаг"],
        "map_rows": [
            ("HR", "Помощник по политикам компании", "Меньше повторяющихся вопросов", "Средняя", "Пилот с проверкой HR и IT"),
            ("Финансы", "Подготовка отчётности", "Меньше ручной консолидации", "Средняя", "Пилот с экспертной проверкой"),
            ("Маркетинг", "Мониторинг конкурентов", "Меньше ручного поиска", "Низкая", "Тест силами сотрудников"),
            ("Поддержка", "Классификация обращений", "Быстрее первичная сортировка", "Высокая", "Техническая оценка"),
            ("Операции", "Еженедельный отчёт по показателям", "Меньше ручного сбора", "Средняя", "Пилот сценария")],
        "map_cta": "Обсудить карту возможностей",
        "calc_eyebrow": "Интерактивная оценка", "calc_title": "Посмотрите, какой ресурс может высвободить изменённый процесс.",
        "calc_intro": "Измените допущения и оцените потенциальную годовую ёмкость для одного рабочего сценария.",
        "calc_fields": [("users", "Сотрудники, использующие сценарий", "100", "1", "10000", "1"),
                        ("adoption", "Предполагаемая регулярность использования", "60", "0", "100", "1"),
                        ("hours", "Часов на человека в неделю", "2", "0.1", "80", "0.1"),
                        ("weeks", "Рабочих недель в году", "44", "1", "52", "1"),
                        ("hourly", "Полная стоимость рабочего часа (€), опционально", "40", "0", "1000", "1")],
        "capacity_label": "Потенциальная ёмкость за год", "value_label": "Иллюстративный эквивалент стоимости времени",
        "calc_note": "Иллюстративная оценка операционной ёмкости. Денежное значение показывает эквивалент рабочего времени, а не прогноз экономии, выручки или ROI. Фактическая ценность зависит от внедрения, качества, затрат на запуск и поддержку, ошибок и использования высвобождённого времени.",
        "security_eyebrow": "Безопасность, IT и управление", "security_title": "Внедрение проходит в согласованных деловых и технических границах.",
        "security_intro": "Диагностика выявляет ограничения и решения для выбранных процессов. Уполномоченные владельцы со стороны клиента утверждают инструменты, доступ к данным и меры контроля.",
        "owners": [("Владелец бизнеса", "Определяет приоритет, результат процесса и критерии его принятия."),
                   ("IT и Security", "Утверждают инструменты, доступы, границы данных и технические меры."),
                   ("Legal и владельцы рисков", "Проверяют обязательства и утверждают применимые требования."),
                   ("Practical AI", "Разбирает процессы, фиксирует допущения и работает по согласованным критериям проверки.")],
        "security_note": "Диагностика помогает принимать внутренние решения. Сертификация соответствия, security-продукты и технические интеграции требуют отдельного объёма работ.",
        "measure_eyebrow": "Измерение", "measure_title": "Сравнивайте каждую инициативу с её исходной точкой.",
        "measures": ["Время на определённый процесс", "Качество результата по согласованным критериям", "Регулярность использования и объём доработок", "Уверенность сотрудников", "Проверенные сценарии в активной работе"],
        "measure_note": "В ходе диагностики стороны согласуют релевантные KPI, исходные значения, источники данных и способ проверки. Целевые значения следуют из процесса и доступных данных.",
        "assessment_eyebrow": "Ограниченный первый шаг", "assessment_title": "AI Opportunity & Readiness Assessment",
        "assessment_price": "€5 000", "assessment_duration": "2–3 недели",
        "assessment_intro": "Фокусная диагностика выбранных функций и процессов. Состав интервью и глубину разбора согласуем со спонсором до начала работ.",
        "scope_title": "Что входит в диагностику", "scope": [
            "Интервью в пределах до восьми согласованных функций с руководителями и выбранными сотрудниками", "Короткий опрос сотрудников и разбор выбранных повторяющихся процессов", "Ограничения IT, Security и управления для выбранных сценариев", "Оценка 10–15 возможных инициатив и приоритизация 3–5", "Opportunity Map и Readiness & Risk Assessment", "Предварительный бизнес-кейс с явными допущениями", "Проект дорожной карты на 12 месяцев и встреча с руководством для принятия решения"],
        "inputs_title": "Что потребуется от клиента", "inputs": ["Спонсор проекта и владельцы процессов", "Доступ к интервью и имеющейся информации о процессах", "Участие IT и Security в вопросах инструментов, данных и реализуемости", "Своевременная обратная связь по выводам и допущениям"],
        "offer_note": "Стоимость относится к диагностике. Внедрение, обучение, интеграции и следующие этапы оформляются отдельным объёмом и соглашением. После диагностики компания сама решает, продолжать ли работу.",
        "form_title": "Обсудить диагностику", "form_intro": "Добавьте контекст. Поля подготовят сообщение для WhatsApp, где вы сможете проверить его перед отправкой.",
        "form_company": "Компания", "form_email": "Рабочая почта", "form_role": "Ваша роль (опционально)",
        "form_process": "Какой процесс хотите улучшить? (опционально)", "form_submit": "Подготовить сообщение в WhatsApp",
        "form_disclosure": "Сайт не отправляет и не сохраняет данные формы. Откроется WhatsApp с черновиком; вы проверите и отправите сообщение там.",
        "form_status": "Откроется WhatsApp с вашим черновиком. Проверьте данные и отправьте сообщение там.",
        "faq_eyebrow": "Вопросы руководителей", "faq_title": "Чего ждать от первого этапа.",
        "faq": [
            ("Это программа обучения?", "Диагностика начинается с бизнес-процессов, готовности и ограничений. По её итогам подходящим следующим шагом может стать обучение, пилот сценария, техническая проработка, управленческое решение или другой формат."),
            ("Нужно ли заранее выбрать AI-инструменты?", "Диагностика учитывает текущий стек и границы, заданные IT и Security. Выбор инструментов следует из процесса, рисков и оценки реализуемости."),
            ("Что будет через 2–3 недели?", "Вы получите результаты диагностики и встречу для принятия решения. Компания сможет продолжить своими силами или согласовать с Practical AI отдельный следующий этап."),
            ("Можно ли гарантировать экономию или ROI?", "Работа фиксирует исходные показатели, проверяет допущения и наблюдаемые изменения. Финансовый эффект оценивается по фактическому внедрению, затратам и использованию высвобождённой ёмкости."),
            ("Кто отвечает за решения по безопасности и соответствию?", "Уполномоченные владельцы IT, Security, Legal и рисков со стороны клиента утверждают применимые границы. Practical AI документирует эти решения для выбранных сценариев."),
            ("Сохранятся ли текущие программы по AI?", "Да. Лаборатории для компаний, спринты для руководителей и ролевые программы остаются отдельными форматами и дополнительными страницами.")],
        "final_eyebrow": "Начните с реальной работы", "final_title": "Выберите первый шаг, опираясь на процессы, которые команда хочет улучшить.",
        "final_text": "В разговоре можно уточнить контекст бизнеса, функции и понять, подходит ли диагностика как первый шаг.",
        "final_cta": "Обсудить диагностику", "programs": "Посмотреть программы", "hr": "Для HR и L&D", "team": "Познакомиться с командой", "guides": "Читать практические статьи",
        "footer": "Practical AI · Внедрение AI и трансформация бизнеса",
        "case_meta": {
            "shildpanel": ("Кейс ShildPanel | Practical AI", "Результаты задач по данным интервью: производственная отчётность, формулы ERP, анализ конкурентов и HR-рутина."),
            "kerama-marazzi": ("Кейс Kerama Marazzi | Practical AI", "Внутренние AI-тренеры: 4 подготовленных специалиста, 70 дней обучения и наставничества, более 50 практических кейсов.")},
        "case_quote": "«Теперь у меня есть плейбук, который можно передать команде, чтобы она всё реализовала.»",
        "case_quote_by": "Александр · операционный директор",
        "case_detail_note": "Результаты описывают конкретные задачи и программу. Это примеры данных компаний; эффект нового проекта зависит от его процессов, инструментов, внедрения и исходной точки.",
        "case_back": "На главную", "case_cta": "Обсудить диагностику для вашей компании",
    },
}


def esc(value: str) -> str:
    return escape(str(value), quote=True)


def list_html(items: list[str], cls: str = "") -> str:
    class_attr = f' class="{cls}"' if cls else ""
    return f"<ul{class_attr}>" + "".join(f"<li>{esc(item)}</li>" for item in items) + "</ul>"


def case_url(lang: str, slug: str) -> str:
    return ("/ru" if lang == "ru" else "") + f"/cases/{slug}/"


def home_url(lang: str) -> str:
    return "/ru/" if lang == "ru" else "/"


def meta_for(lang: str, route: str) -> tuple[str, str]:
    c = COPY[lang]
    if route.startswith("cases/"):
        return c["case_meta"][route.removeprefix("cases/")]
    return c["meta"]


def header(lang: str, route: str = "") -> str:
    c = COPY[lang]
    other = "ru" if lang == "en" else "en"
    nav = "".join(f'<a href="{esc(dest if not route else home_url(lang) + dest)}">{esc(label)}</a>' for dest, label in c["nav"])
    case_switch = f"cases/{route.removeprefix('cases/')}" if route.startswith("cases/") else ""
    switch_url = ("/ru" if other == "ru" else "") + "/" + (case_switch + "/" if case_switch else "")
    contact = f'<a class="button button--small" href="{home_url(lang)}#assessment">{esc(c["cta"])}</a>'
    menu = f'<details class="enterprise-mobile-menu"><summary>{esc(c["menu"])}</summary><nav aria-label="{esc(c["menu"])}">{nav}{contact}</nav></details>'
    return (f'<header class="site-header enterprise-header"><a class="skip-link" href="#main-content">{esc(c["skip"])}</a>'
            f'<div class="wrap nav"><a href="{home_url(lang)}" aria-label="{esc(c["home_label"])}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a>'
            f'<nav class="nav-links" aria-label="{"Main navigation" if lang == "en" else "Основная навигация"}">{nav}</nav>'
            f'<div class="nav-end">{menu}<a class="lang-switch" href="{switch_url}" lang="{other}" aria-label="{esc(c["switch_label"])}">{esc(c["switch"])}</a>{contact}</div></div></header>')


def footer(lang: str) -> str:
    c = COPY[lang]
    routes = [("/programs/" if lang == "en" else "/ru/programs/", c["programs"]),
              ("/for-hr/" if lang == "en" else "/ru/for-hr/", c["hr"]),
              ("/about/" if lang == "en" else "/ru/about/", c["team"]),
              ("/blog/" if lang == "en" else "/ru/blog/", c["guides"])]
    nav = "".join(f'<a href="{url}">{esc(label)}</a>' for url, label in routes)
    return (f'<footer class="site-footer enterprise-footer"><div class="wrap footer-inner"><div class="footer-brand"><a href="{home_url(lang)}"><img class="brand-lockup" src="/assets/brand/logo-reverse.svg" alt="Practical AI" width="760" height="152"></a><p>{esc(c["footer"])}</p></div>'
            f'<div class="footer-column"><nav class="footer-links" aria-label="{"Footer navigation" if lang == "en" else "Навигация в подвале"}">{nav}</nav><div class="footer-contact"><a href="https://wa.me/34627184000" target="_blank" rel="noopener noreferrer">WhatsApp ↗</a><a href="https://www.linkedin.com/in/danielusik/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></div></div></div></footer>')


def shell(lang: str, route: str, body: str, include_js: bool = False) -> str:
    title, description = meta_for(lang, route)
    canonical = BASE + (("/ru" if lang == "ru" else "") + "/" + (route + "/" if route else ""))
    other = "ru" if lang == "en" else "en"
    alt_url = BASE + (("/ru" if other == "ru" else "") + "/" + (route + "/" if route else ""))
    home_id = BASE + "/#organization"
    page_url = canonical
    service_name = title.split(" | ")[0]
    graph = {"@context": "https://schema.org", "@graph": [
        {"@type": "Organization", "@id": home_id, "name": "Practical AI", "url": BASE + "/", "logo": BASE + "/assets/brand/logo-primary.svg", "founder": {"@type": "Person", "name": "Danil Usik", "sameAs": "https://www.linkedin.com/in/danielusik/"}},
        {"@type": "WebSite", "@id": BASE + "/#website", "name": "Practical AI", "url": BASE + "/", "publisher": {"@id": home_id}},
        {"@type": "WebPage", "@id": page_url + "#webpage", "url": page_url, "inLanguage": lang, "isPartOf": {"@id": BASE + "/#website"}},
        {"@type": "Service", "name": service_name, "provider": {"@id": home_id}, "url": page_url}]}
    body_class = ' class="enterprise-home"'
    script = '<script src="/assets/enterprise/enterprise-home.js" defer></script>' if include_js else ""
    return f'''<!doctype html>
<html lang="{lang}"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="theme-color" content="#17213d"><meta name="robots" content="index,follow,max-image-preview:large">
<title>{esc(title)}</title><meta name="description" content="{esc(description)}">
<link rel="canonical" href="{esc(canonical)}"><link rel="alternate" hreflang="en" href="{esc(BASE + (route and '/' + route + '/' or '/'))}"><link rel="alternate" hreflang="ru" href="{esc(BASE + '/ru' + (route and '/' + route + '/' or '/'))}"><link rel="alternate" hreflang="x-default" href="{esc(BASE + (route and '/' + route + '/' or '/'))}">
<meta property="og:type" content="website"><meta property="og:site_name" content="Practical AI"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:url" content="{esc(canonical)}"><meta property="og:locale" content="{'en_US' if lang == 'en' else 'ru_RU'}"><meta property="og:image" content="{BASE}/assets/brand/social-card.png">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{BASE}/assets/brand/social-card.png">
<link rel="icon" type="image/svg+xml" href="/assets/brand/symbol-primary.svg"><link rel="stylesheet" href="/assets/brand/sales-site.css"><link rel="stylesheet" href="/assets/brand/enterprise-home.css">
<script type="application/ld+json">{__import__('json').dumps(graph, ensure_ascii=False, separators=(',', ':'))}</script>{script}
</head><body{body_class}>
{header(lang, route)}<main id="main-content" tabindex="-1">{body}</main>{footer(lang)}</body></html>'''


def render_home(lang: str) -> str:
    c = COPY[lang]
    pains = "".join(f'<article class="ea-card"><span class="ea-index">{i:02}</span><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for i, (title, text) in enumerate(c["pains"], 1))
    outcomes = "".join(f'<article class="ea-outcome"><span>{i:02}</span><div><h3>{esc(title)}</h3><p>{esc(text)}</p></div></article>' for i, (title, text) in enumerate(c["outcomes"], 1))
    team_roles = "".join(f'<li><span class="ea-team-index">{i:02}</span><span class="ea-team-role-copy"><strong>{esc(role)}</strong><small>{esc(description)}</small></span><span class="ea-team-role-mark" aria-hidden="true">↗</span></li>' for i, (role, description) in enumerate(c["hero_team_roles"], 1))
    metrics = "".join(
        f'<article class="ea-metric"><span class="ea-metric-title">{esc(name)}</span>'
        + (f'<div class="ea-metric-value"><span>{esc(before)}</span><b aria-hidden="true">→</b><strong>{esc(after)}</strong></div>' if before else f'<div class="ea-metric-value ea-single"><strong>{esc(after)}</strong></div>')
        + f'<p>{esc(note)}</p></article>' for name, before, after, note in c["shild_metrics"])
    k_metrics = "".join(f'<div class="ea-case-stat"><strong>{esc(value)}</strong><span>{esc(label)}</span></div>' for value, label in c["kerama_metrics"])
    steps = "".join(f'<article class="ea-step"><span>{esc(n)}</span><h3>{esc(title)}</h3><p>{esc(text)}</p></article>' for n, title, text in c["steps"])
    phases = "".join(f'<details class="ea-phase" {"open" if i == 0 else ""}><summary><span class="ea-phase-n">{esc(phase)}</span><span class="ea-phase-main"><b>{esc(title)}</b><small>{esc(when)}</small></span><span class="ea-phase-plus" aria-hidden="true">+</span></summary><div class="ea-phase-body"><p>{esc(description)}</p><div><b>{esc(c["roadmap_outputs"])}</b>{list_html(outputs.split(" · "))}</div><div><b>{esc(c["roadmap_decision"])}</b><p>{esc(decision)}</p></div></div></details>' for i, (phase, title, when, description, outputs, decision) in enumerate(c["phases"]))
    headers = "".join(f"<th scope=\"col\">{esc(x)}</th>" for x in c["map_headers"])
    map_rows = "".join("<tr>" + "".join(f"<td>{esc(cell)}</td>" for cell in row) + "</tr>" for row in c["map_rows"])
    calc_fields = "".join(f'<label class="ea-field" for="ea-{id}"><span>{esc(label)}</span><input id="ea-{id}" name="{id}" type="number" inputmode="decimal" min="{minimum}" max="{maximum}" step="{step}" value="{value}" data-calc="{id}"></label>' for id, label, value, minimum, maximum, step in c["calc_fields"])
    owners = "".join(f'<div class="ea-owner"><b>{esc(name)}</b><p>{esc(text)}</p></div>' for name, text in c["owners"])
    measures = "".join(f'<li>{esc(x)}</li>' for x in c["measures"])
    scope = list_html(c["scope"], "ea-check-list")
    inputs = list_html(c["inputs"], "ea-check-list")
    faq = "".join(f'<details class="ea-faq"><summary>{esc(q)}<span aria-hidden="true">+</span></summary><p>{esc(a)}</p></details>' for q, a in c["faq"])
    case1, case2 = case_url(lang, "shildpanel"), case_url(lang, "kerama-marazzi")
    body = f'''<section class="ea-hero"><div class="wrap ea-hero-grid"><div class="ea-hero-copy"><span class="eyebrow">{esc(c["eyebrow"])}</span><h1>{esc(c["h1"])}</h1><p class="ea-lede">{esc(c["lede"])}</p><div class="ea-actions"><a class="button" href="#assessment">{esc(c["hero_cta"])} <span aria-hidden="true">↓</span></a><a class="button button--ghost" href="#method">{esc(c["hero_secondary"])}</a></div><p class="ea-hero-note">{esc(c["hero_note"])}</p><div class="ea-price-line"><strong>{esc(c["hero_fee"])}</strong><span>{esc(c["hero_duration"])}</span><small>{esc(c["hero_scope"])}</small></div></div><div class="ea-hero-team" role="group" aria-label="{esc(c["hero_team_label"])}"><div class="ea-team-board-top"><span class="ea-team-kicker">{esc(c["hero_team_label"])}</span><span class="ea-team-board-mark" aria-hidden="true">PA / TEAM</span></div><div class="ea-team-board-statement"><span>{esc(c["hero_team_context"])}</span><strong>{esc(c["hero_team_statement"])}</strong></div><ol class="ea-team-roles">{team_roles}</ol><div class="ea-team-board-footer"><span>{esc(c["hero_team_footer"])}</span><span aria-hidden="true">↗</span></div></div></div></section>
<section class="ea-section ea-pain" id="problem"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["pain_eyebrow"])}</span><h2>{esc(c["pain_title"])}</h2></div><p>{esc(c["pain_intro"])}</p></div><div class="ea-grid ea-grid-3">{pains}</div></div></section>
<section class="ea-section ea-outcomes-section" id="results"><div class="wrap ea-split"><div><span class="eyebrow">{esc(c["outcomes_eyebrow"])}</span><h2>{esc(c["outcomes_title"])}</h2><p class="ea-muted">{esc(c["outcomes_intro"])}</p><a class="ea-text-link" href="#assessment">{esc(c["cta"])} <span aria-hidden="true">→</span></a></div><div class="ea-outcomes">{outcomes}</div></div></section>
<section class="ea-section ea-cases" id="cases"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["cases_eyebrow"])}</span><h2>{esc(c["cases_title"])}</h2></div><p>{esc(c["cases_intro"])}</p></div><article class="ea-case-card ea-case-shild"><div class="ea-case-head"><div><span class="ea-case-tag">{esc(c["case_source"])}</span><h3>{esc(c["case_shildpanel"])}</h3><p>{esc(c["case_shild_sub"])}</p></div><a class="ea-text-link" href="{case1}">{esc(c["case_link"])} <span aria-hidden="true">↗</span></a></div><p class="ea-case-desc">{esc(c["case_shild_desc"])}</p><div class="ea-metrics">{metrics}</div><p class="ea-caveat">{esc(c["case_note"])}</p></article><article class="ea-case-card ea-case-kerama"><div class="ea-kerama-copy"><span class="ea-case-tag">Train-the-Trainer</span><h3>{esc(c["case_kerama"])}</h3><p>{esc(c["case_kerama_sub"])}</p><p>{esc(c["case_kerama_desc"])}</p><a class="ea-text-link" href="{case2}">{esc(c["case_link"])} <span aria-hidden="true">↗</span></a></div><div class="ea-case-stats">{k_metrics}</div><p class="ea-caveat ea-reach-note">{esc(c["reach_note"])}</p></article></div></section>
<section class="ea-section ea-method" id="method"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["method_eyebrow"])}</span><h2>{esc(c["method_title"])}</h2></div><p>{esc(c["method_intro"])}</p></div><div class="ea-step-grid">{steps}</div><p class="ea-method-caption">{esc(c["method_caption"])}</p><div class="ea-cycle" aria-label="{esc(c["method_caption"])}"><span>Discover</span><b aria-hidden="true">→</b><span>Test</span><b aria-hidden="true">→</b><span>Review</span><b aria-hidden="true">→</b><span>Share</span><b aria-hidden="true">↺</b></div></div></section>
<section class="ea-section ea-roadmap" id="roadmap"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["roadmap_eyebrow"])}</span><h2>{esc(c["roadmap_title"])}</h2></div><p>{esc(c["roadmap_intro"])}</p></div><div class="ea-phases">{phases}</div></div></section>
<section class="ea-section ea-map" id="opportunity-map"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["map_eyebrow"])}</span><h2>{esc(c["map_title"])}</h2></div></div><p class="ea-map-label">{esc(c["map_label"])}</p><div class="ea-table-scroll" role="region" aria-label="{esc(c["map_title"])}" tabindex="0"><table><thead><tr>{headers}</tr></thead><tbody>{map_rows}</tbody></table></div><a class="button button--dark" href="#assessment">{esc(c["map_cta"])}</a></div></section>
<section class="ea-section ea-estimator" id="estimator"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["calc_eyebrow"])}</span><h2>{esc(c["calc_title"])}</h2></div><p>{esc(c["calc_intro"])}</p></div><div class="ea-estimator-card"><div class="ea-inputs">{calc_fields}</div><div class="ea-results"><div class="ea-result"><span>{esc(c["capacity_label"])}</span><strong id="ea-capacity" aria-live="polite">5,280 h</strong></div><div class="ea-result"><span>{esc(c["value_label"])}</span><strong id="ea-value" aria-live="polite">€211,200</strong></div><p class="ea-caveat">{esc(c["calc_note"])}</p></div></div></div></section>
<section class="ea-section ea-security" id="security"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["security_eyebrow"])}</span><h2>{esc(c["security_title"])}</h2></div><p>{esc(c["security_intro"])}</p></div><div class="ea-owner-grid">{owners}</div><p class="ea-caveat">{esc(c["security_note"])}</p></div></section>
<section class="ea-section ea-measure" id="measurement"><div class="wrap ea-split"><div><span class="eyebrow">{esc(c["measure_eyebrow"])}</span><h2>{esc(c["measure_title"])}</h2></div><div><ul class="ea-measures">{measures}</ul><p class="ea-muted">{esc(c["measure_note"])}</p></div></div></section>
<section class="ea-section ea-assessment" id="assessment"><div class="wrap"><div class="ea-section-head"><div><span class="eyebrow">{esc(c["assessment_eyebrow"])}</span><h2>{esc(c["assessment_title"])}</h2></div><div class="ea-price-box"><strong>{esc(c["assessment_price"])}</strong><span>{esc(c["assessment_duration"])}</span></div></div><p class="ea-assessment-intro">{esc(c["assessment_intro"])}</p><div class="ea-assessment-grid"><article class="ea-scope-card"><h3>{esc(c["scope_title"])}</h3>{scope}<h3>{esc(c["inputs_title"])}</h3>{inputs}<p class="ea-caveat">{esc(c["offer_note"])}</p></article><article class="ea-form-card"><div class="ea-form-team"><span class="ea-form-team-mark" aria-hidden="true">PA</span><div><b>{esc(c["team_contact_title"])}</b><span>{esc(c["team_contact_subtitle"])}</span></div></div><h3>{esc(c["form_title"])}</h3><p>{esc(c["form_intro"])}</p><form id="enterprise-assessment-form" data-lang="{lang}"><label for="ea-company">{esc(c["form_company"])} <span aria-hidden="true">*</span></label><input id="ea-company" name="company" autocomplete="organization" required><label for="ea-email">{esc(c["form_email"])} <span aria-hidden="true">*</span></label><input id="ea-email" name="email" type="email" autocomplete="email" required><label for="ea-role">{esc(c["form_role"])}</label><input id="ea-role" name="role" autocomplete="organization-title"><label for="ea-process">{esc(c["form_process"])}</label><textarea id="ea-process" name="process" rows="3"></textarea><button class="button button--dark" type="submit">{esc(c["form_submit"])} ↗</button><p class="ea-form-disclosure">{esc(c["form_disclosure"])}</p><p class="ea-form-status" id="ea-form-status" role="status" aria-live="polite"></p></form><a class="ea-secondary-contact" href="https://www.linkedin.com/in/danielusik/" target="_blank" rel="noopener noreferrer">LinkedIn ↗</a></article></div></div></section>
<section class="ea-section ea-faq" id="faq"><div class="wrap ea-split"><div><span class="eyebrow">{esc(c["faq_eyebrow"])}</span><h2>{esc(c["faq_title"])}</h2></div><div class="ea-faq-list">{faq}</div></div></section>
<section class="ea-final" id="contact"><div class="wrap ea-final-inner"><div><span class="eyebrow">{esc(c["final_eyebrow"])}</span><h2>{esc(c["final_title"])}</h2><p>{esc(c["final_text"])}</p></div><a class="button" href="#assessment">{esc(c["final_cta"])} ↓</a></div><div class="wrap ea-secondary-links"><a href="{('/ru' if lang == 'ru' else '')}/programs/">{esc(c["programs"])}</a><a href="{('/ru' if lang == 'ru' else '')}/for-hr/">{esc(c["hr"])}</a><a href="{('/ru' if lang == 'ru' else '')}/about/">{esc(c["team"])}</a><a href="{('/ru' if lang == 'ru' else '')}/blog/">{esc(c["guides"])}</a></div></section>'''
    return shell(lang, "", body, include_js=True)


def render_case(lang: str, slug: str) -> str:
    c = COPY[lang]
    if slug == "shildpanel":
        title, subtitle, summary = c["case_shildpanel"], c["case_shild_sub"], c["case_shild_desc"]
        cards = "".join(f'<article class="ea-metric"><span class="ea-metric-title">{esc(name)}</span><div class="ea-metric-value">' + (f'<span>{esc(before)}</span><b aria-hidden="true">→</b><strong>{esc(after)}</strong>' if before else f'<strong>{esc(after)}</strong>') + f'</div><p>{esc(note)}</p></article>' for name, before, after, note in c["shild_metrics"])
        detail = f'<div class="ea-metrics ea-case-detail-metrics">{cards}</div><blockquote class="ea-quote">{esc(c["case_quote"])}<cite>{esc(c["case_quote_by"])}</cite></blockquote>'
    else:
        title, subtitle, summary = c["case_kerama"], c["case_kerama_sub"], c["case_kerama_desc"]
        stats = "".join(f'<div class="ea-case-stat"><strong>{esc(value)}</strong><span>{esc(label)}</span></div>' for value, label in c["kerama_metrics"])
        detail = f'<div class="ea-case-stats ea-case-detail-stats">{stats}</div><p class="ea-caveat ea-reach-note">{esc(c["reach_note"])}</p>'
    source = c["case_source"] if slug == "shildpanel" else c["kerama_source"]
    body = f'''<section class="ea-case-page"><div class="wrap"><a class="ea-back-link" href="{home_url(lang)}#cases">← {esc(c["case_back"])}</a><span class="eyebrow">{esc(source)}</span><h1>{esc(title)}</h1><p class="ea-case-page-subtitle">{esc(subtitle)}</p><p class="ea-case-desc">{esc(summary)}</p>{detail}<p class="ea-caveat ea-case-disclaimer">{esc(c["case_detail_note"])}</p><a class="button button--dark" href="{home_url(lang)}#assessment">{esc(c["case_cta"])}</a></div></section>'''
    return shell(lang, f"cases/{slug}", body)

