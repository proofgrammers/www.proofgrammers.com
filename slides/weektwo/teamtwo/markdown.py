"""
Markdown Document Search Engine that performs keyword search.
"""
from collections import defaultdict
import re
import os
import sys


class Index:
    """A simple inverted index for text documents."""

    def __init__(self):
        self.index = defaultdict(set)
        self.docs = {}

    # helper: return list of words from text (normalized)
    def tokenize(self, text: str):
        """Return lowercase word tokens from text."""
        if not text:
            return []
        return re.findall(r"\b\w+\b", text.lower())

    def add_document(self, name: str, content: str):
        """Adds a document to the index."""
        self.docs[name] = content
        for word in self.tokenize(content):
            self.index[word].add(name)

    def search(self, query: str):
        """Search for documents that contain all words in the query (AND)."""
        words = self.tokenize(query)
        if not words:
            return set()
        sets = [self.index.get(w, set()) for w in words]
        if not sets or any(len(s) == 0 for s in sets):
            return set()
        return set.intersection(*sets)

    def get_snippet(self, name: str, query: str, context: int = 40) -> str:
        """Return a short snippet around the first whole-word match for any query word/phrase."""
        content = self.docs.get(name, "")
        if not content:
            return ""
        q = query.strip()
        if not q:
            return ""
        # try phrase match first (word boundaries), then any token
        phrase_pat = re.compile(r"\b" + re.escape(q) + r"\b", flags=re.IGNORECASE)
        m = phrase_pat.search(content)
        if not m:
            parts = self.tokenize(q)
            if parts:
                pat = re.compile(r"\b(" + "|".join(re.escape(p) for p in parts) + r")\b", flags=re.IGNORECASE)
                m = pat.search(content)
        if not m:
            # fallback: start of document
            s = content.strip().replace("\n", " ")
            return (s[:context] + ("..." if len(s) > context else ""))
        start = max(0, m.start() - context)
        end = min(len(content), m.end() + context)
        snippet = content[start:end].replace("\n", " ")
        return ("..." if start > 0 else "") + snippet + ("..." if end < len(content) else "")

    def add_documents_from_folder(self, folder: str):
        """Index all .md files under folder (recursive)."""
        if not os.path.isdir(folder):
            return 0
        count = 0
        for root, _, files in os.walk(folder):
            for fname in files:
                if not fname.lower().endswith(".md"):
                    continue
                fpath = os.path.join(root, fname)
                try:
                    with open(fpath, "r", encoding="utf-8") as fh:
                        content = fh.read()
                except Exception:
                    continue
                name = os.path.relpath(fpath, start=folder)
                self.add_document(name, content)
                count += 1
        return count


if __name__ == "__main__":
    engine = Index()
    args = sys.argv[1:]
    folder = None
    queries = []

    if args and os.path.isdir(args[0]):
        folder = args[0]
        queries = args[1:]
    else:
        if args:
            queries = args
        this_dir = os.path.dirname(os.path.abspath(__file__))
        test_dir = os.path.join(this_dir, "test")
        if os.path.isdir(test_dir):
            folder = test_dir

    if folder:
        n = engine.add_documents_from_folder(folder)
        print(f"Indexed {n} .md files from: {folder}")
        if n:
            print("Files indexed:")
            for name in sorted(engine.docs.keys()):
                print(" -", name)
        else:
            print("No .md files found.")
    else:
        # minimal fallback examples when no folder is available
        engine.add_document("doc1.md", "# Intro\nThis is about computation theory.")
        engine.add_document("doc2.md", "# Search\nEngines perform keyword search.")
        engine.add_document("doc3.md", "# Notes\nTractable problems are solvable.")

    def run_query(q):
        res = engine.search(q)
        print(f"\nQuery: {q!r} -> {len(res)} result(s)")
        for name in sorted(res):
            print(" -", name)
            sn = engine.get_snippet(name, q)
            if sn:
                print("    ", sn)

    if queries:
        for q in queries:
            run_query(q)
    else:
        try:
            while True:
                q = input("\nEnter query (blank to exit): ").strip()
                if not q:
                    break
                run_query(q)
        except (EOFError, KeyboardInterrupt):
            print("\nexiting")
    def run_query(q):
        results = engine.search(q)
        print(f"\nQuery: {q!r} -> {len(results)} result(s)")
        if results:
            for name in sorted(results):
                print(" -", name)
                sn = engine.get_snippet(name, q)
                if sn:
                    print("    ", sn)

    if queries:
        for q in queries:
            run_query(q)
    else:
        try:
            while True:
                q = input("\nEnter query (blank to exit): ").strip()
                if not q:
                    break
                run_query(q)
        except (EOFError, KeyboardInterrupt):
            print("\nexiting")

# No changes required to run. Use the commands in the instructions to execute and test.
