import ast

def create_ast():
    """Creating an Abstract Syntax Tree."""

    with open("main.py", "r", encoding='utf-8') as fn:
        read_fn = fn.read()
        code = ast.parse(read_fn)

    return code

def walk_tree():
    """Walking through the created AST."""
    code = create_ast()
    functions = []
    for node in ast.walk(code):
        if isinstance(node, ast.FunctionDef):
            functions.append(node.name)
            return functions

def find_main():
    """Find main function in nodes created from the AST."""
    ast_function = walk_tree()
    main_name = "'main'"

    for name in ast_function:
        if name == "main":
            print(f"Main function found: {name}")
        else:
            print("The function you have entered as an input contains no main function.")

if __name__ == "__main__":
    walk_tree()
    find_main()
