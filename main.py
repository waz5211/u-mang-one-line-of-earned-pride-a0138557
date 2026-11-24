#!/usr/bin/env python3
"""Write one line of earned pride to /output/entry.txt.

The line is a quiet, earned moment of pride for a small person doing
something hard: an eight-year-old tying his shoes alone for the first
time, and walking on like it had always been easy.

Before writing, the line is validated in-process: it must be non-empty,
at most 240 characters, and a single line. A failed check raises
ValueError with a clear message instead of writing bad output.
"""

import os

LINE = (
    "Eight-year-old Milo tied his shoes alone for the first time, "
    "then walked to the bus stop like the laces had always listened to him."
)


def validate_line(line: str) -> None:
    """Raise ValueError if the line is not a valid single-line entry."""
    if not line:
        raise ValueError("entry line must not be empty")
    if len(line) > 240:
        raise ValueError(
            f"entry line is {len(line)} characters, over the 240 limit"
        )
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")


def main() -> None:
    validate_line(LINE)
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
