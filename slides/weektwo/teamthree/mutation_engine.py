import random
import string


with open("/home/student/Theoretical_Machines/www.proofgrammers.com/slides/weektwo/teamthree/input.txt", "r") as file:
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