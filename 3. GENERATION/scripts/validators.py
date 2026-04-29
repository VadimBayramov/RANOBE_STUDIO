#!/usr/bin/env python3
"""
validators.py — валидаторы перед pipeline-шагами.

bible_validator : проверяет что все поля bible/ заполнены (до перехода к Слою 2)
state_validator : проверяет state_ch_N.yaml на 4 инварианта (до генерации главы)

Usage:
    python "3. GENERATION/scripts/validators.py" bible
    python "3. GENERATION/scripts/validators.py" state --chapter 7
    # через мастер: python scripts/sync.py --validate bible
"""

import pathlib
import yaml
import argparse
import sys

ROOT = pathlib.Path(__file__).parent.parent.parent  # RANOBE_STUDIO/
BIBLE_DIR = ROOT / "1. DESIGN_IDEA" / "1.3 BIBLE"
STATES_DIR = ROOT / "3. GENERATION" / "scene_plans"

BIBLE_REQUIRED = ["premise.md", "world.md", "characters.md", "arcs.md", "tone.md", "canon.md"]
STATE_INVARIANTS = [
    "chapter",
    "characters",
    "last_beat",
    "open_loops",
]


def validate_bible() -> bool:
    print("=== Bible Validator ===")
    ok = True
    for fname in BIBLE_REQUIRED:
        fpath = BIBLE_DIR / fname
        if not fpath.exists():
            print(f"  [FAIL] Отсутствует: {fname}")
            ok = False
            continue
        text = fpath.read_text(errors="ignore").strip()
        if len(text) < 50:
            print(f"  [WARN] Слишком короткий: {fname} ({len(text)} chars)")
        else:
            print(f"  [OK]   {fname}")
    if ok:
        print("Bible: PASS — можно переходить к Слою 2")
    else:
        print("Bible: FAIL — заполни все файлы перед планированием")
    return ok


def validate_state(chapter: int) -> bool:
    print(f"=== State Validator — глава {chapter} ===")
    # Try to find state file
    state_path = ROOT / "3. GENERATION" / f"state_ch_{chapter}.yaml"
    if not state_path.exists():
        # Also check scene_plans/
        state_path = ROOT / "3. GENERATION" / "scene_plans" / f"state_ch_{chapter}.yaml"
    if not state_path.exists():
        print(f"  [FAIL] state_ch_{chapter}.yaml не найден")
        return False

    try:
        data = yaml.safe_load(state_path.read_text())
    except yaml.YAMLError as e:
        print(f"  [FAIL] YAML parse error: {e}")
        return False

    ok = True
    for field in STATE_INVARIANTS:
        if field not in data:
            print(f"  [FAIL] Поле отсутствует: {field}")
            ok = False
        else:
            print(f"  [OK]   {field}")

    if ok:
        print(f"State ch.{chapter}: PASS")
    else:
        print(f"State ch.{chapter}: FAIL — используй state_generator.py для генерации")
    return ok


def main():
    parser = argparse.ArgumentParser(description="RANOBE_STUDIO validators.")
    parser.add_argument("target", choices=["bible", "state"])
    parser.add_argument("--chapter", type=int, default=1)
    args = parser.parse_args()

    if args.target == "bible":
        ok = validate_bible()
    else:
        ok = validate_state(args.chapter)

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
