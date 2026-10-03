#!/usr/bin/env python3
"""Draw localized, editable Practical AI workflow visuals from SVG primitives."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT_DIR = Path(__file__).resolve().parents[1] / "docs/assets/brand"
parts: list[str] = []


def rect(x, y, width, height, fill, radius=0, stroke="none", stroke_width=1, opacity=1):
    parts.append(f'<rect x="{x}" y="{y}" width="{width}" height="{height}" rx="{radius}" fill="{fill}" stroke="{stroke}" stroke-width="{stroke_width}" opacity="{opacity}"/>')


def label(x, y, value, size=18, fill="#17213D", weight=400, spacing=0, anchor="start"):
    parts.append(f'<text x="{x}" y="{y}" fill="{fill}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" letter-spacing="{spacing}" text-anchor="{anchor}">{escape(value)}</text>')


def path(data, stroke, width=2, fill="none", opacity=1):
    parts.append(f'<path d="{data}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round" opacity="{opacity}"/>')


parts.append('''<svg xmlns="http://www.w3.org/2000/svg" width="1536" height="1024" viewBox="0 0 1536 1024" role="img" aria-labelledby="title desc">
<title id="title">From a team task to a reviewed AI workflow</title>
<desc id="desc">A scripted vector illustration with three connected stages: team task, AI-supported draft, and human review. It is an example workflow, not a client result.</desc>
<defs>
  <linearGradient id="board" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#17213D"/><stop offset="1" stop-color="#283C5D"/></linearGradient>
  <linearGradient id="gold" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFE77A"/><stop offset="1" stop-color="#F4D447"/></linearGradient>
  <filter id="shadow" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="18" stdDeviation="22" flood-color="#070D1E" flood-opacity=".22"/></filter>
  <pattern id="grid" width="48" height="48" patternUnits="userSpaceOnUse"><path d="M48 0H0V48" fill="none" stroke="#FFFFFF" stroke-opacity=".045" stroke-width="1"/></pattern>
</defs>''')
rect(0, 0, 1536, 1024, "#E9EFF6")
rect(42, 42, 1452, 940, "url(#board)", 34)
rect(42, 42, 1452, 940, "url(#grid)", 34)

# Brand signature and framing details.
path("M95 123 L118 74 H133 L110 123 Z", "none", 0, "#FFFFFF")
path("M132 123 L155 74 H170 L147 123 Z", "none", 0, "#F4D447")
label(197, 111, "PRACTICAL AI", 23, "#FFFFFF", 800, 1.2)
label(1440, 110, "WORKFLOW / 01", 15, "#AABBD0", 700, 2, "end")
path("M94 151 H1442", "#6E819F", 1, opacity=.42)
label(95, 215, "ONE SHARED METHOD", 16, "#F4D447", 800, 2.8)
label(95, 264, "A useful AI step starts with the team’s work.", 36, "#FFFFFF", 700, -.8)

# Three cards, built from shapes and editable type rather than image fragments.
rect(97, 330, 395, 510, "#FFFFFF", 20)
rect(570, 330, 395, 510, "#314666", 20, "#617899", 2)
rect(1044, 330, 395, 510, "#FFFFFF", 20)

# Phase 1: existing task and several team roles.
rect(125, 357, 88, 31, "#E9EFF6", 15)
label(169, 378, "01 / TASK", 11, "#17213D", 800, 1.1, "middle")
label(125, 432, "Start with real work", 28, "#17213D", 700, -.6)
label(125, 460, "One recurring task · one clear owner", 16, "#607089")
for i, (initial, color) in enumerate((("S", "#F4D447"), ("H", "#B9D9CE"), ("O", "#C8D4E7"), ("F", "#E8BEAC"))):
    x = 130 + i * 62
    rect(x, 506, 51, 51, color, 15)
    label(x + 25.5, 540, initial, 19, "#17213D", 800, anchor="middle")
label(126, 596, "INPUTS", 12, "#65758C", 800, 1.8)
for i, length in enumerate((286, 210, 255)):
    rect(126, 622 + i * 34, length, 12, "#D8E1EC", 6)
rect(126, 754, 333, 55, "#E9EFF6", 12)
label(143, 789, "TEAM TASK + QUALITY CRITERIA", 13, "#17213D", 800, 1.1)

# Connectors are deliberately part of the vector composition.
path("M502 584 H558", "#F4D447", 7)
path("M541 570 L559 584 L541 598", "#F4D447", 7)
path("M975 584 H1031", "#F4D447", 7)
path("M1014 570 L1032 584 L1014 598", "#F4D447", 7)

# Phase 2: the AI step, shown as a restrained tool surface.
rect(598, 357, 101, 31, "#F4D447", 15)
label(648, 378, "02 / AI", 11, "#17213D", 800, 1.1, "middle")
label(598, 432, "Try one AI step", 28, "#FFFFFF", 700, -.6)
label(598, 460, "Inputs → draft → quality check", 16, "#C8D5E6")
rect(598, 495, 339, 220, "#1B2A46", 16, "#5E7492", 1)
rect(621, 517, 293, 22, "#314666", 5)
for i, width in enumerate((145, 209, 174)):
    rect(621, 560 + i * 37, width, 11, "#647996", 5)
path("M782 670 L832 560 H857 L807 670 Z", "none", 0, "#FFFFFF")
path("M837 670 L887 560 H912 L862 670 Z", "none", 0, "url(#gold)")
rect(598, 754, 339, 55, "#405878", 12)
label(617, 789, "DRAFT READY FOR REVIEW", 13, "#FFFFFF", 800, 1.1)

# Phase 3: reviewed work and shared practice.
rect(1072, 357, 109, 31, "#E9EFF6", 15)
label(1126, 378, "03 / REVIEW", 11, "#17213D", 800, 1.1, "middle")
label(1072, 432, "Check together", 28, "#17213D", 700, -.6)
label(1072, 460, "A person judges the result", 16, "#607089")
rect(1072, 502, 339, 215, "#F2F5F9", 14)
for i, width in enumerate((218, 184, 235)):
    y = 535 + i * 53
    rect(1094, y - 15, 30, 30, "#F4D447", 9)
    path(f"M1102 {y} L1109 {y+7} L1118 {y-6}", "#17213D", 3)
    rect(1143, y - 5, width, 10, "#B6C5D7", 5)
rect(1072, 754, 339, 55, "#E9EFF6", 12)
label(1090, 789, "A REUSABLE TEAM PRACTICE", 13, "#17213D", 800, 1.1)

# Bottom sequence works as a compact visual caption at full width.
path("M95 890 H1440", "#6E819F", 1, opacity=.42)
label(96, 931, "TEAM TASK", 14, "#FFFFFF", 800, 1.2)
label(374, 931, "→", 21, "#F4D447", 800)
label(452, 931, "AI STEP", 14, "#FFFFFF", 800, 1.2)
label(686, 931, "→", 21, "#F4D447", 800)
label(767, 931, "HUMAN REVIEW", 14, "#FFFFFF", 800, 1.2)
label(1082, 931, "→", 21, "#F4D447", 800)
label(1163, 931, "SHARED PRACTICE", 14, "#FFFFFF", 800, 1.2)
parts.append("</svg>")

RU = {
    "From a team task to a reviewed AI workflow": "От задачи команды к проверенному AI-сценарию",
    "A scripted vector illustration with three connected stages: team task, AI-supported draft, and human review. It is an example workflow, not a client result.": "Векторная иллюстрация трёх этапов: задача команды, AI-черновик и проверка человеком. Это пример процесса, а не результат клиента.",
    "WORKFLOW / 01": "ПРОЦЕСС / 01",
    "ONE SHARED METHOD": "ОБЩИЙ МЕТОД",
    "A useful AI step starts with the team’s work.": "AI-практика начинается с задач команды.",
    "01 / TASK": "01 / ЗАДАЧА",
    "Start with real work": "Начинаем с задачи",
    "One recurring task · one clear owner": "Одна задача · один ответственный",
    "INPUTS": "ДАННЫЕ",
    "TEAM TASK + QUALITY CRITERIA": "ЗАДАЧА + КРИТЕРИИ КАЧЕСТВА",
    "02 / AI": "02 / AI",
    "Try one AI step": "Пробуем AI-шаг",
    "Inputs → draft → quality check": "Вход → черновик → проверка",
    "DRAFT READY FOR REVIEW": "ЧЕРНОВИК ДЛЯ ПРОВЕРКИ",
    "03 / REVIEW": "03 / ПРОВЕРКА",
    "Check together": "Проверяем вместе",
    "A person judges the result": "Результат оценивает человек",
    "A REUSABLE TEAM PRACTICE": "СЦЕНАРИЙ ДЛЯ КОМАНДЫ",
    "TEAM TASK": "ЗАДАЧА",
    "AI STEP": "AI-ШАГ",
    "HUMAN REVIEW": "ПРОВЕРКА",
    "SHARED PRACTICE": "ОБЩАЯ ПРАКТИКА",
}


def main() -> None:
    svg_en = "\n".join(parts) + "\n"
    svg_ru = svg_en
    for source, translated in sorted(RU.items(), key=lambda item: len(item[0]), reverse=True):
        svg_ru = svg_ru.replace(escape(source), escape(translated))
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for lang, content in (("en", svg_en), ("ru", svg_ru)):
        target = OUT_DIR / f"workflow-method-{lang}.svg"
        target.write_text(content, encoding="utf-8")
        print(target)


if __name__ == "__main__":
    main()
