# Intake Log

## Progress
- target_cases: 30
- collected_cases: 31

## Entries

### 2026-03-04
- Создан intake-session файл.
- Зафиксирован контекст и старт Step 1.
- Добавлено 7 структурированных кейсов в `20_Cases`.
- Создан первичный файл причин пауз/потерь в `30_Objections`.
- Обновлен следующий шаг: Step 2 (diagnostics).
- Добавлен пакет диагностик (9 кейсов) в `20_Cases`.
- Добавлены паттерны воронки из диагностик в `10_Funnel`.
- Добавлена карта возражений из диагностик в `30_Objections`.
- Добавлено 9 кейсов по командным встречам (воронка, оффер, позиционирование, митапы, масштаб pipeline, процесс-карты).
- Добавлено 3 deal-outcome кейса (ЛПР/оффер/причина/follow-up).
- Добавлен summary по паттернам закрытых/проигранных сделок.
- Добавлено 3 свежих кейса из активных переписок (Artur / Optima / Artem).
- Добавлены паттерны активных сделок (воронка + возражения).
- Порог 30 кейсов закрыт.
- Добавлена baseline-метрика денежной воронки: 100 outreach -> 7 dialogues -> 0 deals.
- Запущен 2-недельный execution-спринт по `PLAYBOOK_TOP10.md`.
- Добавлен weekly scoreboard на 2 недели: outreach / qualified dialogues / diagnostics with LPR / proposals / paid pilots.
- Зафиксированы 3 ключевых отклонения относительно baseline для еженедельного контроля.
- Добавлен блок `Client Intelligence Gate` (правила pre-call проверки ICP/LPR/urgency).
- Добавлен шаблон досье клиента `40_Templates/CLIENT_DOSSIER_TEMPLATE.md`.
- Догружены дополнительные near-miss кейсы из переписок (Aleksandr / Sofia / Rudolf).
- Добавлен новый skill `dynamic-diagnostic-questionnaire` для генерации гибкого опросника перед диагностикой.
- Добавлен входной шаблон `40_Templates/DIAGNOSTIC_BRIEF_INPUT.md` для быстрой подготовки к встрече.
- Добавлен единый skill `sales-execution-copilot` для режима отдельного чата (lead intake, outreach, meeting prep, dialogue structuring).
- Добавлен готовый промпт для запуска отдельного чата: `00_Inbox/AGENT_SALES_COPILOT_PROMPT.md`.
- Импортирована внешняя база кейсов из `~/Downloads` в `60_External_Cases/` (Practical AI + GOLD).
- Добавлен индекс внешней библиотеки: `60_External_Cases/INDEX.md`.
- Обновлен `sales-execution-copilot`: обязательный доступ к `60_External_Cases` как источнику примеров.
- Отменен трек с автоматической аудио-расшифровкой DrHead; временные JSON-расшифровки удалены.
- Добавлен раздел клиентов `70_Clients/` с отдельными папками по всем текущим клиентам из базы кейсов.
- Для каждого клиента создана рабочая структура: profile / meetings / notes / proposals / messages / documents / questionnaires / outgoing / tasks.
- Создан индекс клиентов: `70_Clients/INDEX.md`.
- Импортирован полный пакет DrHead в `70_Clients/DrHead/` (контекст, prep PDF, опросники по участникам).
- Для опросников DrHead создана текстовая версия `.txt` для быстрого поиска и доступа агента.
- Добавлен отдельный prompt `00_Inbox/COLD_OUTREACH_AGENT_PROMPT.md` для короткого вызова "агент по холодным сообщениям".
- Обновлен `sales-execution-copilot`: добавлен режим `Raw LinkedIn Paste -> Cold Outreach` без обязательного шаблона ввода.
