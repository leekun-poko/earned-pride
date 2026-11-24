#!/usr/bin/env python3
"""Write the entry line for the "One Line of Earned Pride" bounty.

The program writes a single line of text to entry.txt inside the
output directory named by MAKEFUN_OUTPUT_DIR (default /output).
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "Eleven failed driving tests behind her, she drove her father to "
    "dialysis this morning \u2014 and he slept the whole way there, "
    "trusting her hands."
)


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ENTRY_TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()

