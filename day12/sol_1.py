import sys
from itertools import chain
from time import time

sys.setrecursionlimit(100000000)

grid = open("input.txt").read().strip().split("\n")

optimal_grid = [[999 for _ in range(len(grid[0]))] for c in range(len(grid))]


def sum_optimal_grid():
    visited = len(list(filter(lambda n: n != 999, chain(*optimal_grid))))
    print(f"{visited} {visited / 140*41} %")


start = (0, 0)
end = (0, 0)
for y, row in enumerate(grid):
    if "S" in row:
        start = (row.index("S"), y)
        grid[y] = grid[y].replace("S", "a")
    if "E" in row:
        end = (row.index("E"), y)
        grid[y] = grid[y].replace("E", "z")

print(start)
print(end)


def find_end(position, steps):
    directions = [
        (position[0] + 1, position[1]),
        (position[0] - 1, position[1]),
        (position[0], position[1] + 1),
        (position[0], position[1] - 1),
    ]

    def is_possible(direction):
        if (
            direction[0] >= len(grid[0])
            or direction[1] >= len(grid)
            or direction[0] < 0
            or direction[1] < 0
        ):
            # out of grid bounds
            return False
        if optimal_grid[direction[1]][direction[0]] <= (steps + 1):
            return False

        current = grid[position[1]][position[0]]
        destination = grid[direction[1]][direction[0]]

        height_diff = ord(destination) - ord(current)
        if height_diff > 1:
            return False

        optimal_grid[direction[1]][direction[0]] = steps + 1
        return True

    possible = list(filter(is_possible, directions))
    if end in possible:
        return steps + 1

    return min(
        [
            *[
                find_end(direction, steps+1)
                for direction in possible
            ],
            999
        ]
    )


[print(r) for r in grid]
print(find_end(start, 0))
sum_optimal_grid()

# for y, r in enumerate(optimal_grid):
#     for x, c in enumerate(r):
#         if x > 100 and x < 140:
#             print(grid[y][x] + ' ' + str(c).ljust(3, ' '), end=" ")
#     print()
