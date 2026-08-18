#!/usr/bin/env python3
"""Run a command with a hard wall-clock deadline and emit a JSON timing record."""

from __future__ import annotations

import argparse
import json
import subprocess
import time


def main() -> int:
    parser = argparse.ArgumentParser()
    budget = parser.add_mutually_exclusive_group(required=True)
    budget.add_argument("--limit", type=float, help="Hard deadline in seconds from this process start")
    budget.add_argument("--deadline-epoch", type=float, help="Absolute Unix deadline inherited from request start")
    parser.add_argument("--reserve", type=float, default=20.0, help="Seconds reserved for packaging/final response with --deadline-epoch")
    parser.add_argument("command", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    command = args.command[1:] if args.command[:1] == ["--"] else args.command
    if not command:
        parser.error("a command is required after --")

    started = time.monotonic()
    if args.deadline_epoch is not None:
        limit = max(0.0, args.deadline_epoch - time.time() - args.reserve)
    else:
        limit = args.limit
    if limit <= 0:
        print(json.dumps({"elapsed_seconds": 0, "limit_seconds": limit, "timed_out": True,
                          "return_code": 124, "within_budget": False}, ensure_ascii=False))
        return 124
    timed_out = False
    return_code = 124
    try:
        completed = subprocess.run(command, timeout=limit, check=False)
        return_code = completed.returncode
    except subprocess.TimeoutExpired:
        timed_out = True
    elapsed = time.monotonic() - started
    print(json.dumps({
        "elapsed_seconds": round(elapsed, 3),
        "limit_seconds": round(limit, 3),
        "timed_out": timed_out,
        "return_code": return_code,
        "within_budget": not timed_out and elapsed <= limit,
    }, ensure_ascii=False))
    return return_code


if __name__ == "__main__":
    raise SystemExit(main())
