"""This file contains a basic yesOnString function."""

def returnYesOnString(some_string: str) -> str:
    """This function always says yes."""
    return "yes"

def yesOnString(program_input: str, input_string: str):
    """Return yes on valid P, if input is defnied and P(I) is yes."""
    if program_input == 'returnYesOnString.py' and isinstance(input_string, str):
            return returnYesOnString(input_string)
    else:
        error = (f"{program_input} either does not exist or is not a valid Python program.")
        return error

print(yesOnString("returnYesOnString.py", "Go Gators!")) # yes
print(yesOnString("returnYesOnString.cpp", "Go Gators!")) # exception case
print(yesOnString("returnYesOnString.py", 1)) # exception case
