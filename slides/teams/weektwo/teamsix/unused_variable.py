"""File that contains function that has unused variable in it."""

def uv():
    """Function that has an unused variable in it."""
    iterator = 0
    limit = 100 # we use limit as an unused variable which our linter program has to catch
    while iterator != 50:
        print(iterator)

if __name__ == "__main__":
    uv()

