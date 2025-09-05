"""Creating AST from the main.py file."""
import ast

def create_ast_main():
    """Create an AST of the main.py file."""
    with open("main.py", "r", encoding='utf-8') as fn:
        read_fn = fn.read()
        create_ast = ast.parse(read_fn)
        ast_file = ast.dump(create_ast, indent=4)

    return ast_file


def create_ast_nomain():
    """Create an AST of the no_main.py file."""
    with open("no_main.py", "r", encoding='utf-8') as fn:
        read_file = fn.read()
        fn_ast = ast.parse(read_file)
        store_ast = ast.dump(fn_ast, indent=4)

    return store_ast


def store_ast():
    """Storing the AST file that were created for the main.py file."""
    ast_main = create_ast_main()

    # TODO: Add exception handling if the file does not exist
    with open("ast.txt", "w", encoding='utf-8') as fn:
        return fn.write(ast_main)

def store_no_main_ast():
    """Storing the AST file that were created for the no_main.py file."""
    ast_no_main = create_ast_nomain()

    # TODO: Add exception handling if the file does not exist
    with open("no_main_ast.txt", "w", encoding='utf-8') as fn:
        return fn.write(ast_no_main)


if __name__ == "__main__":
    store_ast()
    store_no_main_ast()
