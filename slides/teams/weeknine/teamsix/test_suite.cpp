#include <iostream>
#include <algorithm>
#include <string>

/**
 * LastTtoA C++ Implementation
 * Strategy: Reverse string, find first T (which is last in original),
 * replace it, then reverse back.
 */
std::string lastTtoA_cpp(std::string input_string) {
    // Reverse the string so last T becomes first
    std::reverse(input_string.begin(), input_string.end());
    
    // Find the first T (which was the last T in original string)
    std::size_t position = input_string.find('T');
    
    // If no T found, reverse back and return unchanged
    if (position == std::string::npos) {
        std::reverse(input_string.begin(), input_string.end());
        return input_string;
    }
    
    // Replace the T with A
    input_string[position] = 'A';
    
    // Reverse back to original order
    std::reverse(input_string.begin(), input_string.end());
    return input_string;
}

int main() {
    std::cout << "Testing C++ LastTtoA Implementation" << std::endl;
    std::cout << "====================================" << std::endl;
    
    // Test cases
    std::string test_cases[][2] = {
        {"ATCGT", "ATCGA"},
        {"TTTT", "TTTA"},
        {"ACGAA", "ACGAA"},
        {"T", "A"},
        {"", ""}
    };
    
    bool all_passed = true;
    
    for (const auto& test : test_cases) {
        std::string input = test[0];
        std::string expected = test[1];
        std::string result = lastTtoA_cpp(input);
        
        bool passed = (result == expected);
        std::cout << (passed ? "  ✓ " : "  ✗ ");
        std::cout << "'" << input << "' → '" << result << "'";
        if (!passed) {
            std::cout << " (expected '" << expected << "')";
            all_passed = false;
        }
        std::cout << std::endl;
    }
    
    std::cout << "\n====================================" << std::endl;
    std::cout << (all_passed ? "✓ ALL TESTS PASSED" : "✗ SOME TESTS FAILED") << std::endl;
    
    return 0;
}
