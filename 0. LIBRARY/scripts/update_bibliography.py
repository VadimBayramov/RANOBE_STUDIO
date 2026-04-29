#!/usr/bin/env python3
"""
Rebuilds BIBLIOGRAPHY.md from all cards in studies/.
Each section = one source (study_ref), with links to all cards derived from it.
Run automatically via PostToolUse hook, or manually: python update_bibliography.py
"""
import re
from pathlib import Path
from collections import defaultdict
from datetime import date

LIBRARY_DIR = Path(__file__).parent.parent
STUDIES_DIR = LIBRARY_DIR / "studies"
OUTPUT = LIBRARY_DIR / "BIBLIOGRAPHY.md"


def parse_frontmatter(text: str) -> dict:
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        if ":" in line:
            key, _, val = line.partition(":")
            fm[key.strip()] = val.strip().strip('"').strip("'")
    return fm


def get_principle(text: str) -> str:
    m = re.search(r"## Принцип\n(.+)", text)
    if m:
        s = m.group(1).strip()
        return (s[:90] + "…") if len(s) > 90 else s
    return ""


def main():
    sources: dict[str, list[dict]] = defaultdict(list)

    for md_file in sorted(STUDIES_DIR.rglob("*.md")):
        text = md_file.read_text(encoding="utf-8")
        fm = parse_frontmatter(text)
        if not fm.get("card_id"):
            continue

        study_ref = fm.get("study_ref", "Unknown source")
        rel_path = md_file.relative_to(LIBRARY_DIR)

        sources[study_ref].append({
            "card_id": fm["card_id"],
            "domain": fm.get("domain", ""),
            "principle": get_principle(text),
            "path": str(rel_path).replace("\\", "/"),
        })

    total_cards = sum(len(v) for v in sources.values())

    lines = [
        "---",
        "id: bibliography",
        "title: Реестр источников",
        f"last_updated: {date.today()}",
        f"sources: {len(sources)}",
        f"cards: {total_cards}",
        "generated_by: scripts/update_bibliography.py",
        "---",
        "",
        "# BIBLIOGRAPHY — Реестр источников",
        "",
        f"> Auto-generated · {len(sources)} источников · {total_cards} карточек · не редактировать вручную.",
        "",
        "---",
        "",
    ]

    for study_ref in sorted(sources.keys()):
        cards = sorted(sources[study_ref], key=lambda c: c["card_id"])
        lines.append(f"## {study_ref}")
        lines.append("")
        for card in cards:
            principle = card["principle"]
            suffix = f" — {principle}" if principle else ""
            lines.append(f"- [{card['card_id']}]({card['path']}){suffix}")
        lines.append("")
        lines.append("---")
        lines.append("")

    OUTPUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"[bibliography] {len(sources)} sources · {total_cards} cards → BIBLIOGRAPHY.md")


if __name__ == "__main__":
    main()
