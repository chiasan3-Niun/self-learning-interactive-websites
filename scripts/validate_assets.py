#!/usr/bin/env python3
"""Validate manifest paths against a project root."""
import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", required=True, type=Path)
    parser.add_argument("--root", required=True, type=Path)
    args = parser.parse_args()
    data = json.loads(args.manifest.read_text(encoding="utf-8"))
    entries = data if isinstance(data, list) else data.get("items", data.get("files", []))
    missing = []
    for entry in entries:
        path = entry if isinstance(entry, str) else entry.get("image") or entry.get("audio") or entry.get("path")
        if path and not (args.root / path).is_file():
            missing.append(path)
    if missing:
        for path in missing:
            print(f"missing asset: {path}")
        return 1
    print(f"validated: {len(entries)} manifest entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
