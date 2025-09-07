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
        """Find main function in nodes created from the AST."""
        ast_function = self.walk_tree()
        if not ast_function:
            return

        for name in ast_function:
            if name == "main":
                print(f"Main function found: {name}")
            else:
                print("The function you have entered as an input contains no main function.")


if __name__ == "__main__":
    analyzer = ASTAnalyzer()
    analyzer.walk_tree()
    analyzer.find_main()

