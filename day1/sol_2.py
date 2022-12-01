lines = open('input.txt').read().split('\n')

max_sum = 0
running_sum=0

elfes = []

for line in lines:
    if line == '':
        elfes.append(running_sum)
        running_sum = 0
    else:
        running_sum += int(line)

print(sum(sorted(elfes)[-3:]))
