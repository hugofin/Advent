with open('day06.txt') as file:
    data = file.readlines()

patrol = []

for line in data:
    add = []
    for char in line:
        add.append(char)

    patrol.append(add)

total_1, total_2 = 1, 0
y, x = 0, 0

for i in range(len(patrol) - 1):
    for j in range(len(patrol[0]) - 1):
        if data[j][i] == '^':
            y, x = j, i

next_y, next_x = y - 1, x

while next_x < 130 and next_y < 130 and next_x > -1 and next_y > -1:
    match patrol[y][x]:
        case '^':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = '>'
                next_y += 1
                next_x += 1
            elif patrol[next_y][next_x] == '-':
                patrol[y][x] = '+'
                patrol[next_y][next_x] = '^'
                y = next_y
                next_y -= 1
            else:
                patrol[y][x] = '|'
                patrol[next_y][next_x] = '^'
                y = next_y
                next_y -= 1

        case '>':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = 'v'
                next_y += 1
                next_x -= 1
            elif patrol[next_y][next_x] == '|':
                patrol[y][x] = '+'
                patrol[next_y][next_x] = '>'
                x = next_x
                next_x += 1
            else:
                patrol[y][x] = '-'
                patrol[next_y][next_x] = '>'
                x = next_x
                next_x += 1

        case 'v':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = '<'
                next_y -= 1
                next_x -= 1
            elif patrol[next_y][next_x] == '-':
                patrol[y][x] = '+'
                patrol[next_y][next_x] = 'v'
                y = next_y
                next_y += 1
            else:
                patrol[y][x] = '|'
                patrol[next_y][next_x] = 'v'
                y = next_y
                next_y += 1

        case '<':
            if patrol[next_y][next_x] == '#':
                patrol[y][x] = '^'
                next_y -= 1
                next_x += 1
            elif patrol[next_y][next_x] == '|':
                patrol[y][x] = '+'
                patrol[next_y][next_x] = '<'
                x = next_x
                next_x -= 1
            else:
                patrol[y][x] = '-'
                patrol[next_y][next_x] = '<'
                x = next_x
                next_x -= 1

for line in patrol:
    for character in line:
        if character == '-' or character == '|' or character == '+':
            total_1 += 1



print(total_1, total_2)
