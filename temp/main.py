"""In this Python file we create a main function that we can use for our main function detecting tool. """

def main(word: str) -> str:
    """Finding word in a string."""

    text = "gators"

    if word in text:
        return "True"
    else:
        return "False"

if __name__ == "__main__":
    print(main("gators"))


