#!/usr/bin/env python3
"""
RLM REPL server — Algorithm 1 execution layer.
Spawned once by the TypeScript orchestrator as a subprocess.

Protocol (JSON lines via stdin/stdout):
  INIT  stdin  ← {"chunks": [{"id","source","text"}, ...]}
  READY stdout → {"type": "ready"}
  EXEC  stdin  ← {"type": "exec", "code": "..."}
  (mid) stdout → {"type": "sub_rlm", "chunk_id": "...", "question": "..."}
  (mid) stdin  ← {"type": "sub_rlm_result", "result": "..."}
  DONE  stdout → {"type": "result", "stdout": "...", "error": null|"...", "final": null|"..."}
"""
import sys
import io
import json
import re
import traceback

STDOUT_LIMIT = 800  # Algorithm 1: metadata truncation — this is the key design choice

SAFE_BUILTINS = {
    "print": print, "len": len, "range": range, "enumerate": enumerate,
    "list": list, "dict": dict, "set": set, "tuple": tuple,
    "str": str, "int": int, "float": float, "bool": bool,
    "None": None, "True": True, "False": False,
    "min": min, "max": max, "sum": sum, "sorted": sorted, "reversed": reversed,
    "any": any, "all": all, "zip": zip, "map": map, "filter": filter,
    "isinstance": isinstance, "hasattr": hasattr, "getattr": getattr,
    "type": type, "repr": repr, "abs": abs, "round": round,
}


def _make_search(chunks):
    def search(pattern, max_hits=20, flags=re.IGNORECASE):
        try:
            rx = re.compile(pattern, flags)
        except re.error as e:
            return [{"error": f"bad regex: {e}"}]
        out = []
        for c in chunks:
            if rx.search(c["text"]):
                preview = next(
                    (line.strip()[:120] for line in c["text"].split("\n") if rx.search(line)),
                    "",
                )
                out.append({"id": c["id"], "source": c["source"], "preview": preview})
                if len(out) >= max_hits:
                    break
        return out
    return search


def _make_sub_rlm():
    def sub_rlm(chunk_id, question):
        # Write request to real stdout (bypasses our stdout capture)
        sys.__stdout__.write(
            json.dumps({"type": "sub_rlm", "chunk_id": chunk_id, "question": question}) + "\n"
        )
        sys.__stdout__.flush()
        # Block until TypeScript responds with the leaf answer
        raw = sys.__stdin__.readline()
        if not raw:
            return "NOT_FOUND"
        return json.loads(raw).get("result", "NOT_FOUND")
    return sub_rlm


def main():
    init = json.loads(sys.stdin.readline())
    chunks = init["chunks"]

    final_holder: list = [None]

    def FINAL(answer):
        final_holder[0] = str(answer)
        return answer

    namespace = {
        "chunks": chunks,
        "search": _make_search(chunks),
        "sub_rlm": _make_sub_rlm(),
        "FINAL": FINAL,
        "re": re,
        "json": json,
        "__builtins__": SAFE_BUILTINS,
    }

    sys.__stdout__.write(json.dumps({"type": "ready"}) + "\n")
    sys.__stdout__.flush()

    for raw in sys.__stdin__:
        raw = raw.strip()
        if not raw:
            continue

        msg = json.loads(raw)
        if msg["type"] != "exec":
            continue

        code = msg["code"]
        buf = io.StringIO()
        old = sys.stdout
        sys.stdout = buf
        error = None

        try:
            exec(compile(code, "<repl>", "exec"), namespace)  # noqa: S102
        except Exception:
            error = traceback.format_exc(limit=3)
        finally:
            sys.stdout = old

        raw_out = buf.getvalue()

        # Algorithm 1 core: truncate stdout so results must live in REPL variables
        if len(raw_out) > STDOUT_LIMIT:
            preview = (
                raw_out[:STDOUT_LIMIT]
                + f"\n[...{len(raw_out) - STDOUT_LIMIT} chars hidden — store results in variables]"
            )
        else:
            preview = raw_out

        # FINAL detected via function call, not regex — reliable regardless of print() usage
        final = final_holder[0]
        final_holder[0] = None  # reset for next exec

        sys.__stdout__.write(
            json.dumps({"type": "result", "stdout": preview, "error": error, "final": final}) + "\n"
        )
        sys.__stdout__.flush()


if __name__ == "__main__":
    main()
