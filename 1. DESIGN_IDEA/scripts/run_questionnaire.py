#!/usr/bin/env python3
"""
run_questionnaire.py — CLI для сбора ответов на вопросы онбординга.

Читает MANIFEST.md из questionnaire/ → активные вопросы → интерактивный диалог →
заполняет PROMPT_IDEA.md из template.md.

Usage:
    python "1. DESIGN_IDEA/scripts/run_questionnaire.py"
    python "1. DESIGN_IDEA/scripts/run_questionnaire.py" --manifest "1. DESIGN_IDEA/1.1 PROMPT_IDEA/questionnaire/MANIFEST.md"
    python "1. DESIGN_IDEA/scripts/run_questionnaire.py" --mode auto  # LLM заполняет сам
    # через мастер: python scripts/sync.py --questionnaire
"""

import pathlib
import argparse

ROOT = pathlib.Path(__file__).parent.parent.parent  # RANOBE_STUDIO/
QUESTIONNAIRE_DIR = ROOT / "1. DESIGN_IDEA" / "1.1 PROMPT_IDEA" / "questionnaire"
TEMPLATE_PATH = ROOT / "1. DESIGN_IDEA" / "1.1 PROMPT_IDEA" / "template.md"
OUTPUT_DIR = ROOT / "1. DESIGN_IDEA" / "1.1 PROMPT_IDEA"


def load_active_questions(manifest_path: pathlib.Path) -> list[pathlib.Path]:
    """Parse MANIFEST.md — active (not commented) question files."""
    questions = []
    for line in manifest_path.read_text().splitlines():
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        if "questions/" in line:
            q_file = QUESTIONNAIRE_DIR / "questions" / line.split("questions/")[-1].strip()
            if q_file.exists():
                questions.append(q_file)
    return questions


def main():
    parser = argparse.ArgumentParser(description="Run RANOBE_STUDIO onboarding questionnaire.")
    parser.add_argument("--manifest", default=str(QUESTIONNAIRE_DIR / "MANIFEST.md"))
    parser.add_argument("--mode", choices=["interview", "auto"], default="interview")
    args = parser.parse_args()

    manifest = pathlib.Path(args.manifest)
    if not manifest.exists():
        print(f"[ERROR] Manifest not found: {manifest}")
        return

    questions = load_active_questions(manifest)
    print(f"Active questions: {len(questions)}")

    if args.mode == "auto":
        print("MODE AUTO: передай template.md в LLM с твоей идеей — он заполнит всё сам.")
        print(f"Template: {TEMPLATE_PATH.relative_to(ROOT)}")
        return

    # TODO: MODE INTERVIEW — интерактивный CLI-диалог по вопросам
    print("MODE INTERVIEW:")
    for i, q_path in enumerate(questions, 1):
        print(f"\n[{i}/{len(questions)}] {q_path.stem}")
        print(q_path.read_text()[:500])
        answer = input("Ответ (Enter = пропустить): ").strip()
        print(f"  → сохранено: {answer[:80] if answer else '(пусто)'}")

    print(f"\nГотово. Результат → {OUTPUT_DIR}/PROMPT_IDEA.md")
    print("TODO: реализовать сборку PROMPT_IDEA.md из ответов")


if __name__ == "__main__":
    main()
