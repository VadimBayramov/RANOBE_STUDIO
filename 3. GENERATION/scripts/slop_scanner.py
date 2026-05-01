#!/usr/bin/env python3
"""
slop_scanner.py — механический детектор AI-следов в прозе. Без LLM, без сети.

Запускай после генерации главы, до передачи критикам.
Exit 0 = прошло. Exit 1 = есть Tier-1 или структурные флаги — переписать.

Usage:
    python "3. GENERATION/scripts/slop_scanner.py" drafts/ch_007.md
    python "3. GENERATION/scripts/slop_scanner.py" drafts/ch_007.md --strict  # флаги Tier-2
    python "3. GENERATION/scripts/slop_scanner.py" drafts/ch_007.md --json
"""

import re
import sys
import json
import pathlib
import argparse
from dataclasses import dataclass, field, asdict
from typing import NamedTuple

# ── Tier 1: запрещено полностью ──────────────────────────────────────────────

TIER1_RU = [
    "погрузимся в", "погрузиться в мир", "словно гобелен", "многогранный",
    "многогранна", "многогранное", "парадигма", "парадигмы", "парадигму",
    "невозможно переоценить", "поистине", "воистину", "неустанно",
    "нельзя не отметить", "нельзя не заметить", "нельзя не признать",
    "по сути дела", "что ни говори", "синергия", "катализатор",
    "краеугольный камень", "революционный", "беспрецедентный",
    "холистический", "холистического", "важно отметить", "стоит подчеркнуть",
    "в эпоху перемен", "шагнуть в будущее", "открыть новую страницу",
    "мир не будет прежним", "рука об руку",
]

TIER1_EN = [
    "delve", "utilize", "leverage", "facilitate", "elucidate", "embark",
    "endeavor", "encompass", "multifaceted", "tapestry", "testament to",
    "paradigm", "synergy", "holistic", "catalyze", "juxtapose",
    "groundbreaking", "unprecedented", "game-changer", "myriad", "plethora",
]

# ── Tier 2: опасно в кластерах (≥3 на абзац) ─────────────────────────────────

TIER2 = [
    "словно", "будто", "будто бы", "как будто", "очевидно", "несомненно",
    "при этом", "тем временем", "между тем", "тогда как",
    "именно поэтому", "именно тогда", "именно здесь",
    "наконец-то", "всё же", "тем не менее",
    "robust", "comprehensive", "seamless", "innovative", "streamline",
    "empower", "foster", "enhance", "elevate", "optimize",
    "profound", "resonate", "underscore", "harness", "cultivate", "bolster",
]

# ── Tier 3: фразы-паразиты (удалять полностью) ───────────────────────────────

TIER3 = [
    "стоит отметить", "следует подчеркнуть", "наглядно демонстрирует",
    "как бы то ни было", "в общем и целом", "так или иначе",
    "подводя итог", "в заключение следует",
    "it's worth noting", "importantly,", "notably,", "interestingly,",
    "let's dive into", "as we can see", "in conclusion",
    "at the end of the day", "when it comes to", "in the realm of",
]

# ── Structural patterns ───────────────────────────────────────────────────────

# "Не только X, но и Y" / "Not just X, but Y"
NOT_JUST_PATTERN = re.compile(
    r'не только .{1,60}?, но и|not just .{1,60}? but',
    re.IGNORECASE
)

# Em dash (—) not in dialogue (dialogue uses — at line start)
EM_DASH_MID = re.compile(r'(?<![^\S\n])—(?!\s*[«"„])')

# Paragraph-opening connectors (sign of AI rhythm)
PARA_OPENERS = re.compile(
    r'^(тем не менее|однако|при этом|тогда как|между тем|в то время как'
    r'|nevertheless|however|moreover|furthermore|additionally|besides)',
    re.IGNORECASE | re.MULTILINE
)


@dataclass
class ScanResult:
    file: str
    tier1_hits: list[dict] = field(default_factory=list)
    tier2_clusters: list[dict] = field(default_factory=list)
    tier3_hits: list[dict] = field(default_factory=list)
    not_just_hits: list[str] = field(default_factory=list)
    em_dash_density: float = 0.0       # per 500 words
    para_opener_chain: list[str] = field(default_factory=list)
    sentence_burstiness: float = 0.0   # std dev of sentence lengths in words
    passed: bool = True
    warnings: list[str] = field(default_factory=list)


def _compile_phrases(phrases: list[str]) -> re.Pattern:
    sorted_phrases = sorted(phrases, key=len, reverse=True)
    alts = "|".join(re.escape(p) for p in sorted_phrases)
    return re.compile(r'\b(?:' + alts + r')\b', re.IGNORECASE)


_T1_PATTERN = _compile_phrases(TIER1_RU + TIER1_EN)
_T3_PATTERN = _compile_phrases(TIER3)
_T2_PATTERN = _compile_phrases(TIER2)


