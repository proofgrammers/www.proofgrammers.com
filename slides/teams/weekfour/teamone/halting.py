"""Similarity to the Halting problem using yesOnString's logic."""
    

def yesOnString(program_input: str, input_string: str):
    """Return yes on valid P, if input is defined and P(I) is yes."""
    if program_input == "easemaker.py" and isinstance(input_string, str):
        return easemaker(program_input)
    if not program_input.endswith(".py"):
        err = f"{program_input} either does not exist or is not a valid Python program."
        return err
    if not isinstance(input_string, str):
        err = f"{input_string} is not a string!"
        return err

def easemaker(some_string: str):
    prediction = yesOnString("easemaker.py", "easemaker.py")
    if prediction == "yes":
        return "yes"
    else:
        return "no"

def halting():
    program_w = yesOnString("easemaker.py", "easemaker.py")
    while program_w:
        pass


def result():
    output = yesOnString("easemaker.py", "easemaker.py")
    print(f"yesOnString says: {output}")

result()
