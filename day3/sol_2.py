from string import ascii_letters
lines = open('input.txt').read().strip().split('\n')

score = 0

for i in range(0, len(lines), 3):
    badge = list(set(lines[i]).intersection(lines[i+1], lines[i+2]))[0]
    score += ascii_letters.index(badge) + 1

print(score)
