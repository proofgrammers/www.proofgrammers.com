import ast

class VisitNode:
    def __init__(self, source_path):
        self.code = None
        self.tree = None
        self.source_path = source_path

    def load_source(self, path=None):
        """Loading Python source codes."""
        if path:
            print(f"Path could not be found: {path}")
        
        if self.source_path:
            with open("main.py", "r", encoding='utf-8') as fn:
                read_file = fn.read()
                self.code = read_file

            return self.code

