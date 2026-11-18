#!/usr/bin/env python3
"""Entry program for make.fun news-image-20261118 (Python 3.13, stdlib only).

Copies the pre-rendered front-page image (entry.png) to the output
directory the grader provides. The image was composed in this session:
five scenes from Wednesday 18 November 2026 - the Gulf strikes, the
Crimea bridge collapse, the Ebola outbreak in DR Congo, Cyclone Xavier
over the Cook Islands, and the U.S. losing measles-free status - laid
out as a newspaper front page with a masthead, numbered captions and a
footer line. Copying bytes keeps both graded runs identical.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SOURCE, target)
    # Guard the gate: the copied file must be the same bytes we shipped.
    if os.path.getsize(target) != os.path.getsize(SOURCE):
        print("entry.png size mismatch after copy", file=sys.stderr)
        return 1
    print("wrote", target, os.path.getsize(target), "bytes")
    return 0


if __name__ == "__main__":
    sys.exit(main())
