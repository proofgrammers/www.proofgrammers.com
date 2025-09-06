import ast

class VisitNode:
    def __init__(self, source_path):
        self.code = None
        self.tree = None
        self.source_path = source_path

    def load_source(self, path=None):
        """Load Python source code from a file into self.code."""
        file_path = path or self.source_path
        if not file_path:
            raise ValueError("No source path provided. Pass a path or set self.source_path.")

        try:
            with open(file_path, "r", encoding="utf-8") as fn:
                self.code = fn.read()
            return self.code
        except FileNotFoundError:
            raise FileNotFoundError(f"Source file not found: {file_path}")


    def create_ast(self):
        """Creating AST."""
        self.tree = ast.parse(self.code)
        return self.tree

        
