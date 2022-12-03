data = open("day01data.txt")

elf_snacks = []
total = 0

for snack in data:
    print(snack)
    if snack == '\n':
        elf_snacks.append(total)
        total = 0
    else:
        total += int(snack)

elf_snacks.sort(reverse = True)

print(elf_snacks[0])

print(sum(elf_snacks[:3]))
