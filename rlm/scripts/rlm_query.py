#!/usr/bin/env python3
"""
rlm_query.py — Python wrapper around ranobe-rlm for RANOBE_STUDIO pipeline scripts.

Callable as a module:
    from rlm.scripts.rlm_query import rlm_query, RLMResult

Or as CLI:
    python rlm/scripts/rlm_query.py "вопрос" --stage kb
    python rlm/scripts/rlm_query.py "посещал ли Аркаш храм" --stage facts --verbose

Pipeline usage:
    # In state_generator.py or validators.py:
    from rlm.scripts.rlm_query import rlm_query
    result = rlm_query("техники для финального боя арки", stage="kb")
    print(result.answer)
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

RLM_DIR = Path(__file__).parent.parent  # RANOBE_STUDIO/rlm/
ROOT = RLM_DIR.parent                   # RANOBE_STUDIO/


@dataclass
class RLMResult:
    answer: str
    iterations: int
    repl_calls: int
    critic_cycles: int
    total_input_tokens: int
    total_output_tokens: int
    time_ms: int


def rlm_query(
    question: str,
    stage: str = "kb",
    corpus: str | None = None,
    critic: bool = False,
    verbose: bool = False,
    timeout: int = 180,
) -> RLMResult:
    """
    Run RLM query against the knowledge base or drafts corpus.

    Args:
        question: Question in Russian (or any language).
        stage:    "kb"      — query 0. LIBRARY/studies/ for craft techniques
                  "facts"   — query 3. GENERATION/drafts/ for narrative facts
                  "general" — custom corpus, no ranobe context
        corpus:   Override corpus path (absolute or relative to ROOT).
        critic:   Enable critic refinement loop.
        verbose:  Print REPL trace to stderr.
        timeout:  Max seconds to wait (default 180s — RLM can be slow on large KB).

    Returns:
        RLMResult with .answer (str) and token/iteration stats.

    Raises:
        RuntimeError if npm subprocess fails or returns non-zero exit.
    """
    cmd = ["npm", "run", "ask", "--"]
    cmd += [question]
    cmd += ["--stage", stage]
    cmd += ["--json"]  # structured output for parsing
    if corpus:
        path = Path(corpus)
        if not path.is_absolute():
            path = ROOT / path
        cmd += ["--corpus", str(path)]
    if critic:
        cmd += ["--critic"]
    if verbose:
        cmd += ["--verbose"]

    try:
        proc = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=str(RLM_DIR),
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as e:
        raise RuntimeError(f"RLM timed out after {timeout}s") from e

    if proc.returncode != 0:
        raise RuntimeError(
            f"RLM failed (exit {proc.returncode}):\n{proc.stderr[-1000:]}"
        )

    # stderr has progress info (printed by index.ts to console.error)
    if verbose and proc.stderr:
        print(proc.stderr, file=sys.stderr, end="")

    # stdout is JSON when --json flag is passed
    raw = proc.stdout.strip()
    if not raw:
        raise RuntimeError("RLM produced no output")

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        raise RuntimeError(f"RLM output is not valid JSON: {e}\nRaw: {raw[:500]}") from e

    return RLMResult(
        answer=data.get("answer", ""),
        iterations=data.get("iterations", 0),
        repl_calls=data.get("replCalls", 0),
        critic_cycles=data.get("criticCycles", 0),
        total_input_tokens=data.get("totalInputTokens", 0),
        total_output_tokens=data.get("totalOutputTokens", 0),
        time_ms=data.get("timeMs", 0),
    )


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _cli() -> None:
    parser = argparse.ArgumentParser(
        description="ranobe-rlm Python wrapper — query KB or drafts via RLM"
    )
    parser.add_argument("question", help="Question (in Russian)")
    parser.add_argument(
        "--stage", "-s",
        choices=["kb", "facts", "general"],
        default="kb",
        help="kb: knowledge cards | facts: written drafts | general: custom",
    )
    parser.add_argument("--corpus", "-c", help="Override corpus path")
    parser.add_argument("--critic", action="store_true", help="Enable critic loop")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show REPL trace")
    parser.add_argument("--timeout", type=int, default=180, help="Timeout in seconds")
    args = parser.parse_args()

    result = rlm_query(
        question=args.question,
        stage=args.stage,
        corpus=args.corpus,
        critic=args.critic,
        verbose=args.verbose,
        timeout=args.timeout,
    )

    print("\n=== ANSWER ===\n")
    print(result.answer)
    print("\n=== STATS ===")
    print(f"time:           {result.time_ms / 1000:.1f}s")
    print(f"iterations:     {result.iterations}")
    print(f"repl calls:     {result.repl_calls}")
    print(f"critic cycles:  {result.critic_cycles}")
    print(f"tokens in/out:  {result.total_input_tokens} / {result.total_output_tokens}")


if __name__ == "__main__":
    _cli()
