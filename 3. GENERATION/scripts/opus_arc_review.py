#!/usr/bin/env python3
"""
opus_arc_review.py — arc-level revision с Claude Opus dual-persona (literary critic +
professor of fiction). Запускай раз на арку (каждые 15-25 глав).

Stopping conditions (из NousResearch/autonovel):
  - Нет major unqualified items
  - ≥50% items стали hedged/qualified ("это цена амбиции")
  - ≤2 items найдено

Usage:
    python "3. GENERATION/scripts/opus_arc_review.py" --arc 1 --chapters 1-15
    python "3. GENERATION/scripts/opus_arc_review.py" --arc 2 --chapters 16-30 --cycle 2
    python "3. GENERATION/scripts/opus_arc_review.py" --files drafts/ch_001.md drafts/ch_002.md
"""

import pathlib
import argparse
import sys
import re
import json
from datetime import datetime

try:
    import anthropic
except ImportError:
    print("[FAIL] pip install anthropic", file=sys.stderr)
    sys.exit(1)

ROOT = pathlib.Path(__file__).parent.parent.parent
DRAFTS_DIR = ROOT / "3. GENERATION" / "drafts"
CRITIQUES_DIR = ROOT / "3. GENERATION" / "critiques"
BIBLE_DIR = ROOT / "1. DESIGN_IDEA" / "1.3 BIBLE"

MODEL = "claude-opus-4-7-20251101"
MAX_TOKENS = 4096

# Статика кешируется — не меняется между циклами ревью одной арки
_SYSTEM_STATIC = """\
Ты — литературный рецензент с двумя голосами. Сначала прочитай весь текст,
затем выдай анализ в двух ролях.

РОЛЬ 1 — ЛИТЕРАТУРНЫЙ КРИТИК:
Оцени как профессиональный рецензент художественной прозы.
Что не работает структурно? Где темп проседает? Где персонажи плоские?
Где читатель потеряется? Будь честным, но справедливым.

РОЛЬ 2 — ПРОФЕССОР БЕЛЛЕТРИСТИКИ:
Оцени с точки зрения ремесла. Голос держится? Сцены имеют G/C/C/C структуру?
Диалог несёт subtext? Open loops закрываются вовремя?

ФОРМАТ ОТВЕТА:
## КРИТИК
[пронумерованный список конкретных проблем с цитатами и номерами глав]

## ПРОФЕССОР
[пронумерованный список с точными замечаниями]

## ВЕРДИКТ
СТОП: [да/нет] — обоснование одной строкой
[если нет СТОП] ПРИОРИТЕТ: [топ-3 проблемы для следующего цикла]

ПРАВИЛА:
- Конкретность: цитируй, называй главу, описывай что именно сломано
- Если не находишь дефектов — говори это прямо, не придумывай
- Не хвали за отсутствие проблем
- Hedged-замечание ("это цена амбиции", "спорное решение") — отмечай [HEDGED]
- Major unqualified issue — проблема без оговорок, требует фикса
"""


def load_chapters(chapter_paths: list[pathlib.Path]) -> str:
    parts = []
    for p in sorted(chapter_paths):
        text = p.read_text(encoding="utf-8", errors="ignore").strip()
        parts.append(f"=== {p.name} ===\n{text}")
    return "\n\n".join(parts)


def _resolve_chapter_range(spec: str) -> list[pathlib.Path]:
    """'1-15' → [drafts/ch_001.md, ..., drafts/ch_015.md] (только существующие)."""
    m = re.match(r'^(\d+)-(\d+)$', spec)
    if not m:
        raise ValueError(f"Формат диапазона: '1-15', получено: {spec!r}")
    start, end = int(m.group(1)), int(m.group(2))
    paths = []
    for n in range(start, end + 1):
        p = DRAFTS_DIR / f"ch_{n:03d}.md"
        if p.exists():
            paths.append(p)
        else:
            print(f"[WARN] Глава не найдена, пропускаю: {p}", file=sys.stderr)
    return paths


def _count_findings(text: str) -> tuple[int, int]:
    """Возвращает (major_unqualified, hedged) из текста ревью."""
    lines = text.splitlines()
    major = hedged = 0
    for line in lines:
        if re.search(r'\[HEDGED\]', line, re.IGNORECASE):
            hedged += 1
        elif re.match(r'^\s*\d+\.', line) and len(line) > 20:
            # Пронумерованный пункт без [HEDGED] = major unqualified
            major += 1
    return major, hedged


