from functools import reduce
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


common_diviser = reduce(lambda x,y: x*y, (m['divider'] for m in monkeys))
print(common_diviser)
        
monkey_actions = [0 for _ in monkeys]
for i in range(10000):
    print(f"{i/10000} %")
    for i, monkey in enumerate(monkeys):
        for old in monkey['items']:
            monkey_actions[i] += 1
            exec(monkey['operation'])
            worry_level = new % common_diviser
            target_monkey = None
            if worry_level % monkey['divider'] == 0:
                target_monkey = monkey['true'] 
            else:
                target_monkey = monkey['false'] 
            monkeys[target_monkey]['items'].append(worry_level)
        monkey['items'] = []

print(monkey_actions)
sorted_actions = list(sorted(monkey_actions))
print(sorted_actions[-2] * sorted_actions[-1])
print(common_diviser)
[print(m['divider']) for m in monkeys]
