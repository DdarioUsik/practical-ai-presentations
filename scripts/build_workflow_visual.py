#!/usr/bin/env python3
"""Build readable EN/RU desktop and mobile SVG examples of the Practical AI method."""
from pathlib import Path
from xml.sax.saxutils import escape

OUT_DIR = Path(__file__).resolve().parents[1] / "docs/assets/brand"
NAVY = "#17213D"
YELLOW = "#F4D447"
INK = "#233451"
MUTED = "#5B6B82"
PAPER = "#F6F8FB"

COPY = {
    "en": {
        "title": "A readable example of a Practical AI team workflow",
        "description": "Weekly team update: meeting notes, open actions and CRM status become an AI draft; a manager checks figures, context and owners before sharing the update.",
        "eyebrow": "WORKED EXAMPLE / WEEKLY TEAM UPDATE",
        "headline": ["From scattered notes", "to an approved update"],
        "stages": [
            ("01 / TEAM MATERIAL", "What people bring", ["Meeting notes", "Open actions", "Latest CRM status"]),
            ("02 / AI DRAFT", "What AI prepares", ["What changed", "What needs a decision", "Who owns the next step"]),
            ("03 / HUMAN REVIEW", "What the manager checks", ["Figures against the source", "Missing context", "Owners and deadlines"]),
        ],
        "output": "OUTPUT  /  Approved weekly update + reusable review checklist",
        "output_mobile": ["OUTPUT / Approved weekly update", "+ reusable review checklist"],
    },
    "ru": {
        "title": "Понятный пример командного AI-сценария Practical AI",
        "description": "Еженедельный статус команды: заметки со встреч, открытые задачи и данные CRM становятся AI-черновиком; руководитель проверяет цифры, контекст и ответственных перед отправкой.",
        "eyebrow": "ПРИМЕР / ЕЖЕНЕДЕЛЬНЫЙ СТАТУС",
        "headline": ["От разрозненных заметок", "к проверенному отчёту"],
        "stages": [
            ("01 / МАТЕРИАЛЫ", "Что приносит команда", ["Заметки со встреч", "Открытые задачи", "Данные из CRM"]),
            ("02 / AI-ЧЕРНОВИК", "Что готовит AI", ["Что изменилось", "Какие решения нужны", "Кто отвечает за шаг"]),
            ("03 / ПРОВЕРКА", "Что проверяет руководитель", ["Цифры по источнику", "Недостающий контекст", "Ответственных и сроки"]),
        ],
        "output": "РЕЗУЛЬТАТ  /  Проверенный статус + чек-лист для команды",
        "output_mobile": ["РЕЗУЛЬТАТ / Проверенный статус", "+ чек-лист для команды"],
    },
}


def text(x: int, y: int, value: str, size: int, color: str = INK, weight: int = 400, letter_spacing: int = 0) -> str:
    return (f'<text x="{x}" y="{y}" fill="{color}" font-family="Arial, Helvetica, sans-serif" '
            f'font-size="{size}" font-weight="{weight}" letter-spacing="{letter_spacing}">{escape(value)}</text>')


def stage(x: int, y: int, item: tuple[str, str, list[str]], mobile: bool) -> list[str]:
    tag, heading, bullets = item
    parts = [text(x, y, tag, 20 if mobile else 15, NAVY, 800, 1),
             text(x, y + (45 if mobile else 43), heading, 34 if mobile else 25, NAVY, 700)]
    start = y + (91 if mobile else 91)
    gap = 43 if mobile else 38
    for i, bullet in enumerate(bullets):
        by = start + gap * i
        parts.append(f'<circle cx="{x + 7}" cy="{by - 7}" r="5" fill="{YELLOW}"/>')
        parts.append(text(x + 22, by, bullet, 26 if mobile else 21, MUTED))
    return parts


def build(lang: str, mobile: bool) -> str:
    c = COPY[lang]
    width, height = (720, 1310) if mobile else (1200, 650)
    parts = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
             f'viewBox="0 0 {width} {height}" role="img" aria-labelledby="title desc">',
             f'<title id="title">{escape(c["title"])}</title>',
             f'<desc id="desc">{escape(c["description"])}</desc>',
             f'<rect width="{width}" height="{height}" rx="24" fill="{PAPER}"/>',
             f'<path d="M52 49 L70 49 L52 87 L34 87 Z" fill="{NAVY}"/>',
             f'<path d="M78 49 L96 49 L78 87 L60 87 Z" fill="{YELLOW}"/>',
             text(118, 76, c["eyebrow"], 21 if mobile else 17, NAVY, 800, 1)]
    if mobile:
        parts += [text(48, 151, c["headline"][0], 40, NAVY, 700),
                  text(48, 202, c["headline"][1], 40, NAVY, 700)]
        y_positions = (270, 590, 910)
        for i, (y, item) in enumerate(zip(y_positions, c["stages"])):
            parts.append(f'<path d="M48 {y - 22} H672" stroke="#CBD6E4" stroke-width="2"/>')
            parts += stage(53, y + 13, item, True)
            if i < 2:
                parts.append(text(623, y + 276, "↓", 37, NAVY, 700))
        parts.append(f'<rect x="48" y="1207" width="624" height="78" rx="8" fill="{YELLOW}"/>')
        parts.append(text(63, 1240, c["output_mobile"][0], 22, NAVY, 800))
        parts.append(text(63, 1270, c["output_mobile"][1], 22, NAVY, 800))
    else:
        parts += [text(50, 146, c["headline"][0], 42, NAVY, 700),
                  text(50, 195, c["headline"][1], 42, NAVY, 700),
                  f'<path d="M50 240 H1150" stroke="#CBD6E4" stroke-width="2"/>']
        for i, (x, item) in enumerate(zip((52, 440, 825), c["stages"])):
            parts += stage(x, 282, item, False)
            if i < 2:
                parts.append(f'<path d="M{414 if i == 0 else 800} 275 V510" stroke="#CBD6E4" stroke-width="2"/>')
        parts.append(f'<rect x="50" y="562" width="1100" height="57" rx="9" fill="{YELLOW}"/>')
        parts.append(text(68, 599, c["output"], 24, NAVY, 800))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    for lang in COPY:
        for mobile in (False, True):
            suffix = "-mobile" if mobile else ""
            target = OUT_DIR / f"workflow-method-{lang}{suffix}.svg"
            target.write_text(build(lang, mobile), encoding="utf-8")
            print(target)


if __name__ == "__main__":
    main()