def stopping_conditions_met(review_text: str) -> tuple[bool, str]:
    major, hedged = _count_findings(review_text)
    total = major + hedged

    if total <= 2:
        return True, f"≤2 findings ({total} total) — стоп"
    if major == 0:
        return True, "Нет major unqualified items — стоп"
    if total > 0 and hedged / total >= 0.5:
        return True, f"≥50% hedged ({hedged}/{total}) — стоп, это цена амбиции"

    return False, f"{major} major unqualified, {hedged} hedged — продолжать"


def run_review(
    chapter_paths: list[pathlib.Path],
    arc: int,
    cycle: int,
    voice_path: pathlib.Path | None = None,
) -> str:
    client = anthropic.Anthropic()

    manuscript = load_chapters(chapter_paths)
    chapter_names = ", ".join(p.name for p in chapter_paths)

    user_parts = [
        {
            "type": "text",
            "text": f"АРК {arc}, цикл ревью {cycle}. Главы: {chapter_names}\n\n",
        },
        {
            "type": "text",
            "text": manuscript,
        },
    ]

    if voice_path and voice_path.exists():
        voice_text = voice_path.read_text(encoding="utf-8", errors="ignore")
        user_parts.insert(1, {
            "type": "text",
            "text": f"VOICE GUIDE (голос автора):\n{voice_text}\n\n",
            "cache_control": {"type": "ephemeral"},
        })

    response = client.messages.create(
        model=MODEL,
        max_tokens=MAX_TOKENS,
        system=[
            {
                "type": "text",
                "text": _SYSTEM_STATIC,
                "cache_control": {"type": "ephemeral"},
            }
        ],
        messages=[{"role": "user", "content": user_parts}],
    )

    return response.content[0].text


def save_review(arc: int, cycle: int, review_text: str, stop: bool, stop_reason: str) -> pathlib.Path:
    CRITIQUES_DIR.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M")
    out = CRITIQUES_DIR / f"arc_{arc:02d}_cycle_{cycle}_{ts}.md"

    header = f"""---
arc: {arc}
cycle: {cycle}
date: {datetime.now().isoformat()[:10]}
stop: {str(stop).lower()}
stop_reason: "{stop_reason}"
---

"""
    out.write_text(header + review_text, encoding="utf-8")
    return out


def main():
    parser = argparse.ArgumentParser(description="Arc-level Opus dual-persona review.")
    parser.add_argument("--arc", type=int, default=1, help="Номер арки")
    parser.add_argument("--chapters", type=str, help="Диапазон глав: '1-15'")
    parser.add_argument("--files", nargs="+", type=pathlib.Path, help="Явные пути к главам")
    parser.add_argument("--cycle", type=int, default=1, help="Номер цикла ревью (для истории)")
    parser.add_argument("--voice", type=pathlib.Path,
                        default=ROOT / "1. DESIGN_IDEA" / "1.3 BIBLE" / "voice_author.md",
                        help="Путь к voice_author.md (кешируется)")
    args = parser.parse_args()

    if args.files:
        chapters = [p for p in args.files if p.exists()]
    elif args.chapters:
        chapters = _resolve_chapter_range(args.chapters)
    else:
        parser.error("Укажи --chapters '1-15' или --files drafts/ch_001.md ...")

    if not chapters:
        print("[FAIL] Нет доступных глав для ревью", file=sys.stderr)
        sys.exit(1)

    print(f"Arc {args.arc} | Cycle {args.cycle} | {len(chapters)} глав | модель: {MODEL}")
    print("Отправляю в Opus...")

    try:
        review = run_review(chapters, args.arc, args.cycle, args.voice)
    except Exception as e:
        print(f"[FAIL] API error: {e}", file=sys.stderr)
        sys.exit(1)

    stop, reason = stopping_conditions_met(review)
    out_path = save_review(args.arc, args.cycle, review, stop, reason)

    print(f"\n{'=' * 60}")
    print(review)
    print(f"\n{'=' * 60}")
    print(f"Stopping condition: {'СТОП ✓' if stop else 'продолжать'} — {reason}")
    print(f"Сохранено: {out_path}")

    if not stop:
        print(f"\nСледующий цикл:")
        print(f"  python '3. GENERATION/scripts/opus_arc_review.py' "
              f"--arc {args.arc} --chapters {args.chapters or '<range>'} --cycle {args.cycle + 1}")


if __name__ == "__main__":
    main()
