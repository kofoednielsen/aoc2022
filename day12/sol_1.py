import sys
from itertools import chain
from time import time

sys.setrecursionlimit(100000000)

grid = open("input.txt").read().strip().split("\n")

optimal_grid = [[999 for _ in range(len(grid[0]))] for c in range(len(grid))]

print(len(optimal_grid))
print(len(optimal_grid[0]))

def sum_optimal_grid():
    visited = len(list(filter(lambda n: n != 999, chain(*optimal_grid))))
    print(f"{visited} {visited / 5760} %")

last_print = time()

start = (0, 0)
end = (0, 0)
for y, row in enumerate(grid):
    if "S" in row:
        start = (row.index("S"), y)
        grid[y] = grid[y].replace("S", "a")
    if "E" in row:
        end = (row.index("E"), y)
        grid[y] = grid[y].replace("E", "z")


def find_end(position, visited):
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
        if direction in visited:
            return False
        if optimal_grid[direction[1]][direction[0]] <= len(visited) + 1:
            return False

        current = grid[position[1]][position[0]]
        destination = grid[direction[1]][direction[0]]

        height_diff = ord(destination) - ord(current)
        if height_diff > 1 or height_diff < 0:
            return False

        optimal_grid[direction[1]][direction[0]] = len(visited) + 1
        return True

    possible = list(filter(is_possible, directions))
    if end in possible:
        return len(visited) + 1

    return min(
        [
            *[
                find_end(direction, set([*visited, direction]))
                for direction in possible
            ],
            999,
        ]
    )


[print(r) for r in grid]
print(find_end(start, set([])))
sum_optimal_grid()

#for r in optimal_grid:
#    for c in r:
#        print(str(c).ljust(3, ' '), end=" ")
#    print()
#    print()
