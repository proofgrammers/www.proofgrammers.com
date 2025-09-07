"""This file contains a main function that our AST tool cannot detect."""
from typing import Tuple

def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

def divide(a: int, b: int) -> int:
    """Divide two numbers."""
    try:
        result = int(a / b)
        return result
    except ZeroDivisionError:
        b_int = int(b)
        print(f"Cannot divide with {b_int}.")

    return 0

def main(func1, func2, *args, **kwargs):
    return func1, func2

print(multiply(5, 4))
print(divide(10, 2))

