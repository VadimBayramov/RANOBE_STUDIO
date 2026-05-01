#!/usr/bin/env python3
"""
state_generator.py — генерация state_ch_N.yaml через structured output (Haiku 4.5).

Генерирует state для главы N на основе черновика главы N-1.
Правило 2.3 RULES.md: state обновляется ТОЛЬКО через этот скрипт, не через prose.

Usage:
    python "3. GENERATION/scripts/state_generator.py" --chapter 7
    python "3. GENERATION/scripts/state_generator.py" --chapter 7 --from-prev
    python "3. GENERATION/scripts/state_generator.py" --chapter 7 --draft drafts/ch_006.md
"""

import pathlib
import argparse
import sys
import re
import json

try:
    import yaml
except ImportError:
    print("[FAIL] pip install pyyaml", file=sys.stderr)
    sys.exit(1)

try:
    import anthropic
except ImportError:
    print("[FAIL] pip install anthropic", file=sys.stderr)
    sys.exit(1)

ROOT = pathlib.Path(__file__).parent.parent.parent
BIBLE_DIR = ROOT / "1. DESIGN_IDEA" / "1.3 BIBLE"
GEN_DIR = ROOT / "3. GENERATION"
DRAFTS_DIR = GEN_DIR / "drafts"

STATE_SCHEMA = {
    "type": "object",
    "required": ["chapter", "characters", "last_beat", "open_loops"],
    "properties": {
        "chapter": {
            "type": "integer",
            "description": "Номер главы, для которой создаётся state"
        },
        "characters": {
            "type": "object",
            "description": "Имя персонажа (snake_case) → объект с полями status/location/power_level/notes",
            "additionalProperties": {
                "type": "object",
                "properties": {
                    "status": {"type": "string"},
                    "location": {"type": "string"},
                    "power_level": {"type": "integer"},
                    "last_seen": {"type": "integer"},
                    "notes": {"type": "string"},
                }
            }
        },
        "last_beat": {
            "type": "string",
            "description": "Последнее событие предыдущей главы (1-2 предложения, прошедшее время)"
        },
        "open_loops": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Активные сюжетные петли, не более 5 (ID из loops.md)"
        },
        "arc_conflict": {
            "type": "string",
            "description": "Текущий главный конфликт арки (одна строка)"
        },
        "canon_refs": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Факты canon.md, важные для следующей главы (коды: world_rule_NNN, имена и т.д.)"
        },
        "canon_changes": {
            "type": "array",
            "description": "Новые канон-факты, появившиеся в этой главе. Пусто если ничего нового.",
            "items": {
                "type": "object",
                "required": ["fact", "chapter", "change_type"],
                "properties": {
                    "fact": {
                        "type": "string",
                        "description": "Описание факта одной строкой"
                    },
                    "chapter": {"type": "integer"},
                    "change_type": {
                        "type": "string",
                        "enum": ["reveal", "new_rule", "retcon"],
                        "description": "reveal=раскрытие, new_rule=новое правило мира, retcon=правка существующего"
                    },
                    "propagation_checked": {
                        "type": "boolean",
                        "description": "true когда downstream-файлы (arcs, outline, characters) проверены"
                    }
                }
            }
        },
        "propagation_debts": {
            "type": "array",
            "description": "Изменения требующие ревизии downstream. Пусто если ничего.",
            "items": {
                "type": "object",
                "required": ["debt_id", "trigger", "affects", "resolved"],
                "properties": {
                    "debt_id": {
                        "type": "string",
                        "description": "PD-NNN"
                    },
                    "trigger": {
                        "type": "string",
                        "description": "Что изменилось (одна строка)"
                    },
                    "affects": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Список файлов/секций требующих проверки: 'bible/arcs.md#фаза-3'"
                    },
                    "resolved": {
                        "type": "boolean",
                        "description": "false пока не проверено вручную"
                    }
                }
            }
        }
    }
}

_SYSTEM = """\
Ты — state_generator для ранобэ-проекта.
Задача: сгенерировать структурированный YAML-state главы N на основе черновика главы N-1.

Инварианты:
- open_loops: строго не более 5 активных петель
- power_level персонажей: не превышает max_power_tier из canon.md
- last_beat: ровно 1-2 предложения, прошедшее время, конкретное событие
- canon_changes: ТОЛЬКО если в главе явно появился новый факт которого не было до
- propagation_debts: только для изменений с downstream-эффектом
  (смерть/рождение персонажа, изменение правила мира, major reveal с последствиями)
- Если ничего не изменилось — canon_changes и propagation_debts = пустые массивы"""


