"""Detects infinite loops in Python source code."""

import ast

def has_infinite_loop(source_code: str) -> bool:
    """Checks if the source code contains an obvious infinite loop."""
    # Parse the source code into an AST (Abstract Syntax Tree)
    tree = ast.parse(source_code)
    # Walk through all nodes in the AST
    for node in ast.walk(tree):
        # Check for 'while True' loops
        if isinstance(node, ast.While):
            if isinstance(node.test, ast.Constant) and node.test.value is True:
                # Found a 'while True' loop, which is likely infinite
                return True
        # Check for 'for' loops with no break or exit condition (very basic)
        if isinstance(node, ast.For):
            # If the loop body does not contain a 'break', it may be infinite
            if not any(isinstance(child, ast.Break) for child in ast.walk(node)):
                return True
    return False

# Example usage:
# uv run infinite-loop-detector.py
example_code1 = """
while True:
    pass
"""
example_code2 = """
for i in range(10):
    print(i)
    break
"""
result1 = has_infinite_loop(example_code1)
result2 = has_infinite_loop(example_code2)
print("Infinite loop detected!" if result1 else "No infinite loop detected.")
print("Infinite loop detected!" if result2 else "No infinite loop detected.")
