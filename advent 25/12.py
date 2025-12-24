x = open("12.txt").read().split('\n\n')

regions = x[-1].split('\n')

shapes = []

for l in x[:-1]:
    t = 0
    shape = l.split('\n')
    for line in shape[1:]:
        for char in line:
            if char == '#':
                t += 1

    shapes.append(t)

total = 0

for region in regions:

    xs = region.split(' ')

    dimensions = xs[0].rstrip(':').split('x')

    area = int(dimensions[0]) * int(dimensions[1])

    worst_size, perfect_size = 0, 0

    for i, count in enumerate(xs[1:]):
        worst_size += 9 * int(count)
        perfect_size += shapes[i] * int(count)

    if worst_size <= area or area >= perfect_size:
        total += 1

print(total)
