"""One Star for Monday.

Writes one one-star review of Monday, written as if Monday were a
restaurant, to $MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only.
"""

import os

REVIEW = (
    "One star. Waited an hour for a table, the waiter served me a "
    "full week, and the bill took my entire weekend."
)


def check_review(text):
    """Check the review against the competition gate before writing.

    The gate needs UTF-8 text of 1 to 180 characters, not only white
    space, on a single line: a one-star review of Monday written as
    if Monday were a restaurant, at most 25 words, no explanation.
    Returns the cleaned text or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("review must not be only whitespace")
    if len(cleaned) > 180:
        raise ValueError(
            "review is %d characters, over the 180 limit" % len(cleaned)
        )
    if len(cleaned.split()) > 25:
        raise ValueError(
            "review is %d words, over the 25 word limit"
            % len(cleaned.split())
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("review must be exactly one line")
    return cleaned


def review_shape(text):
    """Measure the review for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A review too short to carry a complaint, or
    one padded past the word limit, is caught here before anything
    is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = check_review(REVIEW)
    shape = review_shape(text)
    if shape["words"] < 5:
        raise ValueError("review is too short to carry a complaint")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