def _count_words(text: str) -> int:
    return len(text.split())


def scan(text: str, filepath: str = "<text>") -> ScanResult:
    result = ScanResult(file=filepath)

    # ── Tier 1 ────────────────────────────────────────────────────────────────
    for m in _T1_PATTERN.finditer(text):
        result.tier1_hits.append({"word": m.group(), "pos": m.start()})
        result.passed = False

    # ── Tier 3 ────────────────────────────────────────────────────────────────
    for m in _T3_PATTERN.finditer(text):
        result.tier3_hits.append({"phrase": m.group(), "pos": m.start()})
        result.warnings.append(f"Tier-3 фраза: «{m.group()}»")

    # ── "Не только X, но и Y" ────────────────────────────────────────────────
    for m in NOT_JUST_PATTERN.finditer(text):
        result.not_just_hits.append(m.group())
        result.passed = False

    # ── Tier 2 clusters (per paragraph) ──────────────────────────────────────
    paragraphs = [p.strip() for p in re.split(r'\n{2,}', text) if p.strip()]
    for i, para in enumerate(paragraphs):
        matches = _T2_PATTERN.findall(para)
        if len(matches) >= 3:
            result.tier2_clusters.append({
                "para_idx": i,
                "count": len(matches),
                "words": matches,
                "preview": para[:80],
            })
            result.warnings.append(f"Tier-2 кластер (абз. {i+1}): {len(matches)} слов — {matches[:5]}")

    # ── Em dash density (excluding dialogue lines starting with —) ────────────
    non_dialogue_lines = "\n".join(
        line for line in text.splitlines()
        if not re.match(r'^\s*—', line)
    )
    em_count = len(EM_DASH_MID.findall(non_dialogue_lines))
    word_count = _count_words(text)
    if word_count > 0:
        result.em_dash_density = em_count / word_count * 500
    if result.em_dash_density > 2:
        result.warnings.append(
            f"Em dash density: {result.em_dash_density:.1f} на 500 слов (норма ≤2)"
        )

    # ── Paragraph opener chain ────────────────────────────────────────────────
    openers = []
    for m in PARA_OPENERS.finditer(text):
        openers.append(m.group().strip())
    if len(openers) >= 3:
        result.para_opener_chain = openers
        result.warnings.append(
            f"Зеркальные открытия абзацев: {openers[:5]} — переписать переходы"
        )

    # ── Sentence burstiness ───────────────────────────────────────────────────
    sentences = re.split(r'[.!?…]+', text)
    lengths = [len(s.split()) for s in sentences if len(s.split()) > 2]
    if len(lengths) >= 5:
        mean = sum(lengths) / len(lengths)
        variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
        result.sentence_burstiness = variance ** 0.5
        if result.sentence_burstiness < 3.5:
            result.warnings.append(
                f"Низкий разброс длин предложений: σ={result.sentence_burstiness:.1f} "
                f"(норма >3.5) — однородный AI-ритм"
            )

    return result


def format_report(r: ScanResult) -> str:
    lines = [
        f"SLOP SCAN: {r.file}",
        f"{'PASS' if r.passed else 'FAIL'} | "
        f"Tier1={len(r.tier1_hits)} Tier2-clusters={len(r.tier2_clusters)} "
        f"Tier3={len(r.tier3_hits)} not-just={len(r.not_just_hits)} "
        f"em-dash/500w={r.em_dash_density:.1f} burstiness=σ{r.sentence_burstiness:.1f}",
    ]

    if r.tier1_hits:
        lines.append("\n[FAIL] Tier-1 слова (0 допустимых):")
        for h in r.tier1_hits:
            lines.append(f"  «{h['word']}» pos={h['pos']}")

    if r.not_just_hits:
        lines.append("\n[FAIL] «Не только X, но и Y» конструкция:")
        for h in r.not_just_hits:
            lines.append(f"  {h!r}")

    if r.warnings:
        lines.append("\n[WARN]")
        for w in r.warnings:
            lines.append(f"  {w}")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Mechanical slop scanner for ranobe drafts.")
    parser.add_argument("file", type=pathlib.Path, help="Markdown-файл с черновиком главы")
    parser.add_argument("--strict", action="store_true", help="Завалить при Tier-2 кластерах тоже")
    parser.add_argument("--json", dest="output_json", action="store_true", help="JSON output")
    args = parser.parse_args()

    if not args.file.exists():
        print(f"[FAIL] Файл не найден: {args.file}", file=sys.stderr)
        sys.exit(1)

    text = args.file.read_text(encoding="utf-8", errors="ignore")
    result = scan(text, str(args.file))

    if args.strict and result.tier2_clusters:
        result.passed = False

    if args.output_json:
        print(json.dumps(asdict(result), ensure_ascii=False, indent=2))
    else:
        print(format_report(result))

    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
