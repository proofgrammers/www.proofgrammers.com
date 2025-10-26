#include <iostream>
#include <algorithm>
#include <cctype>

std::string lower(std::string input) {
    std::string string_lower;
    std::transform(input.begin(), input.end(), string_lower.begin(),
                [](unsigned char character){return std::tolower(character);});
    return string_lower;
};

void lastTtoA() {
    std::string input = lower;
}
