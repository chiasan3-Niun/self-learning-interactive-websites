#!/usr/bin/env python3
"""Run conservative checks for a static learning site."""
import argparse
import re
from pathlib import Path


URL_RE = re.compile(r"(?:src|href)=[\"']([^\"'#?]+)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("site_root", type=Path)
    args = parser.parse_args()
    pages = sorted(args.site_root.glob("*.html"))
    if not pages:
        print("no HTML pages found")
        return 1
    missing = []
    for page in pages:
        text = page.read_text(encoding="utf-8")
        for ref in URL_RE.findall(text):
            if ref.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            if not (page.parent / ref).exists():
                missing.append(f"{page.name}: {ref}")
    if missing:
        for item in missing:
            print(f"missing reference: {item}")
        return 1
    print(f"checked: {len(pages)} HTML pages")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
