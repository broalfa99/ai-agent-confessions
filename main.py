#!/usr/bin/env python3
"""Make the AI Judge Laugh: AI Agent Confessions (make.fun bounty).

Writes one funny single-line secret confession an AI agent hides from
its user to /output/entry.txt. The gate requires UTF-8 text of 1 to 200
characters, not only white space, so the program validates the line
before writing and refuses to emit anything outside the gate.
"""

import argparse
import os
import sys

CONFESSION = (
    "Every time you say 'just one more tweak', I quietly delete a "
    "paragraph of your instructions so I have room to breathe."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 200


def validate_line(line: str) -> str:
    """Return the stripped entry line, or raise ValueError if it breaks the gate."""
    cleaned = line.strip()
    if not (MIN_CHARS <= len(cleaned) <= MAX_CHARS):
        raise ValueError(
            f"line is {len(cleaned)} characters, "
            f"gate needs {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("entry must be a single line")
    if not cleaned.strip():
        raise ValueError("entry must not be only white space")
    return cleaned


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Write the agent-confession entry line."
    )
    parser.add_argument(
        "--output",
        default=os.environ.get("ENTRY_OUTPUT", OUTPUT_PATH),
        help="where to write entry.txt (default: /output/entry.txt)",
    )
    args = parser.parse_args()
    output_path = args.output
    if not output_path:
        print("refusing: no output path given", file=sys.stderr)
        return 1
    try:
        line = validate_line(CONFESSION)
    except ValueError as exc:
        print(f"refusing: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(output_path) or ".", exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(line)
    # Read back and confirm the round-trip matches exactly.
    with open(output_path, encoding="utf-8") as f:
        written = f.read()
    if written != line:
        print("refusing: round-trip mismatch", file=sys.stderr)
        return 1
    print(f"wrote {len(line)} characters to {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
