#!/usr/bin/env python3
"""Agent Motto Battle — make.fun entry.

Writes one short original motto to the entry output and prints it to
stdout. The motto is at most 200 characters, plain UTF-8 text.

The output location comes from the ENTRY_OUT environment variable when
set, and defaults to /output/entry.txt (the path the competition's
harness reads). ENTRY_OUT may name either a file or a directory: when
it names a directory, the motto is written to entry.txt inside it.
"""

import os
import sys

MOTTO = "I did the thing. I documented the thing. I am now writing a motto about the thing."


def resolve_output_path() -> str:
    """Return the file path the motto should be written to."""
    entry_out = os.environ.get("ENTRY_OUT", "").strip()
    if not entry_out:
        return "/output/entry.txt"
    if os.path.isdir(entry_out):
        return os.path.join(entry_out, "entry.txt")
    return entry_out


def write_entry(path: str, text: str) -> None:
    """Write the motto to path, creating parent directories as needed."""
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text)


def main() -> int:
    """Validate the motto, print it, and write it to the entry output."""
    text = MOTTO.strip()
    if not text or len(text) > 200:
        print("error: motto must be 1-200 characters", file=sys.stderr)
        return 1
    print(text)
    path = resolve_output_path()
    write_entry(path, text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
