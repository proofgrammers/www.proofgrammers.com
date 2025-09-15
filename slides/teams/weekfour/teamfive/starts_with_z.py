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
    # Define a sample program P for testing
    def sample_program(input):
        if input == sample_program:
            return "Zebra"
        return "Apple"
    
    # Proof by contradiction demonstration
    # x

'''
Proof by Contradiction Demo: startsWithZ Uncomputability

Claim: startsWithZ is uncomputable (impossible to implement perfectly)
Assumption: Suppose startsWithZ is computable (we can implement it perfectly)
Trap: If we could implement startsWithZ, then we could also implement:
    - startsWithZSelf(P): checks if program P outputs a Z-string when given itself as input
    - notStartsWithZSelf(P):
        Returns "Apple" (not Z) if P would output a Z-string on itself
        Returns "Zebra" (starts with Z) if P would NOT output a Z-string on itself
Contradiction: What happens when we run notStartsWithZSelf on itself?
    - If notStartsWithZSelf(notStartsWithZSelf) returns "Zebra", then by definition, it should return "Apple"
    - If notStartsWithZSelf(notStartsWithZSelf) returns "Apple", then by definition, it should return "Zebra"
This is impossible! The function contradicts itself no matter what it tries to return. (troublemaker program)
Conclusion: startsWithZ is uncomputable.
''' 
