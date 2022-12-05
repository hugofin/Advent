data = open("day03data.txt")

rucksacks = []
for rucksack in data:
    rucksacks.append(rucksack.strip('\n'))

total = 0

for rucksack in rucksacks:
    compartments = ['', '']

    middle = int((len(rucksack) - 1) / 2)

    compartments[0] = ''.join(set(rucksack[:middle]))
    compartments[1] = ''.join(set(rucksack[middle:]))

    print(f'splitting {rucksack}')
    print(f'comparing {compartments[0]} and {compartments[1]}')

    for item in compartments[0]:
        if item in(compartments[1]):
            if ord(item) > 96:
                total += ord(item) - 96
                print(f'adding {item} as {ord(item) - 96}')
            else:
                total += ord(item) - 38
                print(f'adding {item} as {ord(item) - 38}')

print(total)

total = 0

for group in range(int(len(rucksacks) / 3)):

    member_1 = ''.join(set(rucksacks[(group * 3)]))
    member_2 = ''.join(set(rucksacks[(group * 3) + 1]))
    member_3 = ''.join(set(rucksacks[(group * 3) + 2]))

    print(f'comparing {member_1}, {member_2} and {member_3}')

    for item in member_1:
        if item in member_2 and item in member_3:
            print(f'the common character is {item}')
            if ord(item) > 96:
                total += ord(item) - 96
            else:
                total += ord(item) - 38

print(total)
