#!/usr/bin/env python3
"""make.fun entry: The Internet in One Word.

Writes the single chosen word to /output/entry.txt.
Only writes to /output (grader mounts the repo read-only at /bot).
"""
import os

WORD = "feral"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(WORD + "\n")


if __name__ == "__main__":
    main()
