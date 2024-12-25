with open('day02.txt') as file:
    data = file.read().split('\n')

def ok_up(a):
    return all(i > 0 and i < 4 for i in a)

def ok_down(a):
    return all(i < 0 and i > -4 for i in a)

def get_changes(xs):
    changes = []
    for (a, b) in zip(xs, xs[1:]):
        changes.append(a - b)    
    return changes

total_1, total_2 = 0, 0

for line in data:
    levels = line.split(' ')
    as_numbers = list(map(int, levels))

    changes = get_changes(as_numbers)
                
    if ok_up(changes) or ok_down(changes):
        total_1 += 1

    solved = False

    for i in range(len(as_numbers)):
        if solved == False:
            copy = as_numbers.copy()
            del copy[i]
            changes_copy = get_changes(copy)

            if ok_up(changes_copy) or ok_down(changes_copy):
                total_2 += 1
                solved = True

print(total_1, total_2)