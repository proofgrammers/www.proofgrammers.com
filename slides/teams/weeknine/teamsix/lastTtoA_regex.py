"""Implementing LastTtoA function using regex."""
import re

def main(input_str: str):
    input = input_str.lower()
    last_t_position = -1
    search_for_t = r"t"
    found_t = re.finditer(search_for_t, input)
    last_match = None

    for find_t in found_t:
        last_match = find_t

    if last_match is not None:
        last_t_position = last_match.start()
        output = input[:last_t_position] + 'a' + input[last_t_position+1:]
    else:
        output = input

    print(output)




if __name__ == "__main__":
    main("ATCGT")
    main("TTTT")
    main("ACGAA")
    main("T")
