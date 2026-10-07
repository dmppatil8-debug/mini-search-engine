import string


STOP_WORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "and",
    "or",
    "of",
    "to",
    "in",
    "on",
    "for",
    "with",
    "at",
    "by",
    "from",
    "as",
    "it",
    "this",
    "that",
    "these",
    "those",
    "be",
    "been",
    "being",
    "can",
    "could",
    "should",
    "would",
    "will",
    "about",
    "into",
    "than",
    "then",
    "their",
    "there",
    "they",
    "he",
    "she",
    "we",
    "you",
    "i",
    "my",
    "your",
}


def tokenize(text: str) -> list[str]:
    """
    Convert text into lowercase words,
    remove punctuation and stop words.
    """
    text = text.lower()

    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    words = text.split()

    words = [
        word
        for word in words
        if word not in STOP_WORDS
    ]

    return words