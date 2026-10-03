# practical-ai-presentations

Practical AI site and client presentations. The public site is published from
`docs/` on the `main` branch to `https://practical-ai.pro/` via GitHub Pages.

## Corporate site

- Edit `site-source/home.en.html` for the English homepage and its content.
- Run `python3 scripts/build_site.py` to generate `docs/index.html`, the static
  Russian `docs/ru/index.html`, shared corporate blog branding, and sitemap.
- Brand assets and design tokens are in `docs/assets/brand/`. The approved `//`
  marks are outlined SVG files; the web font is self hosted and includes its
  SIL Open Font License.
- `scripts/build_social_card.py` regenerates the 1200 × 630 social image from
  `logo-primary.svg` using `resvg_py`.
- Preview locally with `python3 -m http.server 8768 --directory docs`.

The legacy AIHUB case studies and client presentations have their own visual
identity and remain separate from the corporate site pages.
