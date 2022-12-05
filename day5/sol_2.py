lines = open("input.txt").read().strip().replace("[", "").replace("]", "").split("\n")

stacks = []

for stack in lines[:9]:
    stacks.append(stack)

for line in lines[9:]:
    amount, from_create, to_create = [int(c) for c in line.split(' ')]
    stacks[to_create-1] += stacks[from_create-1][-amount:]
    stacks[from_create-1] = stacks[from_create-1][:-amount]

for stack in stacks:
    print(stack[-1], end="")
print()
