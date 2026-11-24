#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — writes one excuse line to /output/entry.txt."""

import os

LINE = "Sorry, can't come in today — I pulled a muscle reaching for the snooze button and my back has officially filed a complaint with HR."


def build_text() -> str:
    parts = [
        "Sorry, can't come in today",
        "I pulled a muscle reaching for the snooze button and my back has officially filed a complaint with HR.",
    ]
    return " — ".join(parts)


def validate(text: str) -> str:
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    if "\n" in text or not text.strip():
        raise ValueError("entry must be a single non-blank line")
    return text


def main() -> None:
    text = validate(build_text())
    if text != LINE:
        raise ValueError("restructured text must match the original line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
