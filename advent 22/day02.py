opened = open("day02data.txt")

total = 0

for item in opened:
    enemy = item[0]
    reaction = item[2]

    if enemy == 'A':
        if reaction == 'X':
            total += (0 + 3)
        elif reaction == 'Y':
            total += (3 + 1)
        else:
            total += (6 + 2)
    elif enemy == 'B':
        if reaction == 'X':
            total += (0 + 1)
        elif reaction == 'Y':
            total += (3 + 2)
        else:
            total += (6 + 3)
    else:
        if reaction == 'X':
            total += (0 + 2)
        elif reaction == 'Y':
            total += (3 + 3)
        else:
            total += (6 + 1)

print(total)
