"""Implementing LastTtoA function using regex."""

import re

def main(input: str):
    tape = list(input)
    
    current_state = "search"
    head_position = 0
    last_t_position = -1

    while current_state != "halt":
        




input = "atatatatatata"
print(main(input))
