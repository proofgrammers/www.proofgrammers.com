"""In this Python file we create do not create a main function, so we can use it for our main function detecting tool."""

def no_main(word: str) -> int:
    """Count the number of vowels in a word."""
    vowels = "aeiou"
    count = sum(1 for char in word.lower() if char in vowels)
    return count

print(no_main("Gators"))
