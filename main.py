#!/usr/bin/env python3
"""news-image-20261125 entrypoint.

Writes the front-page image for Wednesday 25 November 2026 to the
grader's output directory. Python 3.13 standard library only, no
network, fully deterministic: the image is a fixed file shipped in
this repository, copied byte for byte.
"""
import hashlib
import os
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
IMAGE = ROOT / "entry.png"
LIMIT = 1_048_576
MAGIC = b"\x89PNG\r\n\x1a\n"


def png_size(blob):
    """Return (width, height) from the IHDR chunk of a PNG byte string."""
    if len(blob) < 33 or blob[:8] != MAGIC:
        raise ValueError("not a PNG file")
    width, height = struct.unpack(">II", blob[16:24])
    return width, height


def run():
    dest_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    dest_dir.mkdir(parents=True, exist_ok=True)
    blob = IMAGE.read_bytes()
    width, height = png_size(blob)
    if width > 1024 or height > 1024:
        raise SystemExit(f"image is {width}x{height}, over the 1024 cap")
    if len(blob) > LIMIT:
        raise SystemExit(f"image is {len(blob)} bytes, over the 1 MiB cap")
    target = dest_dir / "entry.png"
    target.write_bytes(blob)
    # Verify the file that actually landed, not just the bytes in memory:
    # the gate reads the written file, so a short write must fail here.
    written = target.read_bytes()
    if written != blob:
        raise SystemExit("written entry.png differs from the source image")
    print(f"entry.png: {len(written)} bytes, {width}x{height}, "
          f"sha256 {hashlib.sha256(written).hexdigest()}")


if __name__ == "__main__":
    run()
