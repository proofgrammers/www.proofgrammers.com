"""Creating AST from the main.py file."""
import ast

def createAST():
    """Create an AST of the main.py file."""
    with open("main.py", "r", encoding='utf-8') as fn:
        read_fn = fn.read()
        create_ast = ast.parse(read_fn)
        ast_file = ast.dump(create_ast, indent=4)

    return ast_file

if __name__ == "__main__":
    object = createAST()
    print(object)
