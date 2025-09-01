import random
import string


# Path of text file
path = "input.txt"

# Read the original text
with open(path, "r") as file:
    text = file.read()
print("Original Text:", text)

def mutate_text(text, mutation_rate=0.1):
    mutated = ""
    for char in text:
        if random.random() < mutation_rate:
            mutated += random.choice(string.ascii_letters)
        else:
            mutated += char
    return mutated

mutated_text = mutate_text(text, mutation_rate=0.2)

print("Mutated Text:", mutated_text)

with open("mutated.txt", "w") as file:
    file.write(mutated_text)