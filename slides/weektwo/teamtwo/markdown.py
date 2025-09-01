"""
Markdown Document Search Engine that performs keyword search.
"""

from collections import defaultdict
import re


class Index:
    """A simple inverted index for text documents."""

    def __init__(self):
        self.index = defaultdict(set)
        self.docs = {}

    def clean_text(self, text: str) -> str:
        """Cleans the input text by removing unwanted characters."""
        text = re.sub(r"[#*`\[\]()>_~]", " ", text)
        return text.lower()

    def add_document(self, name: str, content: str):
        """Adds a document to the index."""
        self.docs[name] = content
        cleaned = self.clean_text(content)
        for word in cleaned.split():
            self.index[word].add(name)

    def search(self, query: str):
        """Searches for documents containing the query word."""
        query = query.lower()
        return self.index.get(query, set())


if __name__ == "__main__":
    # Example usage
    engine = Index()
    engine.add_document("doc1.md", "# Intro\nThis is about computation theory.")
    engine.add_document("doc2.md", "# Search\nEngines perform keyword search.")
    engine.add_document("doc3.md", "# Notes\nTractable problems are solvable.")

    query = "computation"
    print("Searching for:", query)
    print("Found in:", engine.search(query))

    query = "search"
    print("\nSearching for:", query)
    print("Found in:", engine.search(query)) #done.
    