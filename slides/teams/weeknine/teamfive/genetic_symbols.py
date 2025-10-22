"""Genetic symbol analysis functions for DNA strings."""

# cd slides/teams/weeknine/teamfive && uv run genetic_symbols.py

def count_cs(dna: str) -> int:
    """Returns the number of occurrences of the symbol C in DNA."""
    return dna.count("C")

def count_ns(dna: str, n: str) -> int:
    """Returns the number of occurrences of the symbol N in DNA."""
    return dna.count(n)

def more_cs_than_gs(dna: str) -> bool:
    """Returns True if DNA contains more Cs than Gs; otherwise False."""
    return count_cs(dna) > count_ns(dna, "G") 

def has_more_ns_than_ms(dna: str, n: str, m: str) -> bool:
    """Returns True if DNA contains more Ns than Ms; otherwise False."""
    return count_ns(dna, n) > count_ns(dna, m)

if __name__ == "__main__":
    example_dna = "ACCTCGACCCGT"
    print(f"DNA string: {example_dna}")
    print(f"Count of Cs: {count_cs(example_dna)}")
    print(f"Count of Gs: {count_ns(example_dna, "G")}")
    print(f"More Cs than Gs? {more_cs_than_gs(example_dna)}")
    print(f"More Ns than Ms? {has_more_ns_than_ms(example_dna, "A", "T")}")
