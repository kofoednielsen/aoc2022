lines = open('input.txt').read().strip().split('\n')

have_been = set()

T_x = 0
T_y = 0
H_x = 0
H_y = 0
for line in lines:

    direction, distance = line.split(' ')
    for _ in range(int(distance)):
        print("================")
        for x in range(10):
            for y in range(10):
                if x == H_x and y == H_y:
                    print('H', end='')
                elif x == T_x and y == T_y:
                    print('T', end='')
                else:
                    print('.', end='')
            print('\n', end='')
        if direction == 'U':
            H_y += 1
        elif direction == 'D':
            H_y -= 1
        elif direction == 'R':
            H_x += 1
        elif direction == 'L':
            H_x -= 1

        dist_x = H_x - T_x
        dist_y = H_y - T_y
        if dist_x > 1:
            T_x += 1
            if dist_y > 0:
                T_y += 1
            if dist_y < -0:
                T_y -= 1
        if dist_x < -1:
            T_x -= 1
            if dist_y > 0:
                T_y += 1
            if dist_y < -0:
                T_y -= 1
        if dist_y > 1:
            T_y += 1
            if dist_x > 0:
                T_x += 1
            if dist_x < -0:
                T_x -= 1
        if dist_y < -1:
            T_y -= 1
            if dist_x > 0:
                T_x += 1
            if dist_x < -0:
                T_x -= 1
            
        have_been.add((T_x,T_y))

print(len(have_been))

for x in range(10):
    for y in range(10):
        if (x,y) in have_been:
            print('#', end="")
        else:
            print('.', end='')
    print('\n', end="")
