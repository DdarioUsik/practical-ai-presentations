# Client Intelligence Gate

Цель: перед любой диагностикой понять, это целевой клиент или нет.

## Trigger
Когда пользователь присылает контакт/компанию/переписку потенциального клиента.

## Mandatory workflow
1. Собери `Client Dossier` по шаблону `40_Templates/CLIENT_DOSSIER_TEMPLATE.md`.
2. Оцени `ICP Fit (0-10)`.
3. Оцени `LPR score (0-3)`:
   - 0: неизвестно кто решает,
   - 1: есть champion, нет доступа к LPR,
   - 2: identified LPR, но нет прямого слота,
   - 3: прямой контакт с LPR.
4. Оцени `Urgency (0-3)`:
   - 0: нет срока/инициативы,
   - 1: интерес общий,
   - 2: есть проектный горизонт,
   - 3: есть дата решения.
5. Выбери маршрут:
   - `Route A (go diagnostic)`: ICP >= 6, LPR >= 2, Urgency >= 2.
   - `Route B (nurture)`: ICP 4-5 или LPR/Urgency = 1.
   - `Route C (disqualify)`: ICP <= 3 или нет релевантной боли.

## Required output format (for each lead)
- Fit verdict: A/B/C
- Why now: 1-2 причины
- Missing data: что нужно дособрать
- Next action in 24h: конкретное сообщение/шаг

## Quality bar
- Не идти в созвон без гипотезы боли и роли собеседника.
- Не продавать до прояснения decision chain.
- Любой `near-miss` сохранять как кейс в `20_Cases`.
