# practical-ai-presentations

Practical AI site and client presentations. The public site is published from
`docs/` on the `main` branch to `https://practical-ai.pro/` via GitHub Pages.

## Corporate site

- Enterprise homepage and case copy lives in `scripts/enterprise_site.py`;
  supporting page copy stays in `scripts/build_sales_site.py`. The homepage
  design is in `docs/assets/brand/enterprise-home.css`. Use
  `python3 scripts/build_sales_site.py --enterprise-only` to build only the
  EN/RU homepages and enterprise case pages while preserving other page files.
- Run `python3 scripts/build_site.py` to generate the static home, HR, programs,
  team approach pages in both languages, the Russian schools page, the localized workflow SVGs, and the sitemap. Each page has its own
  URL, title, description, canonical, hreflang and JSON-LD.
- Run `python3 scripts/check_sales_site.py` before publishing; it checks the
  nine sales pages, local links, language alternates and section order. The
  Russian school page is published at `/ru/for-schools/`; other sizes, longer
  programs, delivery mode, venue and travel conditions are discussed individually.
- Brand assets and design tokens are in `docs/assets/brand/`. The approved `//`
  marks are outlined SVG files; the web font is self hosted and includes its
  SIL Open Font License.
- Program scenes are generated illustrations with visible labels. Their prompts
  are recorded in `scripts/program-image-prompts.md`; the workflow visual is
  reproducible from `scripts/build_workflow_visual.py`. The ShildPanel evidence
  block uses the client logo, case figures and attributed participant quotes.
- `scripts/build_social_card.py` regenerates the 1200 × 630 social image from
  `logo-primary.svg` using `resvg_py`.
- Preview locally with `python3 -m http.server 8768 --directory docs`.

The legacy AIHUB case studies and client presentations have their own visual
identity and remain separate from the corporate site pages. The earlier homepage
can be recovered from Git history at commit `92221d8`.
