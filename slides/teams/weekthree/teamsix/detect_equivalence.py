import ast
from typing import Tuple


def standardize_naming(source: ast) -> ast.AST:
    """
    Standardizes all variable, function, and class names in the AST to numbered placeholders.
    This helps ignore differences in naming conventions when comparing program structure.
    """
    used_name = {}  # Maps original names to standardized numbered names
    name_id = 1  # Counter for generating new names
    # Walk through all nodes in the AST
    for node in ast.walk(source):
        # Standardize variable names
        if isinstance(node, ast.Name):
            if node.id in used_name:
                node.id = used_name[node.id]
            else:
                name_id += 1
                used_name[node.id] = str(name_id)
                node.id = str(name_id)
        # Standardize function and class names
        if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
            if node.name in used_name:
                node.name = used_name[node.name]
            else:
                name_id += 1
                used_name[node.name] = str(name_id)
                node.name = str(name_id)
        # Standardize function argument names
        if isinstance(node, ast.arg):
            if node.arg in used_name:
                node.arg = used_name[node.arg]
            else:
                name_id += 1
                used_name[node.arg] = str(name_id)
                node.arg = str(name_id)
    print(ast.unparse(source))
    return source


def get_syntax_tree(
    program_one, program_two
) -> Tuple[ast.AST | Exception, ast.AST | Exception]:
    """
    Parses two Python programs and returns their ASTs.
    If parsing fails, returns the exception instead.
    """
    try:
        parser_one = ast.parse(program_one)
    except Exception as e:
        parser_one = e

    try:
        parser_two = ast.parse(program_two)
    except Exception as e:
        parser_two = e

    return parser_one, parser_two


def same_string(str_one: str, str_two: str) -> bool:
    """
    Checks if two strings are equal, ignoring leading/trailing newlines.
    """
    if str_one.strip("\n") == str_two.strip("\n"):
        return True
    return False


def same_error(error_one: Exception, error_two: Exception) -> bool:
    """
    Checks if two exceptions have the same string representation.
    """
    if str(error_one) == str(error_two):
        return True


def detect_equivalence(program_one: str, program_two) -> str:
    """
    Determines if two Python programs are equivalent by structure and naming.
    Returns "Yes" if equivalent, otherwise "No".
    """
    parsed_str_one, parsed_str_two = get_syntax_tree(program_one, program_two)
    # If the source code is identical, they are equivalent
    if same_string(program_one, program_two):
        return "Yes"
    # If both programs fail to parse with the same error, consider them equivalent
    if isinstance(parsed_str_one, Exception) and isinstance(parsed_str_two, Exception):
        if same_error(parsed_str_one, parsed_str_two):
            return "Yes"
    # If only one fails to parse, they are not equivalent
    elif isinstance(parsed_str_one, Exception) or isinstance(parsed_str_two, Exception):
        return "No"
    else:
        # Standardize naming and compare AST dumps
        standardized_str_one = standardize_naming(parsed_str_one)
        standardized_str_two = standardize_naming(parsed_str_two)
        if same_string(
            ast.dump(standardized_str_one, indent=True),
            ast.dump(standardized_str_two, indent=True),
        ):
            return "Yes"
    return "No"


if __name__ == "__main__":
    # Example programs to test equivalence
    program_one = """def calculate_sum(numbers):
    toal = 0
    for n in numbers:
        toal += n
    if toal > 10:
        print("Large sum")
    else:
        print("Small sum")
    return toal

calculate_sum([1, 2, 3, 7])
"""

    program_two = """def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    if total > 10:
        print("Large sum")
    else:
        print("Small sum")
    return total

calculate_sum([1, 2, 3, 7])
"""

    # Print whether the two programs are equivalent
    result = detect_equivalence(program_one, program_two)
    print(result)
