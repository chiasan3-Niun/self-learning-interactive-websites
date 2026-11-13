#!/usr/bin/env python3
"""Normalize a user-confirmed content JSON without changing its text."""
import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    data = json.loads(args.input.read_text(encoding="utf-8"))
    if not isinstance(data, (dict, list)):
        raise SystemExit("input must be a JSON object or array")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"manifest written: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
