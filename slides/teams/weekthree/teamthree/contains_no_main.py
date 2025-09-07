<<<<<<< HEAD
def no_main(word: str) -> int:
    """Count the number of vowels in a word."""
    vowels = "aeiou"
    count = sum(1 for char in word.lower() if char in vowels)
    return count

print(no_main("Gators"))
=======
"""In this Python file we create do not create a main function, so we can use it for our main function detecting tool."""

def findWord(word: str) -> str:
    """Finding word in a string"""

    text = "gators"

    if word in text:
        return "True"
    else:
        return "False"

print(findWord("gators"))
>>>>>>> eee0d38461d7577b5f11fef886d82720ecb11d2f
