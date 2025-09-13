# include any created code here - thanks!

# book references:
    # Exercise 3.10 (pg 43)
    # figure 3.9 (pg 38)
    # claim 3.4 (pg 38)
    
# "rf" function: read a program file as a string
def rf(filename: str) -> str:
    with open(filename, "r") as f:
        return f.read()

# Case 1
def DefinedOnString(program_code : str, inString : str) -> bool:
    """When given a program and an input string, returns True if the program halts on that input."""
    return True # Assume it halts for demonstration

def Paradox():
    """A paradoxical function that uses DefinedOnString to create a contradiction."""
   
    my_source = rf(__file__) # read this file as a string
    if DefinedOnString(my_source, my_source):
        print("Checker says: halts → looping forever...")
        while True:
            pass
    else:
        print("Checker says: does not halt → halting now.")
        return "halted"

# Paradox()


# Case 2
def DefinedOnString(program_code : str, inString : str) -> bool:
    """When given a program and an input string, returns True if the program halts on that input."""
    return False # Assume it does not halt for demonstration

def Paradox():
    """A paradoxical function that uses DefinedOnString to create a contradiction."""
   
    my_source = rf(__file__) # read this file as a string
    if DefinedOnString(my_source, my_source):
        print("Checker says: halts → looping forever...")
        while True:
            pass
    else:
        print("Checker says: does not halt → halting now.")
        return "halted"
    
Paradox()
