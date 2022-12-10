lines = open('input.txt').read().strip().split('\n')

x = 1
cycles = 0
total = 0
sum_cycles = [20, 60, 100, 140, 180, 220]
pixels = [["🎄"]*40 for _ in range(6)]
for line in lines:
    args = line.split(' ')
    add_cycles = 1
    if args[0] == 'addx':
        add_cycles = 2

    for _ in range(add_cycles):
        if abs(cycles%40 - x) < 2:
            pixels[cycles//40][cycles%40] = '🎅'
        cycles += 1
        if cycles in sum_cycles:
            total += x * cycles

    if args[0] == 'addx':
        x += int(args[1])

print(total)
for row in pixels:
    for pixel in row:
        print(pixel, end="")
    print()
