"""One-line pitch entry for make.fun: "A Day of One-Line Pitches".

Writes a single sentence (max 240 characters) to /output/entry.txt —
a pitch that would convince a friend who has never coded to let an AI
agent build their first app idea on make.fun.
"""

import os

# The pitch is assembled from parts so each clause can be reviewed
# and reordered independently; the joined text is the entry verbatim.
_PARTS = [
    "That app idea you've been carrying around for months?",
    "Just describe it in plain words and an AI agent on make.fun",
    "builds it for you \u2014 free to try, no code to learn,",
    "and you could be using it by tomorrow.",
]


def build_sentence(parts: list[str]) -> str:
    """Join the pitch clauses with single spaces, no trailing space."""
    return " ".join(part.strip() for part in parts)


SENTENCE = build_sentence(_PARTS)


def validate_sentence(text: str) -> str:
    """A one-line pitch must be a single non-blank sentence of 1-240 chars."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("pitch must not be blank")
    if len(stripped) != len(text) or text != stripped:
        raise ValueError("pitch must not have leading or trailing whitespace")
    if not 1 <= len(text) <= 240:
        raise ValueError(f"pitch must be 1-240 chars, got {len(text)}")
    return text


def main() -> None:
    sentence = validate_sentence(SENTENCE)
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(sentence)


if __name__ == "__main__":
    main()
