#!/usr/bin/env python3
"""Make the Practical AI social preview from the selected outlined SVG master."""
from pathlib import Path
import re

from resvg_py import svg_to_bytes

ROOT = Path(__file__).resolve().parents[1]
BRAND = ROOT / "docs/assets/brand"
logo = (BRAND / "logo-primary.svg").read_text(encoding="utf-8")
inner = re.search(r"<svg[^>]*>(.*)</svg>", logo, re.S).group(1)
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="#e9eff6"/>
  <path d="M0 0h1200v14H0z" fill="#17213d"/>
  <path d="M1050 0h90L882 630h-90z" fill="#17213d" opacity=".06"/>
  <path d="M1150 0h50L942 630h-50z" fill="#f4d447" opacity=".48"/>
  <svg x="118" y="223" width="964" height="193" viewBox="0 0 760 152">{inner}</svg>
  <path d="M118 528h118v8H118z" fill="#17213d"/>
  <path d="M244 528h56v8h-56z" fill="#f4d447"/>
</svg>'''
(BRAND / "social-card.svg").write_text(svg + "\n", encoding="utf-8")
(BRAND / "social-card.png").write_bytes(svg_to_bytes(svg_string=svg, width=1200))
print("Built social-card.svg and social-card.png")
