#!/usr/bin/env python3
"""
Comprehensive test suite for all LastTtoA implementations.
Tests Turing machine, pure Python, and regex implementations.
"""

import re
from typing import List, Tuple, Callable
from lastTtoA_regex import main as lastTtoA_regex
from turing_lastTtoA import turing_lastTtoA
from plain_lastTtoA import lastTtoA_plain



def test_all_implementations() -> None:
    """Test all LastTtoA implementations with comprehensive test cases."""
    test_cases: List[Tuple[str, str]] = [
        ("ATCGT", "ATCGA"),      # Basic case
        ("TTTT", "TTTA"),        # Multiple T's
        ("ACGAA", "ACGAA"),      # No T's
        ("T", "A"),              # Single T
        ("", ""),                # Empty string
        ("ACGTACGT", "ACGTACGA"), # Complex case
        ("ATCGATCG", "ATCGATCA"), # Multiple T's, last one
        ("GGGGGGGG", "GGGGGGGG"), # No T's
        ("TTTTTTTT", "TTTTTTTA"), # All T's
    ]
    
    implementations: List[Tuple[str, Callable[[str], str]]] = [
        ("Turing Machine", turing_lastTtoA),
        ("Pure Python", lastTtoA_plain),
        ("Regex Python", lastTtoA_regex)
    ]
    
    print("=" * 60)
    print("COMPREHENSIVE TEST SUITE FOR LASTTTOA IMPLEMENTATIONS")
    print("=" * 60)
    
    all_passed = True
    
    for name, func in implementations:
        print(f"\nTesting {name}:")
        print("-" * 40)
        passed = 0
        failed = 0
        
        for input_str, expected in test_cases:
            try:
                result = func(input_str)
                if result == expected:
                    status = "✓ PASS"
                    passed += 1
                else:
                    status = "✗ FAIL"
                    failed += 1
                    all_passed = False
                print(f"  {status} '{input_str}' → '{result}' (expected: '{expected}')")
            except Exception as e:
                print(f"  ✗ ERROR '{input_str}' → Exception: {e}")
                failed += 1
                all_passed = False
        
        print(f"\n  Summary: {passed} passed, {failed} failed")
    
    print("\n" + "=" * 60)
    if all_passed:
        print("🎉 ALL TESTS PASSED - All implementations are correct!")
    else:
        print("❌ SOME TESTS FAILED - Check implementation logic")
    print("=" * 60)


def performance_comparison() -> None:
    """Compare performance of different implementations."""
    import time
    
    test_string = "ATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG" * 100  # Large string
    
    implementations = [
        ("Turing Machine", turing_lastTtoA),
        ("Pure Python", lastTtoA_plain),
        ("Regex Python", lastTtoA_regex)
    ]
    
    print("\n" + "=" * 60)
    print("PERFORMANCE COMPARISON")
    print("=" * 60)
    print(f"Test string length: {len(test_string)} characters")
    
    for name, func in implementations:
        start_time = time.time()
        func(test_string)  # Execute function but don't store result
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
        
        print(f"{name:15}: {execution_time:.2f} ms")
    
    print("=" * 60)


if __name__ == "__main__":
    test_all_implementations()
    performance_comparison()
