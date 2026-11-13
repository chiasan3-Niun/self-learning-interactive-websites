#!/usr/bin/env python3
"""Create a deterministic inventory of files under a source directory."""
import argparse
import json
from pathlib import Path

SUPPORTED = {".docx", ".txt", ".md", ".csv", ".json", ".jpg", ".jpeg", ".png", ".webp", ".wav", ".mp3", ".m4a", ".ogg"}


def scan(root: Path) -> dict:
    files = []
    warnings = []
    stems = {}
    for path in sorted(p for p in root.rglob("*") if p.is_file()):
        rel = path.relative_to(root).as_posix()
        suffix = path.suffix.lower()
        if suffix not in SUPPORTED:
            warnings.append(f"skipped unsupported file: {rel}")
            continue
        entry = {"path": rel, "type": suffix[1:], "bytes": path.stat().st_size}
        files.append(entry)
        stems.setdefault(path.stem.lower(), []).append(rel)
    for stem, paths in sorted(stems.items()):
        if len(paths) > 1:
            warnings.append(f"duplicate stem '{stem}': {', '.join(paths)}")
    return {"root": str(root), "files": files, "warnings": warnings}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("root", type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = scan(args.root)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"inventory: {len(result['files'])} supported files")
    for warning in result["warnings"]:
        print(f"warning: {warning}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
