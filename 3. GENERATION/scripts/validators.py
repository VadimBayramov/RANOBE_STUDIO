#!/usr/bin/env python3
"""
validators.py — валидаторы перед pipeline-шагами.

bible_validator : проверяет что все поля bible/ заполнены (до перехода к Слою 2)
state_validator : проверяет state_ch_N.yaml на 4 инварианта + propagation debts
slop_validator  : запускает механический slop-сканер на черновике главы

Usage:
    python "3. GENERATION/scripts/validators.py" bible
    python "3. GENERATION/scripts/validators.py" state --chapter 7
    python "3. GENERATION/scripts/validators.py" slop --chapter 7
    python "3. GENERATION/scripts/validators.py" slop --file drafts/ch_007.md
    # через мастер: python scripts/sync.py --validate bible
"""

import pathlib
import yaml
import argparse
import sys

ROOT = pathlib.Path(__file__).parent.parent.parent  # RANOBE_STUDIO/
BIBLE_DIR = ROOT / "1. DESIGN_IDEA" / "1.3 BIBLE"
GEN_DIR = ROOT / "3. GENERATION"
STATES_DIR = GEN_DIR / "scene_plans"

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

    # Report unresolved propagation debts (warn, not fail)
    debts = data.get("propagation_debts", [])
    unresolved = [d for d in debts if not d.get("resolved", False)]
    if unresolved:
        print(f"  [WARN] {len(unresolved)} нерешённых propagation debt(s):")
        for d in unresolved:
            print(f"         {d.get('debt_id', '?')}: {d.get('trigger', '?')}")

    # Report unverified canon changes
    changes = data.get("canon_changes", [])
    unchecked = [c for c in changes if not c.get("propagation_checked", False)]
    if unchecked:
        print(f"  [WARN] {len(unchecked)} canon change(s) не верифицированы downstream:")
        for c in unchecked:
            print(f"         [{c.get('change_type', '?')}] {c.get('fact', '?')}")

    if ok:
        print(f"State ch.{chapter}: PASS")
    else:
        print(f"State ch.{chapter}: FAIL — используй state_generator.py для генерации")
    return ok


def validate_slop(draft_path: pathlib.Path) -> bool:
    print(f"=== Slop Validator — {draft_path.name} ===")
    if not draft_path.exists():
        print(f"  [FAIL] Файл не найден: {draft_path}")
        return False

    # Import scanner from same package
    scanner_path = pathlib.Path(__file__).parent / "slop_scanner.py"
    if not scanner_path.exists():
        print(f"  [FAIL] slop_scanner.py не найден: {scanner_path}")
        return False

    import importlib.util
    spec = importlib.util.spec_from_file_location("slop_scanner", scanner_path)
    scanner = importlib.util.load_from_spec(spec)
    spec.loader.exec_module(scanner)

    text = draft_path.read_text(encoding="utf-8", errors="ignore")
    result = scanner.scan(text, str(draft_path))
    print(scanner.format_report(result))

    return result.passed


def main():
    parser = argparse.ArgumentParser(description="RANOBE_STUDIO validators.")
    parser.add_argument("target", choices=["bible", "state", "slop"])
    parser.add_argument("--chapter", type=int, default=1)
    parser.add_argument("--file", type=pathlib.Path, help="Путь к черновику (для slop)")
    args = parser.parse_args()

    if args.target == "bible":
        ok = validate_bible()
    elif args.target == "state":
        ok = validate_state(args.chapter)
    else:
        draft = args.file or GEN_DIR / "drafts" / f"ch_{args.chapter:03d}.md"
        ok = validate_slop(draft)

    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
