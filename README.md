# Mini Search Engine

A lightweight search engine built from scratch in Python using an inverted index and TF-IDF ranking.

This project was created as a capstone project to understand how basic information retrieval and search systems work internally without relying on external search libraries.

## Features

- Document indexing
- Inverted index
- Text tokenization
- Lowercase normalization
- Punctuation removal
- Stop-word removal
- TF-IDF ranking
- Document scoring
- Search result snippets
- Top-K search results
- JSON index storage
- JSON index loading
- Command-line interface using `argparse`
- Type hints
- Unit testing with `pytest`

## Project Structure

```text
mini-search-engine/
│
├── docs/
│   ├── cricket.txt
│   ├── python.txt
│   ├── machine_learning.txt
│   └── ...
│
├── search/
│   ├── __init__.py
│   ├── tokenizer.py
│   ├── indexer.py
│   └── ranker.py
│
├── tests/
│   ├── test_tokenizer.py
│   ├── test_indexer.py
│   └── test_ranker.py
│
├── .gitignore
├── docs.py
├── index.json
├── requirements.txt
├── README.md
└── search.py
```
