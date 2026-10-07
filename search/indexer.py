import json
import math
from collections import Counter
from pathlib import Path

from search.tokenizer import tokenize


def build_index(docs_path: Path) -> dict:
    """
    Build an inverted index from all text documents.
    """
    index: dict[str, dict[str, int]] = {}
    doc_lengths: dict[str, int] = {}

    documents = list(docs_path.glob("*.txt"))

    for document_path in documents:
        text = document_path.read_text(
            encoding="utf-8"
        )

        words = tokenize(text)

        doc_name = document_path.name

        doc_lengths[doc_name] = len(words)

        word_counts = Counter(words)

        for word, count in word_counts.items():

            if word not in index:
                index[word] = {}

            index[word][doc_name] = count

    total_documents = len(documents)

    idf: dict[str, float] = {}

    for word, postings in index.items():

        documents_containing_word = len(postings)

        idf[word] = math.log(
            (1 + total_documents)
            / (1 + documents_containing_word)
        ) + 1

    return {
        "documents": doc_lengths,
        "index": index,
        "idf": idf,
        "total_documents": total_documents,
    }


def save_index(
    data: dict,
    output_path: Path,
) -> None:
    """
    Save the search index to a JSON file.
    """
    output_path.write_text(
        json.dumps(data, indent=4),
        encoding="utf-8",
    )


def load_index(
    input_path: Path,
) -> dict:
    """
    Load a previously saved search index.
    """
    return json.loads(
        input_path.read_text(
            encoding="utf-8"
        )
    )
    