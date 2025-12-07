grid = {}
for y, line in enumerate(open("04.txt")):
    for x, space in enumerate(line.strip()):
        if space == '@':
            grid.update({(y,x): space})

def check(grid):
    new_grid, total = {}, 0
    keys = grid.keys()

    for spot in keys:
        y, x = spot
        adjacent_rolls = 0

        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if (y-i, x-j) in keys:
                    adjacent_rolls += 1

        if adjacent_rolls <= 4:
            total += 1
        else:
            new_grid.update({spot: '@'})

    return new_grid, total

total_rolls, retrived_rolls = 0, -1

while retrived_rolls != 0:
    grid, retrived_rolls = check(grid)
    total_rolls += retrived_rolls

print(total_rolls)
