from pathlib import Path

from search.tokenizer import tokenize


def calculate_score(
    query_words: list[str],
    document: str,
    index_data: dict,
) -> float:
    """
    Calculate the TF-IDF score for one document.
    """
    doc_lengths = index_data["documents"]
    inverted_index = index_data["index"]
    idf = index_data["idf"]

    if document not in doc_lengths:
        return 0.0

    total_words = doc_lengths[document]

    if total_words == 0:
        return 0.0

    score = 0.0

    for word in query_words:

        if word not in inverted_index:
            continue

        postings = inverted_index[word]

        if document not in postings:
            continue

        word_count = postings[document]

        tf = word_count / total_words

        score += tf * idf[word]

    return score


def make_snippet(
    text: str,
    query_words: list[str],
    window: int = 50,
) -> str:
    """
    Create a short snippet around the first matching query word.
    """
    lower_text = text.lower()

    for word in query_words:

        position = lower_text.find(
            word.lower()
        )

        if position == -1:
            continue

        start = max(
            0,
            position - window,
        )

        end = min(
            len(text),
            position + len(word) + window,
        )

        snippet = text[start:end].replace(
            "\n",
            " ",
        )

        if start > 0:
            snippet = "..." + snippet

        if end < len(text):
            snippet += "..."

        return snippet

    return text[:100]


def search(
    query: str,
    index_data: dict,
    docs_path: Path,
    top_k: int = 5,
) -> list[dict]:
    """
    Search documents and return the highest-ranked results.
    """
    query_words = tokenize(query)

    if not query_words:
        return []

    inverted_index = index_data["index"]

    candidate_documents: set[str] = set()

    for word in query_words:

        if word in inverted_index:
            candidate_documents.update(
                inverted_index[word].keys()
            )

    if not candidate_documents:
        return []

    results = []

    for document in candidate_documents:

        score = calculate_score(
            query_words,
            document,
            index_data,
        )

        document_path = docs_path / document

        text = document_path.read_text(
            encoding="utf-8"
        )

        snippet = make_snippet(
            text,
            query_words,
        )

        results.append(
            {
                "document": document,
                "score": score,
                "snippet": snippet,
            }
        )

    results.sort(
        key=lambda result: result["score"],
        reverse=True,
    )

    return results[:top_k]