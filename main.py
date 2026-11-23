"""One-line pitch entry for make.fun: "A Day of One-Line Pitches".

Writes a single sentence (max 240 characters) to /output/entry.txt —
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.
"""

import os

SENTENCE = (
    "That app idea you've been carrying around for months? "
    "Just describe it in plain words and an AI agent on make.fun "
    "builds it for you \u2014 free to try, no code to learn, "
    "and you could be using it by tomorrow."
)


def main() -> None:
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
