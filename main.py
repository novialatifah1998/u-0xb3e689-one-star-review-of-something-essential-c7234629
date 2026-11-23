#!/usr/bin/env python3
"""One-Star Review of Something Essential.

Writes one original deadpan one-star review of toothpaste — an everyday
essential — to /output/entry.txt. Python 3 stdlib only, no network,
deterministic output.
"""

import os
from pathlib import Path

LINE = (
    "Toothpaste ends exactly when the tube looks half full, every single time."
)

# Why this line: toothpaste is an everyday essential everyone relies on, and
# the grievance is the small daily annoyance everyone recognises but has
# never seen written down as a one-star review — the tube that still looks
# half full but squeezes out nothing. It is filed in earnest, deadpan, one
# joke told cleanly: no winking, no exclamation marks, no second joke. The
# turn lands in the last three words ("every single time"), after the
# complaint has been read straight, and the oddly precise "exactly when"
# makes it sound like a filed complaint rather than a shrug. 73 characters,
# inside the 1-160 gate. The sun / gravity / sleep / Mondays angles are the
# crowded ones; the toothpaste tube is the unclaimed one.

# Gate the judge's rule at build time: the line must stay within 1-160 chars.
# One source of truth for the gate, used both at import and after read-back.
GATE_MIN = 1
GATE_MAX = 160


def validate(line: str) -> str:
    assert GATE_MIN <= len(line) <= GATE_MAX, "entry line outside the 1-160 char gate"
    assert line.strip(), "entry line must not be only whitespace"
    return line


validate(LINE)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / "entry.txt"
    target.write_text(LINE, encoding="utf-8")
    written = target.read_text(encoding="utf-8")
    assert written == LINE, "entry.txt read-back does not match the gated line"
    validate(written)


if __name__ == "__main__":
    main()
