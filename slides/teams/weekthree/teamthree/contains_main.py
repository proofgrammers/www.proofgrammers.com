"""In this Python file we create a main function that we can use for our main function detecting tool. """

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
