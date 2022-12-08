data = open('input.txt').read().strip().split('\n')

rows = []
for row in data:
    rows.append([int(c) for c in row])


columns = []
for i in range(len(rows)):
    columns.append([])

for row in rows:
    for i in range(len(row)):
        columns[i].append(row[i])


def line_of_sight_length(trees, height):
    if not trees:
        return 0
    for i, tree in enumerate(trees):
        if tree >= height:
            return i+1
    return len(trees)

max_score = 0
for x in range(len(rows)):
    for y in range(len(columns)):
        height = rows[y][x]
        max_score = max(
            line_of_sight_length(list(reversed(rows[y][:x])), height) *
            line_of_sight_length(rows[y][x+1:], height) *
            line_of_sight_length(list(reversed(columns[x][:y])), height) *
            line_of_sight_length(columns[x][y+1:], height)
        , max_score)

print(max_score)
