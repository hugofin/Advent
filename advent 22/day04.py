data = open("day04data.txt")

pairs = []
for pair in data:

    intermediate = pair.strip('\n').split(',')
    intermediate[0] = intermediate[0].split('-')
    intermediate[1] = intermediate[1].split('-')

    pairs.append(intermediate)

total = 0

for pair in pairs:
    if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
        total += 1

    elif (int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][1])):
        total += 1

print(total)
total = 0

for pair in pairs:

    if int(pair[0][0]) <= int(pair[1][0]) and int(pair[0][1]) >= int(pair[1][1]):
        total += 1

    elif (int(pair[1][0]) <= int(pair[0][0]) and int(pair[1][1]) >= int(pair[0][1])):
        total += 1

    elif int(pair[0][1]) >= int(pair[1][0]) and int(pair[0][1]) <= int(pair[1][1]):
        total += 1

    elif (int(pair[0][0]) >= int(pair[1][0]) and int(pair[0][0]) <= int(pair[1][1])):
        total += 1

print(total)
