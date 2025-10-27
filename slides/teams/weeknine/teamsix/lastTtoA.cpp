#include <iostream>
#include <algorithm>
#include <cctype>

std::string lower(std::string input) {
    std::transform(input.begin(), input.end(), input.begin(),
                [](unsigned char character){return std::tolower(character);});
    return input;
};

std::string lower_text = lower("TTTTT");

void lastTtoA() {
    std::string& input_string = lower_text;
    std::reverse(input_string.begin(), input_string.end()); // string reverse so first element is the last
    char const& replace_letter = 't';
    char const& replace_with = 'a';

    std::size_t position = input_string.find(replace_letter);
    if(position == std::string::npos) return;
    if(position != std::string::npos){
      input_string.replace(position, 1, 1, replace_with);
    }
    // The line below replaces every T found in the text
    //std::replace(input_string.begin(), input_string.end(), replace_letter, replace_with);
 
    // logic to re-reverse input string
    std::string normal_string;
    for (int i = input_string.length() - 1; i>= 0; --i) {
        normal_string += input_string[i];
    }
    std::cout << normal_string;
}

int main() {
    lastTtoA();
}
