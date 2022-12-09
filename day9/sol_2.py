from time import sleep
import os
lines = open('input.txt').read().strip().split('\n')

have_been = set()

def move_tail(head, tail):
    # this is garbage 🗑️
    dist_x = head[0] - tail[0]
    dist_y = head[1] - tail[1]
    if dist_x > 1:
        tail = (tail[0]+1, tail[1])
        if dist_y > 0:
            tail = (tail[0], tail[1]+1)
        if dist_y < 0:
            tail = (tail[0], tail[1]-1)
    elif dist_x < -1:
        tail = (tail[0]-1, tail[1])
        if dist_y > 0:
            tail = (tail[0], tail[1]+1)
        if dist_y < 0:
            tail = (tail[0], tail[1]-1)
    elif dist_y > 1:
        tail = (tail[0], tail[1]+1)
        if dist_x > 0:
            tail = (tail[0]+1, tail[1])
        if dist_x < 0:
            tail = (tail[0]-1, tail[1])
    elif dist_y < -1:
        tail = (tail[0], tail[1]-1)
        if dist_x > 0:
            tail = (tail[0]+1, tail[1])
        if dist_x < 0:
            tail = (tail[0]-1, tail[1])
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
        #os.system('clear')
        #for y in reversed(range(-20,20)):
        #    for x in range(-20,20):
        #        for i, tail in enumerate(snake):
        #            if (x,y) == tail:
        #                print(i, end='')
        #                break
        #        else:
        #            print('.', end='')
        #    print()

#os.system('clear')
#for y in reversed(range(-20,20)):
#    for x in range(-20,20):
#        if (x,y) in have_been:
#            print('#', end='')
#        else:
#            print('.', end='')
#    print()
print(len(have_been))
