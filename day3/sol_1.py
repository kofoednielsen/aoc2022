from string import ascii_letters
lines = open('input.txt').read().strip().split('\n')

score = 0

for line in lines:
    compartment_1 = set(line[:len(line)//2])
    compartment_2 = set(line[len(line)//2:])
    in_both = list(compartment_1.intersection(compartment_2))[0]
    score += ascii_letters.index(in_both) + 1

print(score)
