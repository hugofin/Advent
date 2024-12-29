import itertools
with open('day08.txt') as file:
    data = file.readlines()

def write_map(map):
    total = 0
    for line in map:
        print(''.join(line))
        for character in line:
            if character != '.':
                total += 1
    print(total)

map, aerials = [], []

for y, line in enumerate(data):
    row = []
    for x, character in enumerate(line[:-1]):
        row.append(character)
        if character != '.':
            aerials.append((character, y, x))
    map.append(row)

for [(one_f, one_y, one_x), (two_f, two_y, two_x)] in itertools.combinations(aerials, r = 2):

    if (one_f, one_y, one_x) != (two_f, two_y, two_x) and one_f == two_f:
        diff_y = abs(one_y - two_y)
        diff_x = abs(one_x - two_x)

        if one_x < two_x:
            next_y, next_x = one_y - diff_y, one_x - diff_x

            while next_y >= 0 and next_x >= 0:
                map[next_y][next_x] = '#'
                next_y, next_x = next_y - diff_y, next_x - diff_x

            next_y, next_x = two_y + diff_y, two_x + diff_x

            while next_y <= len(map) - 1 and next_x <= len(map[0]) - 1:
                map[next_y][next_x] = '#'
                next_y, next_x = next_y + diff_y, next_x + diff_x

        else:
            next_y, next_x = one_y - diff_y, one_x + diff_x

            while next_y >= 0 and next_x <= len(map[0]) - 1:
                map[next_y][next_x] = '#'
                next_y, next_x = next_y - diff_y, next_x + diff_x

            next_y, next_x = two_y + diff_y, two_x - diff_x

            while next_y <= len(map) - 1 and next_x >= 0:
                map[next_y][next_x] = '#'
                next_y, next_x = next_y + diff_y, next_x - diff_x

write_map(map)
