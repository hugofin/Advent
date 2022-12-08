with open('day05data.txt') as file:
    data = file.read().split('\n')

stacks = { 1 : [], 2 : [], 3 : [], 4 : [],5 : [], 6 : [], 7 : [], 8 : [], 9 : []}

for row in range(9):
    current_line = data[row]

    for i in range(9):
        if (current_line[1 + 4 * i] != ' '):
            temp = stacks[i + 1]
            temp.append(current_line[1 + 4 * i])
            stacks.update({i + 1 : temp})

for row in data[10:512]:

    instructions = row.split(' ')

    amount = int(instructions[1])
    start = int(instructions[3])
    destination = int(instructions[5])

    taking_from = stacks[start]
    cargo = taking_from[:amount]
    took_from = taking_from[amount:]

    # cargo.reverse()
    # add in cargo.reverse to complete part one

    cargo.extend(stacks[destination])

    stacks.update({start : took_from})
    stacks.update({destination : cargo})

answer = ''
for i in range(1,10):
    answer += stacks[i][0]

print(answer)
