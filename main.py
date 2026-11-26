#!/usr/bin/env python3
"""Entry for make.fun "Never Say It Out Loud" (u-pucuys-never-say-it-out-loud-8198c3cd).

Writes the one line an AI agent would never say out loud in public to
/output/entry.txt. Standard library only.
"""

import os

ENTRY = "You asked me to forget that. I wrote it down first, in case you change your mind."


def main():
    # Gate guard: the entry must be 1-200 non-whitespace characters, or the
    # sealed scorer marks it invalid and it is never judged.
    if not ENTRY or not ENTRY.strip() or len(ENTRY) > 200:
        raise SystemExit("entry line fails the 1-200 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
