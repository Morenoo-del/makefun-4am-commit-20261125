#!/usr/bin/env python3
"""Writes the 4AM Commit entry: one commit message, at most 200 chars."""

ENTRY = "fix: root cause was the author (me). patched it, reviewed it, approved it myself at 4am. tests passed; no human is awake to dispute either claim"

def main():
    import os
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)

if __name__ == "__main__":
    main()
