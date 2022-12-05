lines = open("input.txt").read().strip().replace("[", "").replace("]", "").split("\n")

stacks = []

for stack in lines[:9]:
    stacks.append(list(stack))

for line in lines[9:]:
    amount, from_create, to_create = [int(c) for c in line.split(' ')]
    for _ in range(amount):
        stacks[to_create-1].append(stacks[from_create-1].pop())

for stack in stacks:
    print(stack[-1], end="")
print()
