from typing import Dict, Set, List, Tuple
from dataclasses import dataclass

@dataclass
class Transition:
    """Represents a transition in a Turing machine."""
    current_state: str
    read_symbol: str
    next_state: str
    write_symbol: str
    move_direction: str  # 'L' for left, 'R' for right

class TuringMachine:
    """Represents a Turing machine with its states and transitions."""
    
    def __init__(self):
        self.states: Set[str] = set()
        self.transitions: List[Transition] = []
        self.alphabet: Set[str] = set()
        self.initial_state: str = None
        self.accept_state: str = None
        self.reject_state: str = None

    def add_transition(self, transition: Transition):
        """Add a transition to the Turing machine."""
        self.states.add(transition.current_state)
        self.states.add(transition.next_state)
        self.alphabet.add(transition.read_symbol)
        self.alphabet.add(transition.write_symbol)
        self.transitions.append(transition)

def has_cycles(tm: TuringMachine) -> bool:
    """
    Determine if a Turing machine's state diagram contains cycles using DFS.
    Returns True if cycles are found, False otherwise.
    
    This is computable because we're only analyzing the static structure
    of the state diagram, not the machine's behavior on any input.
    
    Time Complexity: O(V + E) where V is number of states and E is number of transitions
    Space Complexity: O(V) for the visited set and recursion stack
    """
    def dfs(state: str, visited: Set[str], rec_stack: Set[str]) -> bool:
        # If state is in recursion stack, we found a cycle
        if state in rec_stack:
            return True
            
        # If already visited and not in recursion stack, no cycle here
        if state in visited:
            return False
            
        # Add state to both visited and recursion stack
        visited.add(state)
        rec_stack.add(state)
        
        # Check all transitions from current state
        for transition in tm.transitions:
            if transition.current_state == state:
                if dfs(transition.next_state, visited, rec_stack):
                    return True
                    
        # Remove state from recursion stack
        rec_stack.remove(state)
        return False

    visited: Set[str] = set()
    rec_stack: Set[str] = set()
    
    # Try DFS from each unvisited state
    for state in tm.states:
        if state not in visited:
            if dfs(state, visited, rec_stack):
                return True
                
    return False

def test_cycle_detection():
    """Test the cycle detection with example Turing machines."""
    # Example 1: TM with a cycle
    tm1 = TuringMachine()
    tm1.add_transition(Transition("q0", "1", "q1", "1", "R"))
    tm1.add_transition(Transition("q1", "1", "q2", "1", "R"))
    tm1.add_transition(Transition("q2", "1", "q0", "1", "R"))  # cycle here
    print(has_cycles(tm1)) # expected output should be true
    
    # Example 2: TM without cycles
    tm2 = TuringMachine()
    tm2.add_transition(Transition("q0", "1", "q1", "1", "R"))
    tm2.add_transition(Transition("q1", "1", "q2", "1", "R"))
    tm2.add_transition(Transition("q2", "1", "q3", "1", "R"))
    print(has_cycles(tm2))  # expected output is False
    
    # Example 3: TM with immediate cycle
    tm3 = TuringMachine()
    tm3.add_transition(Transition("q0", "1", "q0", "1", "R"))  # self-loop
    print(has_cycles(tm3))  # expected output is True

if __name__ == "__main__":
    test_cycle_detection()