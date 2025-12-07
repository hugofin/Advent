dial, total = 50, 0

for instruction in open("01.txt"):
    direction = instruction[0]
    gross_magnitude = int(instruction[1:])
    new_dial = dial

    total += gross_magnitude // 100
    fine_magnitude = gross_magnitude % 100

    if direction == 'L':
        new_dial = dial + fine_magnitude
    else:
        new_dial = dial - fine_magnitude

    if (dial != 0):
        if (new_dial <= 0 or new_dial >= 100):
            total += 1

    dial = new_dial % 100

print(total)
