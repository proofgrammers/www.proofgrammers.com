def turing_lastTtoA(tape_input: str) -> str:
    # init the tape as a list of symbols + a blank at the end
    tape = list(tape_input) + ['_']
    head = 0
    state = 'q0'

    while state != 'qhalt':
        symbol = tape[head]

        # state q0: move right until we find a blank
        if state == 'q0':
            if symbol in {'A', 'C', 'G', 'T'}:
                head += 1
            elif symbol == '_':
                state = 'q1'
                head -= 1  # move left
            else:
                raise ValueError(f"Unexpected symbol: {symbol}")

        # state q1: move left until we find the last T
        elif state == 'q1':
            if symbol == 'T':
                tape[head] = 'A'
                state = 'qhalt'  # halt after replacement
            elif symbol == '_':
                # no T found, halt without changes
                state = 'qhalt'
            else:
                head -= 1  # move left

        # safety: make sure head never goes below zero
        if head < 0:
            state = 'qhalt'  # halt if we reach the beginning

    # return everything before the first blank
    return ''.join([s for s in tape if s != '_'])


# simple test calls
print("Testing Turing Machine Implementation:")
print("ATCGT ->", turing_lastTtoA("ATCGT"))  # Expected: ATCGA
print("TTTT ->", turing_lastTtoA("TTTT"))    # Expected: TTTA
print("ACGA ->", turing_lastTtoA("ACGA"))    # Expected: ACGA
print("T ->", turing_lastTtoA("T"))          # Expected: A
print("'' ->", turing_lastTtoA(""))          # Expected: (empty)
print("TATGCT ->", turing_lastTtoA("TATGCT"))  # Expected: TATGCA
