import math

lines = open('input.txt').read().strip().split('\n')

have_been = set()

def magic(x):
    # 🪄
    if x == 0:
        return 0
    return math.copysign(1, x) 

def move_tail(head, tail):
    # less garbage ✨
    dist_x = head[0] - tail[0]
    dist_y = head[1] - tail[1]
    if abs(dist_x) > 1 or abs(dist_y) > 1:
        return (tail[0] + magic(dist_x), tail[1] + magic(dist_y))
    return tail

snake = [(0,0)] * 10
for line in lines:
    direction, distance = line.split(' ')
    for _ in range(int(distance)):
        if direction == 'U':
            snake[0] = (snake[0][0], snake[0][1] + 1)
        elif direction == 'D':
            snake[0] = (snake[0][0], snake[0][1] - 1)
        elif direction == 'R':
            snake[0] = (snake[0][0]+1, snake[0][1])
        elif direction == 'L':
            snake[0] = (snake[0][0]-1, snake[0][1])

        for i in range(1, len(snake)):
            snake[i] = move_tail(snake[i-1], snake[i])
            if i == len(snake)-1:
                have_been.add(snake[i])

print(len(have_been))
