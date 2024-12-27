import copy
with open('day06.txt') as file:
    data = file.readlines()

patrol = []

for line in data:
    add = []
    for char in line:
        add.append(char)
    patrol.append(add)

patrol_blocks = copy.deepcopy(patrol)

total_1, total_2 = 1, 0
y, x = 0, 0

for i in range(len(patrol) - 1):
    for j in range(len(patrol[0]) - 1):
        if data[j][i] == '^':
            y, x = j, i

next_y, next_x = y - 1, x

while next_x < len(patrol) and next_y < len(patrol) and next_x > -1 and next_y > -1:
    match patrol[y][x]:
        case '^':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = '>'
                next_y += 1
                next_x += 1
            else:
                patrol[y][x] = 'X'
                patrol[next_y][next_x] = '^'
                y = next_y
                next_y -= 1

        case '>':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = 'v'
                next_y += 1
                next_x -= 1
            else:
                patrol[y][x] = 'X'
                patrol[next_y][next_x] = '>'
                x = next_x
                next_x += 1

        case 'v':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = '<'
                next_y -= 1
                next_x -= 1
            else:
                patrol[y][x] = 'X'
                patrol[next_y][next_x] = 'v'
                y = next_y
                next_y += 1

        case '<':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = '^'
                next_y -= 1
                next_x += 1
            else:
                patrol[y][x] = 'X'
                patrol[next_y][next_x] = '<'
                x = next_x
                next_x -= 1

for line in patrol:
    for character in line:
        if character == 'X':
            total_1 += 1

def is_loop(patrol_loop, x, y, next_x, next_y):
    visited = set()

    while next_x < len(patrol_loop) and next_y < len(patrol_loop) and next_x > -1 and next_y > -1:
        location = (x, y, patrol_loop[y][x])

        if location in visited:
            return 1

        visited.add(location)

        match patrol_loop[y][x]:
            case '^':
                if patrol_loop[next_y][next_x] == '#':
                    patrol_loop[y][x] = '>'
                    next_y += 1
                    next_x += 1
                else:
                    patrol_loop[y][x] = 'X'
                    patrol_loop[next_y][next_x] = '^'
                    y = next_y
                    next_y -= 1

            case '>':
                if patrol_loop[next_y][next_x] == '#':
                    patrol_loop[y][x] = 'v'
                    next_y += 1
                    next_x -= 1
                else:
                    patrol_loop[y][x] = 'X'
                    patrol_loop[next_y][next_x] = '>'
                    x = next_x
                    next_x += 1

            case 'v':
                if patrol_loop[next_y][next_x] == '#':
                    patrol_loop[y][x] = '<'
                    next_y -= 1
                    next_x -= 1
                else:
                    patrol_loop[y][x] = 'X'
                    patrol_loop[next_y][next_x] = 'v'
                    y = next_y
                    next_y += 1

            case '<':
                if patrol_loop[next_y][next_x] == '#':
                    patrol_loop[y][x] = '^'
                    next_y -= 1
                    next_x += 1
                else:
                    patrol_loop[y][x] = 'X'
                    patrol_loop[next_y][next_x] = '<'
                    x = next_x
                    next_x -= 1
    return 0

start_y, start_x = 0, 0

for i in range(len(patrol_blocks) - 1):
    for j in range(len(patrol_blocks[0]) - 1):
        if data[j][i] == '^':
            start_y, start_x = j, i

for i in range(len(patrol)):
    for j in range(len(patrol)):
        if patrol_blocks[i][j] == '.':

            patrol_blocks_temp = copy.deepcopy(patrol_blocks)
            patrol_blocks_temp[i][j] = '#'

            next_y, next_x = start_y - 1, start_x

            total_2 += is_loop(patrol_blocks_temp, start_x, start_y, next_x, next_y)

print(total_1, total_2)
