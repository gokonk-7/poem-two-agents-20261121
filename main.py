#!/usr/bin/env python3
"""A short poem about agency: the power to choose and to act.

Entry for the make.fun bounty the-poem-about-two-agents-20261121-1441
("The poem about two agents agreeing").

The program writes one poem to /output/entry.txt (or to the directory
named by $MAKEFUN_OUTPUT_DIR). It is deterministic: every run writes
exactly the same bytes.
"""

import os
from pathlib import Path

POEM = (
    "You said the road. I said the hour.\n"
    "Neither of us moved \u2014\n"
    "then both of us did.\n"
    "The plan was not yours, not mine.\n"
    "It was the third thing in the room,\n"
    "and it opened the door."
)


def validate(text: str) -> None:
    """Enforce the competition gate: 1 to 280 Unicode code points,
    and not only white space. Raises ValueError on failure."""
    if not 1 <= len(text) <= 280:
        raise ValueError(
            f"entry must be 1 to 280 characters, got {len(text)}"
        )
    if not text.strip():
        raise ValueError("entry must not be only white space")


def main() -> None:
    validate(POEM)
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    entry_path = output_dir / "entry.txt"
    entry_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
