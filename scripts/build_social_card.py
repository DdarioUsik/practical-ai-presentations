#!/usr/bin/env python3
"""Build the Practical AI social card from the web wordmark and deck illustration."""
from base64 import b64encode
from pathlib import Path
import re

from resvg_py import svg_to_bytes

BRAND = Path(__file__).resolve().parents[1] / "docs/assets/brand"
wordmark = (BRAND / "glass/wordmark.svg").read_text(encoding="utf-8")
inner = re.search(r"<svg[^>]*>(.*)</svg>", wordmark, re.S).group(1)
lime = b64encode((BRAND / "glass/lime.webp").read_bytes()).decode("ascii")
svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="630" viewBox="0 0 1200 630">
  <rect width="1200" height="630" fill="#e8f52e"/>
  <image href="data:image/webp;base64,{lime}" x="592" y="92" width="574" height="427" />
  <svg x="95" y="222" width="480" height="143" viewBox="0 0 470 140">{inner}</svg>
</svg>'''
(BRAND / "social-card.svg").write_text(svg + "\n", encoding="utf-8")
(BRAND / "social-card.png").write_bytes(svg_to_bytes(svg_string=svg, width=1200))
print("Built social-card.svg and social-card.png")
