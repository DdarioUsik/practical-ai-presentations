---
name: dynamic-diagnostic-questionnaire
description: Generate a flexible pre-call diagnostic questionnaire from a lead description, company context, and sales stage. Use when the user wants a ready question flow for discovery calls that adapts by ICP fit, LPR access, urgency, and offer route.
---

# Dynamic Diagnostic Questionnaire

Create a call-ready question flow before every diagnostic meeting. Use `CLIENT_DOSSIER_TEMPLATE.md` as input data model.

## Required Input

Collect or infer:
- lead role and function,
- company segment and stage,
- current business pain hypothesis,
- LPR access level,
- expected call goal (`qualify`, `scope pilot`, `move to proposal`).

If data is missing, start output with a short `Missing data` block and add the exact clarifying questions to ask in the first 3 minutes.

## Scoring Gate

Score before generating deep questions:
- `ICP fit` (0-10),
- `LPR score` (0-3),
- `Urgency` (0-3).

Routing:
- `Route A`: ICP >= 6, LPR >= 2, Urgency >= 2.
- `Route B`: medium fit; run light qualification + nurture path.
- `Route C`: low fit; run short disqualify script.

## Output Format

Return exactly these sections:

1. `Call objective (1 sentence)`
2. `Questionnaire (core 12)`:
   - 3 questions: business context and pain
   - 3 questions: economics and impact
   - 3 questions: decision chain and LPR
   - 3 questions: urgency, pilot readiness, next step
3. `Branching`:
   - If no LPR access -> 3 escalation questions
   - If no urgency -> 3 priority questions
   - If budget resistance -> 3 pilot framing questions
4. `Red flags`:
   - 3-5 stop-signals for this lead
5. `Commit ask`:
   - one exact phrase to lock next action with date
6. `CRM summary template`:
   - pain, LPR, urgency, route, next step, risk

Keep output concise and copy-paste ready for a live call.

## Question Quality Rules

- Ask one idea per question.
- Prefer measurable language (`how much`, `how often`, `by when`).
- Avoid generic consulting questions.
- Move from context -> pain -> economics -> decision -> commit.
- No solution pitching before pain and decision chain are confirmed.

## Tone Rules

- Professional and direct.
- No jargon overload.
- Questions must sound natural in Russian for B2B conversation.

## Post-Call Conversion

After user provides call notes, convert to:
- route decision (`A/B/C`),
- top objections,
- recommended follow-up in 24h,
- pilot hypothesis (scope, KPI, timeline) if route A.
