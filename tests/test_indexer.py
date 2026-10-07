from pathlib import Path

from search.indexer import (
    build_index,
    save_index,
    load_index,
)


def create_test_documents(
    docs_path: Path,
) -> None:
    """
    Create small test documents.
    """
    docs_path.mkdir()

    (docs_path / "one.txt").write_text(
        "Python is powerful and Python is popular.",
        encoding="utf-8",
    )

    (docs_path / "two.txt").write_text(
        "Python is useful for data science.",
        encoding="utf-8",
    )


def test_build_index(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    assert data["total_documents"] == 2
    assert "python" in data["index"]
    assert data["index"]["python"]["one.txt"] == 2


def test_document_lengths(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    assert data["documents"]["one.txt"] > 0
    assert data["documents"]["two.txt"] > 0


def test_save_and_load(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    index_path = tmp_path / "index.json"

    save_index(data, index_path)

    loaded_data = load_index(index_path)

    assert loaded_data == data


def test_idf_exists(tmp_path):
    docs_path = tmp_path / "docs"

    create_test_documents(docs_path)

    data = build_index(docs_path)

    assert "python" in data["idf"]
    assert data["idf"]["python"] > 0