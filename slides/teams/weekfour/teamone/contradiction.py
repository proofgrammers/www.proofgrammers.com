"""Create a proof by contradiction for the yesOnString problem."""

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


def troublemaker(some_string: str):
    """Flip the answer: say 'no' if yesOnString predicts 'yes', else 'yes'."""
    prediction = yesOnString("troublemaker.py", "troublemaker.py")
    if prediction == "yes":
        return "no"
    else:
        return "yes"

def decider():
    """Show the contradiction when we ask about troublemaker on itself."""
    result = yesOnString("troublemaker.py", "troublemaker.py")
    print(f"yesOnString says: {result}")

decider()
