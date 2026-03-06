---
stage: solution_alignment
source: meeting_diagnostic
result: pause
loss_reason: security_constraints_and_customization_scope_unclear
created: 2026-03-04
---

# Case: Optima Exchange — техсогласование с командой

## Context
Техническая встреча с разработчиками и управляющими Optima. Ключевая тема: Telegram Business API vs TDLib, риски бана, права доступа операторов, SLA реакции, аналитика по операторам.

## Client Goal
Быстро получить "супер-мессенджер" с жестким контролем операторов и без потери доверия клиентов.

## What I Proposed
- Возможный iFrame/виджет подход + callback-интеграция в их CRM.
- Этапный запуск: сначала ядро мессенджера, AI-слой позже.
- Сбор требований и оценка сроков/бюджета.

## What Worked
- Четко выявлены must-have требования.
- Зафиксирован следующий шаг: требования + оценка вилки.

## What Failed
- Ожидания по срокам "очень срочно", а требования еще не формализованы.
- Часть функционала требует кастомной доработки.

## Objections
- Риск бана Telegram-аккаунта.
- Нежелание видимых ботов в коммуникации.
- Жесткие требования к speed-to-first-response.

## Next Action
Собрать formal requirements doc (функциональные + нефункциональные), затем выдать 2 варианта: fast MVP vs full custom.
