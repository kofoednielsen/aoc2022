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

visible_trees = 0
for x in range(len(rows)):
    for y in range(len(columns)):
        if (max([*rows[y][:x], -1]) < rows[y][x] or
           max([*rows[y][x+1:], -1]) < rows[y][x] or 
           max([*columns[x][:y], -1]) < rows[y][x] or
           max([*columns[x][y+1:], -1]) < rows[y][x]):
            visible_trees += 1

print(visible_trees)
