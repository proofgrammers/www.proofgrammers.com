import ast

class ASTAnalyzer:
    def create_ast(self):
        """Create an AST from an in-memory Python snippet."""
        code_with_main = """\
def main(word: str) -> str:
    text = "gators"
    if word in text:
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    print(main("gators"))
"""
        return ast.parse(code_with_main)

    def walk_tree(self):
        """Return a list of function names in the AST."""
        tree = self.create_ast()
        functions = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                functions.append(node.name)
        return functions

    def find_main(self):
        """Print whether a 'main' function exists."""
        fn_names = self.walk_tree()
        if "main" in fn_names:
            print("Main function found: main")
        else:
            print("The function you have entered as an input contains no main function.")

if __name__ == "__main__":
    analyzer = ASTAnalyzer()
    analyzer.find_main()

