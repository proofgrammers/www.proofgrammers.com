def lastTtoA_plain(dna: str) -> str:
    """Replace the last occurrence of 'T' with 'A' in the given DNA string."""
    # find the position of the last 'T'
    last_t_index = -1
    for i in range(len(dna)):
        if dna[i] == 'T':
            last_t_index = i

    # replace only if there was at least one 'T'
    if last_t_index == -1:
        return dna  # no change if no 'T'

    # construct a new string
    return dna[:last_t_index] + 'A' + dna[last_t_index + 1:]


# simple test calls
print("Testing Plain Python Implementation:")
print("ATCGT ->", lastTtoA_plain("ATCGT"))  # expected: ATCGA
print("TTTT ->", lastTtoA_plain("TTTT"))    # expected: TTTA
print("ACGA ->", lastTtoA_plain("ACGA"))    # expected: ACGA
print("T ->", lastTtoA_plain("T"))          # expected: A
print("'' ->", lastTtoA_plain(""))          # expected: (empty)
print("TATGCT ->", lastTtoA_plain("TATGCT"))  # expected: TATGCA
