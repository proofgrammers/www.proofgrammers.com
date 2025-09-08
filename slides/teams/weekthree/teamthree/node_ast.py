import ast

class ASTAnalyzer:
    def create_ast(self):
        """Creating an Abstract Syntax Tree."""
        try:
            with open("cannot_detect_main.py", "r", encoding='utf-8') as fn:
                read_fn = fn.read()
                code = ast.parse(read_fn)
            return code
        except FileNotFoundError:
            print("Error: 'main.py' not found.")
            return None

    def walk_tree(self):
        """Walking through the created AST."""
        code = self.create_ast()
        if code is None:
            return None
        functions = []
        for node in ast.walk(code):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
        return functions

    def find_main(self):
        """Report whether a 'main' function exists."""
        names = self.walk_tree()
        if names is None:
            return

        if "main" in names:
            print("Main function found: main")
        else:
            print("No main function found.")


if __name__ == "__main__":
    analyzer = ASTAnalyzer()
    analyzer.walk_tree()
    analyzer.find_main()

