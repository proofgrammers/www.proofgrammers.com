#!/usr/bin/env python3
"""
LastTtoA Problem - Deterministic Turing Machine Implementation
==============================================================

This module implements a formal Turing machine that solves the LastTtoA problem:
replacing the last occurrence of 'T' with 'A' in a DNA string.

Author: Proofgrammers Team
Date: 2025-10-23
"""

class TuringMachine:
    """
    A deterministic Turing machine implementation for the LastTtoA problem.
    
    Formal Definition: M = (Q, Σ, Γ, δ, q₀, qₐccₑₚₜ, qᵣₑⱼₑcₜ)
    - Q: {q0, q1, q2, qaccept}
    - Σ: {A, C, T, G} (input alphabet)
    - Γ: {A, C, T, G, □} (tape alphabet)
    - δ: transition function defined in self.transitions
    - q₀: q0 (start state)
    - qₐccₑₚₜ: qaccept (accept state)
    """
    
    def __init__(self):
        self.states = {'q0', 'q1', 'q2', 'qaccept'}
        self.input_alphabet = {'A', 'C', 'T', 'G'}
        self.tape_alphabet = {'A', 'C', 'T', 'G', '□'}
        self.start_state = 'q0'
        self.accept_state = 'qaccept'
        
        # Transition function δ(state, symbol) = (new_state, write_symbol, direction)
        self.transitions = {
            # Phase 1: Move to end of string (q0)
            ('q0', 'A'): ('q0', 'A', 'R'),
            ('q0', 'C'): ('q0', 'C', 'R'),
            ('q0', 'T'): ('q0', 'T', 'R'),
            ('q0', 'G'): ('q0', 'G', 'R'),
            ('q0', '□'): ('q1', '□', 'L'),
            
            # Phase 2: Move left looking for last T (q1)
            ('q1', 'A'): ('q1', 'A', 'L'),
            ('q1', 'C'): ('q1', 'C', 'L'),
            ('q1', 'G'): ('q1', 'G', 'L'),
            ('q1', 'T'): ('q2', 'A', 'R'),  # Found last T, replace with A
            ('q1', '□'): ('qaccept', '□', 'R'),  # No T found, accept
            
            # Phase 3: Move to end and accept (q2)
            ('q2', 'A'): ('q2', 'A', 'R'),
            ('q2', 'C'): ('q2', 'C', 'R'),
            ('q2', 'T'): ('q2', 'T', 'R'),
            ('q2', 'G'): ('q2', 'G', 'R'),
            ('q2', '□'): ('qaccept', '□', 'L'),
        }
    
    def run(self, input_string, verbose=False):
        """
        Run the Turing machine on the given input string.
        
        Args:
            input_string (str): DNA string containing only A, C, T, G
            verbose (bool): If True, print step-by-step execution
            
        Returns:
            tuple: (result_string, execution_steps)
        """
        # Initialize tape with input string and blank symbol at end
        tape = list(input_string) + ['□']
        head = 0
        state = self.start_state
        
        # Track steps for analysis
        steps = []
        step_count = 0
        max_steps = len(input_string) * 10  # Prevent infinite loops
        
        if verbose:
            print(f"Starting Turing Machine execution...")
            print(f"Input: '{input_string}'")
            print(f"Initial tape: {''.join(tape)}")
            print("-" * 50)
        
        while state != self.accept_state and step_count < max_steps:
            if head >= len(tape):
                tape.append('□')
            
            current_symbol = tape[head]
            
            # Record current configuration
            config = {
                'step': step_count,
                'state': state,
                'tape': ''.join(tape),
                'head': head,
                'symbol': current_symbol
            }
            steps.append(config)
            
            if verbose:
                tape_display = list(tape)
                tape_display[head] = f"[{current_symbol}]"
                print(f"Step {step_count}: State={state}, Tape={''.join(tape_display)}")
            
            if (state, current_symbol) not in self.transitions:
                if verbose:
                    print(f"No transition defined for state={state}, symbol={current_symbol}")
                break
                
            new_state, write_symbol, direction = self.transitions[(state, current_symbol)]
            
            # Write symbol to tape
            tape[head] = write_symbol
            
            # Move head
            if direction == 'R':
                head += 1
            elif direction == 'L':
                head -= 1
                if head < 0:
                    tape.insert(0, '□')
                    head = 0
            
            state = new_state
            step_count += 1
        
        if verbose:
            print("-" * 50)
            print(f"Final state: {state}")
            print(f"Steps taken: {step_count}")
        
        # Extract result (remove blank symbols)
        result = ''.join(tape).replace('□', '')
        
        if verbose:
            print(f"Result: '{result}'")
        
        return result, steps
    
    def analyze_complexity(self, input_string):
        """
        Analyze the time and space complexity for the given input.
        
        Args:
            input_string (str): Input to analyze
            
        Returns:
            dict: Analysis results
        """
        result, steps = self.run(input_string)
        
        analysis = {
            'input_length': len(input_string),
            'steps_taken': len(steps),
            'time_complexity': f"O({len(input_string)})",
            'space_complexity': f"O({len(input_string)})",
            'tape_cells_used': len(input_string) + 1,
            'states_visited': len(set(step['state'] for step in steps)),
            'result': result
        }
        
        return analysis


def test_turing_machine():
    """Test the Turing machine with various inputs."""
    tm = TuringMachine()
    
    test_cases = [
        ("ATCGT", "ATCGA"),
        ("TTACG", "TTACG"),  # Last T should become A: TTACG -> TTACG
        ("ACGAA", "ACGAA"),
        ("T", "A"),
        ("", ""),
        ("TTTAAA", "TTAAAA"),
        ("AAATTT", "AAAATT"),
    ]
    
    print("=== TURING MACHINE TEST RESULTS ===\n")
    
    all_passed = True
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result, steps = tm.run(test_input)
        passed = result == expected
        status = "✓ PASS" if passed else "✗ FAIL"
        
        print(f"Test {i}: '{test_input}' → '{result}' (expected: '{expected}') {status}")
        
        if not passed:
            all_passed = False
            print(f"  ERROR: Expected '{expected}', got '{result}'")
        
        # Show complexity analysis for first few tests
        if i <= 3:
            analysis = tm.analyze_complexity(test_input)
            print(f"  Steps: {analysis['steps_taken']}, "
                  f"Time: {analysis['time_complexity']}, "
                  f"Space: {analysis['space_complexity']}")
        
        print()
    
    print(f"Overall Result: {'✓ ALL TESTS PASSED' if all_passed else '✗ SOME TESTS FAILED'}")
    return all_passed


if __name__ == "__main__":
    # Run tests
    test_turing_machine()
    
    # Demonstrate verbose execution
    print("\n=== VERBOSE EXECUTION EXAMPLE ===")
    tm = TuringMachine()
    tm.run("ATCGT", verbose=True)
