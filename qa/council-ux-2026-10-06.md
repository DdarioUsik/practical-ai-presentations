# Practical AI — UX and accessibility review

```yaml
v: ACP1
id: h:20261006-conversion-brand-production-auditor
src: brand-production-auditor
dst: DES
t: R
act: ANL
p: PUB
a: A2
c: 0.95
u: NOW
decision: HOLD
scope: website UX and accessibility source review
human_approval_required: true
```

`HOLD` means the requested conversion package is not ready for release review. The existing checker passes structural/local-link checks, but it does not cover the defects below.

## Prioritized findings

1. **P0 — Defect: the requested contact route is absent.** Evidence: `scripts/build_sales_site.py:143-148` generates only `t.me` URLs; all hero, card, header and closing CTAs inherit them. Buyer consequence: a buyer expecting WhatsApp at `+34 627 184 000` cannot use the requested primary channel, while Telegram-only contact creates avoidable friction. Fix: generate contextual EN/RU `wa.me/34627184000` links as primary CTAs and expose Telegram as a clearly labelled alternative.

2. **P0 — Defect: mobile/tablet loses the persistent conversion action.** Evidence: `docs/assets/brand/sales-site.css:170` hides `.nav-end .button` at widths up to 1060px; at `:175-176` navigation becomes a scrollbar-hidden horizontal strip. Buyer consequence: the main contact action disappears and some navigation may be undiscoverable to touch/keyboard users. Fix: keep one visible contact control at every width; use a labelled menu or wrapping navigation with a visible overflow affordance and 44px minimum targets.

3. **P0 — Defect: team credibility requested in the brief is missing.** Evidence: `scripts/build_sales_site.py:57,116,255-261` renders generic facets only; `:69-71` makes About another method description. The generated homepage and About page name no people or roles. Buyer consequence: HR/L&D cannot evaluate who will deliver the work, weakening trust before contact. Fix: add verified cards for Danil Usik, Svetlana Galakhova and Julia Krylova with role, concise evidence-backed expertise and LinkedIn; hold Julia-specific claims until verified.

4. **P1 — Defect: the final CTA lacks decision-support and channel choice.** Evidence: `scripts/build_sales_site.py:218-220` outputs only a question and one Telegram link; the screenshot `output/playwright/home-before.png` confirms the sparse closing band. Buyer consequence: buyers receive no prompt for what to send or what happens next. Fix: state three inputs (team/roles, recurring task, desired outcome), the next step without invented timing, then WhatsApp primary plus Telegram alternative.

5. **P1 — Defect: keyboard users have no skip path.** Evidence: generated pages begin with header then `<main>` (`docs/index.html:12-13`), with no skip link; the sticky header and multi-link navigation repeat on every page. Buyer consequence: keyboard and screen-reader users must traverse global navigation on every route. Fix: add a focus-visible “Skip to main content” link and stable `id="main-content"` in the shared shell/builders.

6. **P1 — Defect: internal implementation language is public.** Evidence: `scripts/build_sales_site.py:30,88` exposes “Educational programs · second step” / “второй экран”; it appears in `docs/index.html:14` and the screenshot. Buyer consequence: the label sounds like a wireframe note and makes the page feel unfinished. Fix: replace it with a buyer-facing category such as “Programs for business teams” / “Программы для бизнес-команд.”

7. **P2 — Hypothesis: the page delays human trust evidence too long.** Evidence: `docs/index.html:13-18` places hero, programs, one case, quotes and method before the anonymous team section; the screenshot shows the same sequence. Buyer consequence (hypothesis): risk-conscious corporate buyers may postpone contact because provider identity arrives late and remains abstract. Fix/test: introduce a compact named-team trust strip near the hero/program choice, retain fuller cards later, and validate through qualitative buyer sessions rather than claiming a conversion lift.

## Checks and evidence

- `scripts/check_sales_site.py`: PASS — 8 sales pages and 9 editorial pages; metadata, language alternates, local assets and shared navigation checked.
- Manual review items: responsive keyboard/touch test at 320/768/1024px; automated WCAG contrast/accessibility scan; verify all three LinkedIn profiles and Julia’s role before release.
- Next corrective action: implement findings 1–6 in source builders/shared CSS, rebuild, run the checker plus responsive accessibility tests, then return for independent review and human approval.

## Files read

`qa/conversion-brief-2026-10-06.md`; `scripts/build_sales_site.py`; `scripts/build_site.py`; `scripts/build_blog_shell.py`; `scripts/check_sales_site.py`; `docs/assets/brand/sales-site.css`; `docs/assets/brand/workflow-method-en.svg`; generated EN/RU home, For HR and About HTML; `output/playwright/home-before.png`; ACP-1 and mandatory runtime context files.

## Files changed

Only this report. Production, generated site and durable memory were unchanged; no session note is warranted for this bounded review.
