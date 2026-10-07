import argparse
from pathlib import Path

from search.indexer import (
    build_index,
    save_index,
    load_index,
)

from search.ranker import search


INDEX_FILE = Path("index.json")


def create_parser() -> argparse.ArgumentParser:
    """
    Create the command-line argument parser.
    """
    parser = argparse.ArgumentParser(
        description="Mini TF-IDF Search Engine"
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    index_parser = subparsers.add_parser(
        "index",
        help="Build search index",
    )

    index_parser.add_argument(
        "docs",
        type=Path,
        help="Path to documents",
    )

    query_parser = subparsers.add_parser(
        "query",
        help="Search documents",
    )

    query_parser.add_argument(
        "query",
        type=str,
        help="Search query",
    )

    query_parser.add_argument(
        "--top",
        type=int,
        default=5,
        help="Number of results",
    )

    return parser


def main() -> None:
    """
    Run the command-line search engine.
    """
    parser = create_parser()

    args = parser.parse_args()

    if args.command == "index":

        docs_path = args.docs

        if not docs_path.exists():
            print(
                f"Error: {docs_path} does not exist."
            )
            return

        data = build_index(docs_path)

        save_index(
            data,
            INDEX_FILE,
        )

        print(
            "Index created successfully."
        )

        print(
            f"Documents indexed: "
            f"{data['total_documents']}"
        )

        print(
            f"Unique words: "
            f"{len(data['index'])}"
        )

    elif args.command == "query":

        if not INDEX_FILE.exists():
            print(
                "Error: index.json not found."
            )

            print(
                "Run the index command first."
            )

            return

        index_data = load_index(
            INDEX_FILE
        )

        docs_path = Path("docs")

        results = search(
            args.query,
            index_data,
            docs_path,
            args.top,
        )

        if not results:
            print("No results found.")
            return

        print(
            f'\nSearch results for: "{args.query}"\n'
        )

        for number, result in enumerate(
            results,
            start=1,
        ):
            print(
                f"{number}. "
                f"{result['document']}"
            )

            print(
                f"   Score: "
                f"{result['score']:.6f}"
            )

            print(
                f"   {result['snippet']}"
            )

            print()


if __name__ == "__main__":
    main()