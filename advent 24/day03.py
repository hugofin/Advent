with open('day03.txt') as file:
    data = file.read().strip('\n')

on_mul = data.split('mul(')
allowed_chars = ['1','2','3','4','5','6','7','8','9','0']

def all_ints(string):
    for char in string:
        if char not in allowed_chars:
            return False
        
    return True

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
