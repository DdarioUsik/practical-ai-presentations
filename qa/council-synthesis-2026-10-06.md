# Practical AI — conversion council and implementation

## Goal
Make the homepage identify the people delivering the training and help buyers start a useful conversation with Danil. The user requested a council, core-team cards for Danil Usik, Svetlana Galakhova and Julia Krylova, LinkedIn links, WhatsApp at +34 627 184 000, Telegram as an alternative, and a site review. The follow-up explicitly requested the team's LinkedIn portraits.

## Independent perspectives
Launched through `pc.py agent run --profile safe`: Neo reviewed corporate buyer/sales needs; Brand Production Auditor reviewed UX/accessibility. Both read the same conversion brief and existing source. The initial auditor HOLD concerned the pre-change site, not the final implementation.

Both identified anonymous team copy, Telegram-only CTAs, a hidden mobile header CTA, and a weak final contact section. UX additionally identified the missing keyboard skip link. Buyer/sales proposed showing team identity earlier and qualifying the first inquiry. Both flagged customer-visible “second step” wording.

## Decisions implemented
- Replace the abstract team block with three named cards, verified profile links, relevant bios and original 400×400 LinkedIn portraits. Show the same team on About. Sources and original-file hashes: `team-portrait-sources-2026-10-06.json`.
- Add a hero link to the core team, place its full cards before the method section, and rename the About navigation entry to Our team.
- Make WhatsApp the primary commercial CTA throughout the current EN/RU sales and guide pages; offer Telegram in the hero/page hero, closing and footer.
- Explain the first conversation: team size, recurring task, preferred timing; discuss priorities/tools and choose a format. Show Danil's real portrait and phone number in the closing panel.
- Keep the header contact visible across screen sizes, provide 44px contact/language targets, a keyboard skip link and suitable fragment offsets.
- Remove implementation labels and restore role-only testimonial bylines and the earlier preference to omit visible source footnotes. Case results remain tied to their stated tasks and named case.
- Repair nine legacy case links to absent offer pages with readable case-specific WhatsApp drafts.
- Fix program cards that overflowed on tablet widths. Version shared CSS by content hash so a new deployment requests current styling.

## Verification
- Static check: 8 sales and 9 editorial pages passed metadata, alternates, navigation and assets.
- Full site links: 36 HTML pages and 549 local page/asset/fragment references passed.
- Browser: 87 route/viewport checks; all 36 pages at 1440px, and the 17 current sales/guide pages at 320, 375, 768 and 1440px. Initial failures were eight sales pages overflowing at 768px. After the grid fix, all 17 pages passed the affected 768px checks. Broken images and runtime page errors: none observed. All core-team portraits loaded; header contact was visible; keyboard skip worked.
- Viewed desktop team/closing screenshots and the Russian mobile homepage. The large empty method area in the initial screenshot was lazy-load timing; scrolling to the actual visual loaded it successfully.
- Reports: `browser-audit-results-2026-10-06.json`, `browser-regression-results-2026-10-06.json`.

## Limits
These changes improve clarity and remove observed defects. Conversion lift has not been measured. Contact links were inspected without sending messages. Public professional profiles can require LinkedIn sign-in; photos are served as local assets and do not depend on a visitor's LinkedIn session.
