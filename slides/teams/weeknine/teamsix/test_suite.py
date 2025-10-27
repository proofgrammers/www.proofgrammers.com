#!/usr/bin/env python3
"""
Test suite for LastTtoA implementations.
Tests three approaches: Turing Machine, Pure Python, and Regex.
"""

import sys
from io import StringIO

# Import the three implementations
from turing_lastTtoA import turing_lastTtoA
from plain_lastTtoA import lastTtoA_plain
from lastTtoA_regex import main as regex_main


def test_regex(input_str):
    """Wrapper to capture regex output (since it prints instead of returning)."""
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    try:
        regex_main(input_str)
        return captured_output.getvalue().strip()
    finally:
        sys.stdout = old_stdout


def main():
    """Run tests on all three implementations."""
    # Test cases: (input, expected_output)
    test_cases = [
        ("ATCGT", "ATCGA"),   # Basic case
        ("TTTT", "TTTA"),     # Multiple T's
        ("ACGAA", "ACGAA"),   # No T's
        ("T", "A"),           # Single T
        ("", ""),             # Empty string
    ]
    
    # List of implementations to test
    implementations = [
        ("Turing Machine", turing_lastTtoA),
        ("Pure Python", lastTtoA_plain),
        ("Regex Python", test_regex)
    ]
    
    print("Testing LastTtoA Implementations")
    print("=" * 40)
    
    all_passed = True
    
    for name, func in implementations:
        print(f"\n{name}:")
        for input_str, expected in test_cases:
            try:
                result = func(input_str)
                # Note: Regex returns lowercase, others return uppercase
                if name == "Regex Python":
                    expected = expected.lower()
                
                if result == expected:
                    print(f"  ✓ '{input_str}' → '{result}'")
                else:
                    print(f"  ✗ '{input_str}' → '{result}' (expected '{expected}')")
                    all_passed = False
            except Exception as e:
                print(f"  ✗ '{input_str}' → ERROR: {e}")
                all_passed = False
    
    # Print final result
    print("\n" + "=" * 40)
    if all_passed:
        print("✓ ALL TESTS PASSED")
    else:
        print("✗ SOME TESTS FAILED")


if __name__ == "__main__":
    main()
