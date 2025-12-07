total = 0

def compare(length, size, number):
    first = number[:size]
    for i in range(1, length // size):
        if first != number[i * size: (i + 1) * size]:
            return False
    return True

for product_range in open("02.txt").readlines()[0].split(','):
    product_segments = product_range.split('-')
    lower = int(product_segments[0])
    upper = int(product_segments[1])

    while(lower <= upper):
        lower_string = str(lower)
        length = len(lower_string)

        for size in range(1, (length // 2) + 1):
            if length % size == 0:
                if compare(length, size, lower_string):
                    total += lower
                    break
        lower += 1

print(total)
