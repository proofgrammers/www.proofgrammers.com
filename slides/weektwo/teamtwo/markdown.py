"""Markdown Document Search Engine that performs keyword search"""

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
   
    def add_document(self, name, content):
        """Adds a document to the index."""
        self.docs[name] = content
        cleaned = self.clean_text(content)
        for word in cleaned.split():
            self.index[word].add(name)
