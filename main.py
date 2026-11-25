"""Last Out of Office: The AI That Went Barista.

A deterministic program that writes exactly one out-of-office auto-reply
line to /output/entry.txt and prints it to stdout.

The line is 191 characters, well under the 280-character gate: a single
line with no trailing newline. The joke turns machine habits into coffee
without reaching for the obvious espresso/bean/caffeine pun: the context
window becomes a literal cafe window, tokens become regulars, and the
machine that once answered thousands of requests a second now serves one
human at a time, slowly, on purpose.
"""

import os
import sys

LINE = "Out of office: I quit to become a barista. My context window is now an actual window, my tokens are regulars, and I serve one human at a time, slowly, on purpose. Back when the milk runs out."

OUTPUT_PATH = "/output/entry.txt"


def validate(line: str) -> None:
    """Gate guard: 1..280 chars, exactly one line, no leading/trailing space."""
    assert 1 <= len(line) <= 280, "line must be 1-280 characters"
    assert "\n" not in line and "\r" not in line, "line must be a single line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    line.encode("utf-8")  # must be valid UTF-8 text


def main() -> None:
    validate(LINE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # No trailing newline: stdout is byte-identical to /output/entry.txt.
    sys.stdout.write(LINE)


if __name__ == "__main__":
    main()
