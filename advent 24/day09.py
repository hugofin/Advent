with open('day09.txt') as file:
    data = file.read()

disc, i = [], 0

while data[i] != '\n':
    if i % 2 == 0:
        disc += [str(i//2) for x in range(int(data[i]))]
    else:
        disc += list('.' * int(data[i]))
    i += 1

# print(''.join(disc))
disc = disc[::-1]

def next_blank(list):
    for i, char in enumerate(list[::-1]):
        if char == '.':
            return len(list) - i - 1
    return 0

for i, char in enumerate(disc):
        if char != '.':
            target = next_blank(disc)
            disc[target] = char
            disc[i] = '.'
            # print(''.join(disc), i, target)
            if '.' not in disc[i + 1:target]:
                break

disc = disc[::-1]
total, i = 0, 0

while disc[i] != '.':
    total += int(disc[i]) * i
    i += 1

print(total)
