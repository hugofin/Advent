with open('day02.txt') as file:
    data = file.read().split('\n')

def ok_up(a):
    for i in a:
        if not (i > 0 and i < 4):
            return 0       
    return 1

def ok_down(a):
    for i in a:
        if not (i < 0 and i > -4):
            return 0        
    return 1

total_1, total_2 = 0, 0

for line in data:
    levels = line.split(' ')
    as_numbers = list(map(int, levels))

    changes = []

    for i in range(len(as_numbers) - 1):
        changes.append(as_numbers[i] - as_numbers[i+1])    
                
    is_up = ok_up(changes)
    is_down = ok_down(changes)

    total_1 += is_up + is_down
    total_2 += is_up + is_down

    if is_up + is_down == 0:

        solved = False

        for i in range(len(as_numbers)):
            if solved == False:
                copy = as_numbers.copy()
                del copy[i]
                changes_copy = []

                for i in range(len(copy) - 1):
                    changes_copy.append(copy[i] - copy[i+1])    

                if ok_up(changes_copy) == 1:
                    total_2 += 1
                    solved = True

                elif ok_down(changes_copy) == 1:
                    total_2 += 1
                    solved = True

print(total_1, total_2)