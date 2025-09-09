import ast

def has_syntax_error(code: str) -> str:
    try:
        ast.parse(code)
        return "no"
    except SyntaxError:
        return "yes"