import ast
import main
from temp.create_ast import create_ast_main

class VisitNode:
    def __init__(self, code, tree):
        self.code = code
        self.tree = tree

    def createAST(self):
        """Creating an AST."""
        with open("main.py", "r", encoding='utf-8') as fn:
            self.code = fn.read()
            self.tree = ast.parse(self.code)
        return self.tree

    def walkNode(self):
        """Walking through the nodes of the created AST."""
        ast_tree = self.tree

        for node in ast.walk(ast_tree):
            if isinstance(node, ast.FunctionDef):
                print(f"Detected function definition: {node.name}")
                


if __name__ == "__main__":
    object = VisitNode
    object.walkNode
