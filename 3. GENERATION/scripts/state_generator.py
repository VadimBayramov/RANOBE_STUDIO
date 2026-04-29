#!/usr/bin/env python3
"""
state_generator.py — генерация state_ch_N.yaml через structured output (Haiku 4.5).

Принимает описание состояния в свободной форме → выдаёт валидный YAML
по фиксированной JSON schema. Запускай state_validator после.

Правило 2.3 RULES.md: state обновляется ТОЛЬКО через этот скрипт, не через prose.

Usage:
    python "3. GENERATION/scripts/state_generator.py" --chapter 7
    python "3. GENERATION/scripts/state_generator.py" --chapter 7 --from-prev  # на базе предыдущего
    # через мастер: python scripts/sync.py --state --chapter 7
"""

import pathlib
import argparse

ROOT = pathlib.Path(__file__).parent.parent.parent  # RANOBE_STUDIO/

STATE_SCHEMA = {
    "type": "object",
    "required": ["chapter", "characters", "last_beat", "open_loops"],
    "properties": {
        "chapter": {"type": "integer"},
        "characters": {
            "type": "object",
            "description": "Имя персонажа → {location, status, power_level, notes}"
        },
        "last_beat": {
            "type": "string",
            "description": "Последнее событие предыдущей главы (1-2 предложения)"
        },
        "open_loops": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Незакрытые сюжетные петли"
        },
        "canon_refs": {
            "type": "array",
            "items": {"type": "string"},
            "description": "Факты canon.md, релевантные этой главе"
        },
    }
}

# TODO: реализовать через Anthropic SDK
# from anthropic import Anthropic
# client = Anthropic()
# response = client.messages.create(
#     model="claude-haiku-4-5-20251001",
#     max_tokens=1024,
#     system="Generate a state YAML following the schema.",
#     messages=[{"role": "user", "content": user_description}],
#     tools=[{"name": "state_output", "input_schema": STATE_SCHEMA}],
# )


def main():
    parser = argparse.ArgumentParser(description="Generate state_ch_N.yaml via structured output.")
    parser.add_argument("--chapter", type=int, required=True)
    parser.add_argument("--from-prev", action="store_true",
                        help="Load previous chapter state as base")
    args = parser.parse_args()

    print(f"state_generator.py — глава {args.chapter}")
    print("TODO: требует Anthropic API key и реализации")
    print(f"Schema fields: {list(STATE_SCHEMA['properties'].keys())}")
    print(f"После генерации: python '3. GENERATION/scripts/validators.py' state --chapter {args.chapter}")


if __name__ == "__main__":
    main()
