def select(slice):
    max, max_i = '0', 0

    for i, number in enumerate(slice):
        if number > max:
            max, max_i = number, i

    return max, (max_i + 1)

total_joltage = 0

for battery in open("03.txt"):
    battery = battery.strip()

    joltage = ""
    search_index = 0

    for i in range(1, 13):
        cell, cell_index = select(battery[search_index : len(battery)-(12 - i)])
        joltage += cell
        search_index += cell_index

    total_joltage += int(joltage)

print(total_joltage)
