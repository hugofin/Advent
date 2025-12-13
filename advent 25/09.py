tiles = set()
for line in open("09.txt"):
    x = line.strip().split(',')
    tiles.add((int(x[0]), int(x[1])))

print(tiles)

max_area = 0

for a in tiles:
    for b in tiles:

        print(a, b)

        height = abs(a[0] - b[0]) + 1
        width = abs(a[1] - b[1]) + 1

        area = width * height

        print(area)
        
        if (a[0], b[1]) in tiles or (b[0], a[1]) in tiles:
            if area >= max_area:
                max_area = area

        print('___________________')

print(max_area)
