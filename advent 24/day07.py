with open('day07.txt') as file:
    data = file.readlines()

total = 0

def concat(a, b):
    c = str(a) + str(b)
    return int(c)

def check(target, acc, xs):
    if len(xs) == 0:
        if acc == target:
            return True
        else:
            return False
    else:
        return (check(target, acc + xs[0], xs[1:]) or check(target, acc * xs[0], xs[1:]) or check(target, concat(acc, xs[0]), xs[1:]))

for line in data:
    [target, values] = line.split(':')

    target = int(target)
    values = [int(x) for x in values.split()]

    if check(target, values[0], values[1:]):
        total += target

print(total)
