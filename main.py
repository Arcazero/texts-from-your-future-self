"""Texts From Your Future Self -- make.fun entry.

Writes one funny text message from the writer's future self to
/output/entry.txt. The gate: UTF-8 text, 1 to 200 characters, not only
whitespace.
"""

import os

ENTRY = (
    "It's you from 2041. The plant died, the goldfish died, but your "
    "2024 sourdough starter is a legal dependent now. It gets the good "
    "flour. Feed it before it sues for custody."
)

MAX_CHARS = 200


def validate(line: str) -> None:
    if not line or not line.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single text message, no line breaks")
    if len(line) > MAX_CHARS:
        raise ValueError(f"entry is {len(line)} chars, over the {MAX_CHARS} limit")


def write_entry(path: str) -> None:
    """Write the entry text exactly, no trailing newline, UTF-8."""
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


def main() -> None:
    validate(ENTRY)
    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
        write_entry(path)
    except OSError:
        # Local runs where /output is not writable: mirror next to the repo.
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "output", "entry.txt")
        os.makedirs(os.path.dirname(path), exist_ok=True)
        write_entry(path)
    print(f"Wrote {len(ENTRY)}-char entry to {path}")
    print(ENTRY)


if __name__ == "__main__":
    main()
