# Practical AI conversion review — 2026-10-06

## Goal
Help an HR/L&D or business leader decide whether to start a conversation with Danil about corporate AI training. The user requested a council, named core-team cards, LinkedIn links, WhatsApp as the primary contact route (+34 627 184 000), Telegram as an alternative, and a website-wide bug and presentation review.

## Current evidence
- Production: https://practical-ai.pro/
- Source: `scripts/build_sales_site.py`; build: `scripts/build_site.py`.
- Shared styling: `docs/assets/brand/sales-site.css`.
- Shared guide shell: `scripts/build_blog_shell.py`.
- Routes: EN/RU homepage, Programs, For HR & L&D, About, guide index and three paired guide articles. Historical case/proposal pages also exist; preserve their content.
- Homepage sequence: hero/workflow card → program cards → ShildPanel task results → three participant remarks → method and workflow illustration → generic team paragraph → guides → single closing CTA.
- Team section names nobody; About repeats the method rather than identifying people.
- All main contact links currently use Telegram. Header hides the CTA at <=1060px.
- Screenshot: `output/playwright/home-before.png`.
- Builder currently exposes “second step”/“второй экран” in the program eyebrow. Earlier user preferences: roles rather than company names in testimonial bylines; remove visible source footnotes.

## Proposed changes
Named core-team cards for Danil Usik, Svetlana Galakhova, Julia Krylova; concise verified expertise and LinkedIn links. WhatsApp primary with contextual EN/RU draft messages; Telegram visible as an alternative. A concrete final contact section describes what to share and what happens next. Keep both languages and existing branding. Make the navigation/contact usable on mobile. Fix observed broken assets, internal links, anchors, layout and contrast issues within the current site.

## Constraints and open facts
Use existing project architecture and source scripts. Read only; do not edit source or publish anything. Avoid unsupported biographies, sales guarantees, invented response times or free-call offers. User supplied three team names; Julia’s specific role and profile are pending verification. Review wording and visible quality, not fabricated conversion metrics. Do not send messages, open messaging drafts through an account, or submit forms.

## Review output
Give 5–8 prioritized recommendations with exact page or source locations, buyer impact, and a concrete fix. Distinguish observed defects from hypotheses. Keep the report under 700 words. Do not delegate further or expand into brand/legal/system audits.
