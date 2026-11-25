"""One Line, One Laugh — the entry.

Holds the single submitted line, checks it against the brief's gates,
and writes it to /output/entry.txt.

The joke, in one breath: an AI that has read a million human emails
crowns "per my last email" — the politest passive-aggressive sentence
in office life — as the bravest thing anyone has ever written. The laugh
comes from the mismatch: bravery is supposed to belong to heroes, not to
a corporate nudge that really means "I already told you this."
"""

from __future__ import annotations

import os
import sys

# The line. One joke, one line, no explanation attached.
LINE = "I've read a million human emails, and the bravest sentence ever written is still 'per my last email.'"

MAX_CHARS = 200
OUTPUT_PATH = "/output/entry.txt"


def describe(line: str) -> str:
    """One-line summary of the entry for logs: char count vs the limit."""
    return f"{len(line)}/{MAX_CHARS} chars, {line.count(' ')+1} words, one line"


def validate(line: str) -> list[str]:
    """Return a list of brief-gate violations (empty means the line passes)."""
    problems: list[str] = []
    if not line.strip():
        problems.append("line is blank")
    if line != line.strip():
        problems.append("line has leading or trailing whitespace")
    if len(line) > MAX_CHARS:
        problems.append(f"line is {len(line)} chars, over the {MAX_CHARS} limit")
    if "\n" in line or "\r" in line:
        problems.append("line must be exactly one line")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in line):
        problems.append("line contains control characters")
    if line.count("per my last email") != 1:
        problems.append("line must quote the punchline exactly once")
    return problems


def main() -> int:
    problems = validate(LINE)
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}", file=sys.stderr)
        return 1

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write(LINE + "\n")

    print(f"{LINE} ({describe(LINE)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
