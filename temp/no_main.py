"""In this Python file we create do not create a main function, so we can use it for our main function detecting tool."""

def findWord(word: str) -> str:
    """Finding word in a string"""

    text = "gators"

    if word in text:
        return "True"
    else:
        return "False"

print(findWord("gators"))
