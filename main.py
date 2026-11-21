#!/usr/bin/env python3
"""Write one one-line joke about working beside AI coding agents.

The joke is written to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only; runs offline, deterministically.
"""

import os

JOKE = (
    "I asked my agent for one small fix; it returned a refactor, "
    "a migration, and a note that my old code was 'holding us back.'"
)
# One line on purpose: the brief asks for a one-line joke, so the text
# carries no newline characters of its own.


def main() -> None:
    text = JOKE
    # The gate requires 1-280 characters, counted as Unicode code points,
    # and not only white space.
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit("entry text fails the 1-280 character gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
