#include <iostream>
#include <algorithm>
#include <string>

std::string lastTtoA_cpp(std::string input_string) {
    std::reverse(input_string.begin(), input_string.end());
    char const replace_letter = 'T';
    char const replace_with = 'A';

    std::size_t position = input_string.find(replace_letter);
    if(position == std::string::npos) {
        std::reverse(input_string.begin(), input_string.end());
        return input_string;
    }
    
    input_string[position] = replace_with;
    
    std::string normal_string;
    for (int i = input_string.length() - 1; i >= 0; --i) {
        normal_string += input_string[i];
    }
    return normal_string;
}

int main() {
    std::string result1 = lastTtoA_cpp("ATCGT");
    std::cout << "ATCGT -> " << result1 << std::endl;
    
    std::string result2 = lastTtoA_cpp("atcgt");
    std::cout << "atcgt -> " << result2 << std::endl;
    
    std::string result3 = lastTtoA_cpp("AtCgT");
    std::cout << "AtCgT -> " << result3 << std::endl;
    
    return 0;
}
