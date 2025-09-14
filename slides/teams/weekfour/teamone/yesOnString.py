"""This file contains a basic yesOnString function."""

def yesOnString(program_input: str, input_string: str):
    """Return yes on valid P, if input is defnied and P(I) is yes."""
    try:
        if program_input == 'returnYesOnString.py':
            return returnYesOnString(input_string)
    except FileNotFoundError:
        print(f"{program_input} either does not exist or is not a valid Python program.")
