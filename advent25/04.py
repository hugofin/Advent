grid = []
for line in open("04.txt"):
    row = []
    for space in line.strip():
        row.append(space)
    grid.append(row)

def print_rolls(grid):
    for row in grid:
        print(''.join(row))

def check(x, y):
    adjacent_rolls = 0

    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            t_y, t_x = y + j, x + j
            if (t_x >= 0 and t_x < len(grid[x]) and t_y >= 0 and t_y < (len(grid))):
                if grid[t_y][t_x] == '@' or grid[t_y][t_x] == 'x':
                    adjacent_rolls += 1

    if adjacent_rolls <= 4:
        grid[y][x] = 'x'
        return 1
    else:
        return 0

def remove_rolls(grid):
    rolls = 0
    for y, row in enumerate(grid):
        for x, spot in enumerate(row):
            if spot == '@':
                rolls += check(x,y)
    return grid, rolls

def replace_empty(grid):
    for y, row in enumerate(grid):
        for x, spot in enumerate(row):
            if spot == 'x':
                grid[y][x] = '.'
    return grid

total_rolls = 0
retrived_rolls = -1

while retrived_rolls != 0:
    newGrid, retrived_rolls = remove_rolls(grid)
    grid = replace_empty(newGrid)
    total_rolls += retrived_rolls

print_rolls(grid)
print(total_rolls)
