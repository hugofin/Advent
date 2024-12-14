with open('day04.txt') as file:
    data = file.readlines()

def check_horizontal(x, y):
    out = 0
    if grid[y][x:x+4] == 'XMAS': out += 1    
    if grid[y][x-4:x] == 'SAMX': out += 1
        
    return out

def check_vertical(x, y):
    out = 0
    down = grid[y][x] + grid[y+1][x] + grid[y+2][x] + grid[y+3][x]
    up   = grid[y][x] + grid[y-1][x] + grid[y-2][x] + grid[y-3][x]

    for opt in [down, up]:
        if opt == 'XMAS': out += 1

    return out
    
def check_diagonal(x, y):
    out = 0
    lup = grid[y][x] + grid[y-1][x-1] + grid[y-2][x-2] + grid[y-3][x-3]
    ldn = grid[y][x] + grid[y+1][x-1] + grid[y+2][x-2] + grid[y+3][x-3]
    rup = grid[y][x] + grid[y-1][x+1] + grid[y-2][x+2] + grid[y-3][x+3]
    rdn = grid[y][x] + grid[y+1][x+1] + grid[y+2][x+2] + grid[y+3][x+3]

    for opt in [lup, ldn, rup, rdn]:
        if opt == 'XMAS': out += 1

    return out

def check_xmas(x, y):
    tl, tr = grid[y-1][x-1], grid[y-1][x+1]
    mi     = grid[y][x]
    bl, br = grid[y+1][x-1], grid[y+1][x+1]

    if mi == 'A':
        match (tl, tr, bl, br):
            case ('M', 'M', 'S', 'S'):  # M M
                return 1                #  A
                                        # S S

            case ('S', 'M', 'S', 'M'):  # S M
                return 1                #  A
                                        # S M

            case ('S', 'S', 'M', 'M'):  # S S
                return 1                #  A
                                        # M M

            case ('M', 'S', 'M', 'S'):  # M S
                return 1                #  A
                                        # M S
    return 0

padding = []
for i in range(3):
    tmp = ''
    for j in range(146):
        tmp += ' '
    padding.append(tmp)

grid = []

for i in data:
    i = i.strip('\n')
    i = '   ' + i + '   '
    grid.append(i)

grid = padding + grid + padding

total_1, total_2 = 0, 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] != ' ':
            total_1 += check_horizontal(x, y) + check_vertical(x, y) + check_diagonal(x, y)
            total_2 += check_xmas(x, y)

print(total_1, total_2)