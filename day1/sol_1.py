lines = open('input.txt').read().split('\n')

max_sum = 0
running_sum=0

for line in lines:
    if line == '':
        max_sum = max(running_sum, max_sum)
        running_sum = 0
    else:
        running_sum += int(line)

print(max_sum)
