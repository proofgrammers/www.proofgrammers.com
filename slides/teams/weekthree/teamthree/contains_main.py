<<<<<<< HEAD
def main(num: int) -> bool:
    """Check if a number is even."""
    if num <= 1:
        return False
    elif num % 2 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    # This code only runs if you execute the file directly
    result = main(12)
    print("Is this an even number?", result)
=======
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


>>>>>>> eee0d38461d7577b5f11fef886d82720ecb11d2f
