with open('day03.txt') as file:
    data = file.read().strip('\n')

on_mul = data.split('mul(')

def all_ints(string):
    return all(char.isdigit() for char in string)

total_1, total_2 = 0, 0

for i in on_mul:
    sections = i.split(')')[0]
    ints = sections.split(',')

    if len(ints) == 2 and (all_ints(ints[0]) and all_ints(ints[1])):
        total_1 += (int(ints[0]) * int(ints[1]))

on_do = data.split('do()')
for i in on_do:
    block = i.split('don\'t()')[0]

    block_mul = block.split('mul(')
    
    for i in block_mul:
        sections = i.split(')')[0]
        ints = sections.split(',')

        if len(ints) == 2 and (all_ints(ints[0]) and all_ints(ints[1])):
            total_2 += (int(ints[0]) * int(ints[1]))

print(total_1, total_2)            
