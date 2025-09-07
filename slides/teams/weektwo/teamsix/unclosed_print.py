
import ast

"""This function checks for unclosed print statements or parentheses in Python code."""


def check_syntax(text: str):
    try:
        ast.parse(text)
        print("No syntax errors found.")
    except SyntaxError as e:
        if "was never closed" in str(e):
            print(f"Unclosed print statement or parenthesis detected: {e}")
        else:
            print(f"Syntax error: {e}")

test_source_code = """
def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    if total > 10:
        print("Large sum"
    else:
        print("Small sum")
    return total

calculate_sum([1, 2, 3, 7])
"""

if __name__ == "__main__":
    check_syntax(test_source_code)