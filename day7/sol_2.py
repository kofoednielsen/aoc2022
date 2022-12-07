commands = open('input.txt').read().strip().split('$')
pwd = []

sizes = {}

for command in commands:
    if not command:
        continue
    lines = command.strip().split('\n')
    if lines[0].startswith('cd'):
        target = lines[0].split(' ')[1]
        if target == '..':
            pwd.pop()
        else:
            pwd.append(target)
    if lines[0].startswith('ls'):
        for file in lines[1:]:
            if not file.startswith('dir'):
                size = int(file.split(' ')[0])
                for i in range(1, len(pwd)+1):
                    key = '/'.join(pwd[:i])
                    sizes[key] = size + sizes.get(key, 0)                


print(min(filter(lambda s: s >= 30000000-(70000000-sizes['/']), sizes.values())))
