grid = []
for line in open("07.txt"):
    row = []
    for space in line.strip():
        if space == '.':
            row.append(0)
        else:
            row.append(space)
    grid.append(row)

splits, total_beams = 0, 0

for j, line in enumerate(grid):
    for i, char in enumerate(line):
        if grid[j][i] == 'S':
            grid[j+1][i] = 1
        elif char == '^' and grid[j-1][i] > 0:
            grid[j][i-1] += grid[j-1][i]
            grid[j][i+1] += grid[j-1][i]
            splits += 1
        elif type(grid[j-1][i]) is int and grid[j-1][i] > 0:
            grid[j][i] += grid[j-1][i]

for char in grid[-1]:
    if type(char) is int:
        total_beams += char

print(splits, total_beams)
