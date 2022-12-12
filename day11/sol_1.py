lines = open('input.txt').read().strip().split('\n')

monkeys = []

monkey = -1 
for line in lines:
    line = line.strip()
    if line.startswith('Monkey'):
        monkey += 1  
        monkeys.append({})
    if line.startswith('Starting items'):
        monkeys[monkey]['items'] = [int(item) for item in line.split(': ')[1].split(',')]
    if line.startswith('Operation'):
        monkeys[monkey]['operation'] = line.split(': ')[1]
    if line.startswith('Test'):
        monkeys[monkey]['divider'] = int(line.split('by ')[1])
    if line.startswith('If true'):
        monkeys[monkey]['true'] = int(line.split('monkey ')[1])
    if line.startswith('If false'):
        monkeys[monkey]['false'] = int(line.split('monkey ')[1])

        
monkey_actions = [0 for _ in monkeys]
for _ in range(20):
    for i, monkey in enumerate(monkeys):
        for old in monkey['items']:
            monkey_actions[i] += 1
            exec(monkey['operation'])
            worry_level = new // 3
            target_monkey = None
            if worry_level % monkey['divider'] == 0:
                target_monkey = monkey['true'] 
            else:
                target_monkey = monkey['false'] 
            monkeys[target_monkey]['items'].append(worry_level)
        monkey['items'] = []

for monkey in monkeys:
    print(monkey)
sorted_actions = list(sorted(monkey_actions))
print(sorted_actions[-2] * sorted_actions[-1])
