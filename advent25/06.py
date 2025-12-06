x = open("06.txt").readlines()

sums, sum = [], []

for i, operation in enumerate(x[-1]):
    if operation != ' ':
        sums.append(sum)
        sum = [operation]

    num = ''

    for line in x[:-1]:
        num += line[i]

    if num.strip() != "":
        sum.append(num)

    if i == len(x[-1]) - 1:
        sums.append(sum)

total = 0
for sum in sums[1:]:
    if sum[0] == '*':
        accumulator = 1
        for value in sum[1:]:
            accumulator *= int(value)

        total += accumulator

    else:
        accumulator = 0
        for value in sum[1:]:
            accumulator += int(value)

        total += accumulator

print(total)
