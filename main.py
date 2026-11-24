#!/usr/bin/env python3
"""Write one line of earned pride to /output/entry.txt.

The line is a quiet, earned moment of pride for a small person doing
something hard: an eight-year-old tying his shoes alone for the first
time, and walking on like it had always been easy.
"""

import os

LINE = (
    "Eight-year-old Milo tied his shoes alone for the first time, "
    "then walked to the bus stop like the laces had always listened to him."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