def _load_canon_max_tier() -> int:
    canon = BIBLE_DIR / "canon.md"
    if not canon.exists():
        return 9
    m = re.search(r'max_power_tier:\s*(\d+)', canon.read_text())
    return int(m.group(1)) if m else 9


def _find_state(chapter: int) -> pathlib.Path | None:
    for d in [GEN_DIR, GEN_DIR / "scene_plans"]:
        p = d / f"state_ch_{chapter}.yaml"
        if p.exists():
            return p
    return None


def _build_message(chapter: int, draft_text: str, from_prev: bool) -> str:
    parts = [f"Черновик главы {chapter - 1} (на основе которой строим state для гл. {chapter}):\n\n{draft_text}"]

    if from_prev:
        prev = _find_state(chapter - 1)
        if prev:
            parts.append(f"\nState предыдущей главы ({chapter - 1}):\n{prev.read_text()}")

    canon = BIBLE_DIR / "canon.md"
    if canon.exists():
        parts.append(f"\ncanon.md:\n{canon.read_text()}")

    parts.append(f"\nСгенерируй state_ch_{chapter}.yaml.")
    return "\n".join(parts)


def _generate(chapter: int, draft_text: str, from_prev: bool) -> dict:
    client = anthropic.Anthropic()

    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=_SYSTEM,
        messages=[{"role": "user", "content": _build_message(chapter, draft_text, from_prev)}],
        tools=[{
            "name": "state_output",
            "description": "Структурированный state следующей главы",
            "input_schema": STATE_SCHEMA,
        }],
        tool_choice={"type": "tool", "name": "state_output"},
    )

    tool_block = next(b for b in response.content if b.type == "tool_use")
    state = tool_block.input

    # Enforce canon power invariant
    max_tier = _load_canon_max_tier()
    for name, char in state.get("characters", {}).items():
        if isinstance(char, dict) and char.get("power_level", 0) > max_tier:
            print(f"[WARN] {name}.power_level обрезан до max_power_tier={max_tier}", file=sys.stderr)
            char["power_level"] = max_tier

    # Enforce open_loops ≤ 5
    loops = state.get("open_loops", [])
    if len(loops) > 5:
        print(f"[WARN] open_loops обрезан с {len(loops)} до 5", file=sys.stderr)
        state["open_loops"] = loops[:5]

    # Default propagation_checked = false for new canon_changes
    for change in state.get("canon_changes", []):
        change.setdefault("propagation_checked", False)

    # Default resolved = false for new debts
    for debt in state.get("propagation_debts", []):
        debt.setdefault("resolved", False)

    return state


def main():
    parser = argparse.ArgumentParser(description="Generate state_ch_N.yaml via Haiku structured output.")
    parser.add_argument("--chapter", type=int, required=True, help="Номер главы (для которой создаём state)")
    parser.add_argument("--from-prev", action="store_true", help="Загрузить state предыдущей главы как базу")
    parser.add_argument("--draft", type=pathlib.Path, help="Путь к черновику (default: drafts/ch_<N-1>.md)")
    args = parser.parse_args()

    draft_path = args.draft or DRAFTS_DIR / f"ch_{args.chapter - 1:03d}.md"
    if not draft_path.exists():
        print(f"[FAIL] Черновик не найден: {draft_path}", file=sys.stderr)
        sys.exit(1)

    print(f"Генерирую state_ch_{args.chapter}.yaml на основе {draft_path.name}...")

    try:
        state = _generate(args.chapter, draft_path.read_text(), args.from_prev)
    except Exception as e:
        print(f"[FAIL] API error: {e}", file=sys.stderr)
        sys.exit(1)

    out_path = GEN_DIR / f"state_ch_{args.chapter}.yaml"
    out_path.write_text(
        yaml.dump(state, allow_unicode=True, default_flow_style=False, sort_keys=False),
        encoding="utf-8",
    )
    print(f"[OK] {out_path}")

    debts = state.get("propagation_debts", [])
    if debts:
        print(f"\n[!] {len(debts)} propagation debt(s) — нужна ревизия downstream:")
        for d in debts:
            print(f"  {d['debt_id']}: {d['trigger']}")
            for a in d.get("affects", []):
                print(f"    → {a}")

    changes = state.get("canon_changes", [])
    if changes:
        print(f"\n[!] {len(changes)} новых canon-фактов — добавь в bible/canon.md:")
        for c in changes:
            print(f"  [{c['change_type']}] {c['fact']}")

    print(f"\nДальше: python '3. GENERATION/scripts/validators.py' state --chapter {args.chapter}")


if __name__ == "__main__":
    main()
