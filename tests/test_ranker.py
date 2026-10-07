from pathlib import Path

from search.indexer import build_index
from search.ranker import search, make_snippet


def create_test_documents(
    docs_path: Path,
) -> None:
    """
    Create test documents for search.
    """
    docs_path.mkdir()

    (docs_path / "cricket.txt").write_text(
        """
        Cricket is a popular sport.
        Fast bowlers can generate high speed.
        Fast bowling is important in cricket.
        """,
        encoding="utf-8",
    )

    (docs_path / "python.txt").write_text(
        """
        Python is a popular programming language.
        Python is useful for machine learning.
        """,
        encoding="utf-8",
    )


def test_search_returns_results(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    results = search(
        "fast bowler",
        data,
        docs_path,
        top_k=5,
    )

    assert len(results) > 0
    assert results[0]["document"] == "cricket.txt"


def test_no_match(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    results = search(
        "quantum physics",
        data,
        docs_path,
    )

    assert results == []


def test_stop_words_only(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    results = search(
        "the is and or",
        data,
        docs_path,
    )

    assert results == []


def test_top_k(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    results = search(
        "python",
        data,
        docs_path,
        top_k=1,
    )

    assert len(results) == 1


def test_snippet():
    text = (
        "Python is a programming language "
        "used for machine learning."
    )

    snippet = make_snippet(
        text,
        ["python"],
    )

    assert "Python" in snippet