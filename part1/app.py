#!/usr/bin/env python3
"""Part 1 starter CLI (Complete the two TODOs in the code below)."""
from constants import BANNER, HELP
from sonnet import SONNET

def manual_count_occurrences(text: str, pattern: str) -> int:
    text = text.lower()
    pattern = pattern.lower()

    if not text or not pattern:
        return 0
    if len(pattern) > len(text):
        return 0
    else:
        count = 0
        for i in range(len(text) - len(pattern) + 1):
            matches = 0
            for j in range(len(pattern)):
                if text[i+j] == pattern[j]:
                    matches += 1
            if matches == len(pattern):
                count += 1
        return count


def print_result(query: str, total: int, title_count: int, line_count: int) -> None:
    print(f"Matches for \"{query}\": {total} (title: {title_count}, lines: {line_count})")

def main() -> None:
    print(BANNER)
    while True:
        try:
            raw = input("> ").strip()
            search_item = raw.lower()
        except (EOFError, KeyboardInterrupt):
            print("\nBye.")
            break
        if not raw:
            continue
        if raw.startswith(":"):
            if raw == ":quit":
                print("Bye.")
                break
            if raw == ":help":
                print(HELP)
                continue
            print("Unknown command. Type :help for commands.")
            continue

        title = SONNET["title"].lower()
        title_count = 0
        title_count += manual_count_occurrences(title, search_item)

        line_count = 0
        for line in SONNET["lines"]:
            line_count += manual_count_occurrences(line.lower(), search_item)

        total = title_count + line_count
        print_result(raw, total, title_count, line_count)

if __name__ == "__main__":
    main()
