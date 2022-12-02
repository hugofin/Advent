opened = open("01data.txt")

elf_snacks = []
total = 0

for item in opened:
    snack = item.split("\n\n")
    if snack[0] == '\n':
        elf_snacks.append(total)
        total = 0
    else:
        total += int(snack[0])

elf_snacks.sort(reverse = True)

print(elf_snacks[0])

print(sum(elf_snacks[:3]))
