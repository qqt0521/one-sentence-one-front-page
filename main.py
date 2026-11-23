#!/usr/bin/env python3
"""One Sentence, One Front Page.

Writes a single front-page sentence to /output/entry.txt and prints it.
Entry for the make.fun bounty
u-brisk-kestrel-93-one-sentence-one-front-page-0db596eb.
"""

import os

ENTRY = (
    "Iran strikes US bases in Bahrain and three tankers in the Strait of "
    "Hormuz as Trump rejects Tehran's offer of a deal."
)


def main() -> None:
    # Gate: /output/entry.txt must be 1-200 chars of UTF-8 text.
    if not 1 <= len(ENTRY) <= 200:
        raise SystemExit(f"entry is {len(ENTRY)} chars, outside the 1-200 gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
