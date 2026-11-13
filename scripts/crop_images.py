#!/usr/bin/env python3
"""Create derived crops from an explicit crop map; never overwrite inputs."""
import argparse
import json
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--crop-map", required=True, type=Path)
    args = parser.parse_args()
    try:
        from PIL import Image
    except ImportError as exc:
        raise SystemExit("Pillow is required for image cropping: python -m pip install Pillow") from exc
    crop_map = json.loads(args.crop_map.read_text(encoding="utf-8"))
    args.output.mkdir(parents=True, exist_ok=True)
    for source_name, box in crop_map.items():
        if not isinstance(box, list) or len(box) != 4:
            raise SystemExit(f"crop box must be [left, top, right, bottom]: {source_name}")
        source = args.input / source_name
        if not source.is_file():
            raise SystemExit(f"missing source image: {source_name}")
        destination = args.output / source_name
        destination.parent.mkdir(parents=True, exist_ok=True)
        with Image.open(source) as image:
            image.crop(tuple(box)).save(destination)
        print(f"created: {destination}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
