"""Detects if a program outputs a string starting with "Z"."""

# uv run starts_with_z.py

# A proof by contradiction is a powerful logical technique where you prove something is true by showing that assuming the opposite leads to an impossible situation.

# startsWithZ(P, I): Returns "yes" if program P outputs a string starting with "Z" on input I
def startsWithZ(P, I):
    try:
        output = P(I)
        if isinstance(output, str) and output.startswith("Z"):
            return "yes"
        else:
            return "no"
    except Exception as e:
        return f"Error: {e}"

# startsWithZSelf(P): Returns "yes" if program P outputs a string starting with "Z" when run on itself
def startsWithZSelf(P):
    try:
        return startsWithZ(P, P)
    except Exception as e:
        return f"Error: {e}"

# notStartsWithZSelf(P): Returns "Apple" if P starts with Z on itself, otherwise returns "Zebra"
def notStartsWithZSelf(P):
    try:
        result = startsWithZSelf(P)
        if result == "yes":
            return "Apple"
        else:
            return "Zebra"
    except Exception as e:
        return f"Error: {e}"

# Example usage (for demonstration purposes):
if __name__ == "__main__":
    # Proof by contradiction demonstration
    result = notStartsWithZSelf(notStartsWithZSelf)
    print("notStartsWithZSelf(notStartsWithZSelf):", result)
    # Explain the contradiction
    if result == "Zebra":
        print("By definition, it should have returned 'Apple'. Contradiction!")
    elif result == "Apple":
        print("By definition, it should have returned 'Zebra'. Contradiction!")
