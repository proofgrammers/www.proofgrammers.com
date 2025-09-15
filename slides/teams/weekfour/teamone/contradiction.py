"""Create a proof by contradiction for the yesOnString problem."""

def troublemaker(some_string: str):
    return "yes"

def yesOnString(program_input: str, input_string: str):
    """Return yes on a valid P, if input is defined and P(I) is yes."""
    if program_input == 'troublemaker.py' and isinstance(input_string, str):
        return troublemaker(input_string)
    if not program_input.endswith(".py"):
        err = f"{program_input} either does not exist or is not a valid Python program."
        return err
    if not isinstance(input_string, str):
        err = f"{input_string} is not a string!"
        return err


def decider(program_input: str, input_string: str):
    """Decide if yesOnString works well."""
    result = "yes"
    expected_resut = yesOnString("troublemaker.py", "some_string")

    if expected_resut == result:
        print("yes")
    else:
        print("false")

decider(program_input="yesOnString.py", input_string="hello")
