import ast

class VisitNode:
    def __init__(self, code, tree):
        self.code = code
        self.tree = tree

    def create_ast(self):
        """Creating an AST."""
        with open("main.py", "r", encoding='utf-8') as fn:
            self.code = fn.read()
            self.tree = ast.parse(self.code)
        return self.tree

    def walk_node(self, tree):
        """Walking through the nodes of the created AST."""
        ast_tree = self.tree
        ast_nodes = ast.walk(ast_tree)
    
        for node in ast_nodes:
            if isinstance(node, ast.FunctionDef):
                print(f"Detected function definition: {node.name}")
                


if __name__ == "__main__":
    with open("main.py", "r", encoding='utf-8') as fn:
        code = fn.read()
        tree = ast.parse(code)

    VisitNode.walk_node(self, tree)
