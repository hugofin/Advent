from functools import cache


def to_tuples(x):
    return tuple(x.strip('()').split(','))

def flip(lights, switch):
    new_lights = list(lights)

    for space in switch:
        y = int(space) + 1

        x = lights[y]

        if x == '.':
            new_lights[y] = '#'
        else:
            new_lights[y] = '.'
    return ''.join(new_lights)

def get_combiations(xs):
    if len(xs) == 0:
        return [[]]
    result = []

    for x in get_combiations(xs[1:]):
        result += [x, x + [xs[0]]]
    return result

def all_off(lights):
    return set(lights[1:-1]) == set('.')

@cache
def part_one(lights, switches):
    combinations = get_combiations(switches)
    combinations.sort(key=len)

    valid = []

    for combination in combinations:

        lights_option = lights

        for switch in combination:
            lights_option = flip(lights_option, switch)

        if all_off(lights_option):
            valid.append(combination)

    return valid

@cache
def part_two(switches, joltage):

    if any(x < 0 for x in joltage):
        return 999999999

    if sum(joltage) == 0:
        return 0

    lights = '['

    for light in joltage:
        if light % 2 == 1:
            lights += '#'
        else:
            lights += '.'

    lights += ']'

    valid_combinations = part_one(lights, switches)

    min_val = 99999999

    for combination in valid_combinations:
        new_joltage = list(joltage)

        for button in combination:
            for light in button:
                new_joltage[int(light)] -= 1

        for i, jolt in enumerate(new_joltage):
            new_joltage[i] = jolt // 2

        presses = len(combination) + 2 * part_two(switches, tuple(new_joltage))
        min_val = min(min_val, presses)

    return min_val

total_presses = 0

for line in open("10.txt"):
    sections = line.split()
    lights = sections[0]
    switches = tuple(map(to_tuples, sections[1:-1]))
    target_joltage = tuple(map(int, sections[-1][1:-1].split(',')))

    # total_presses += min([len(x) for x in part_one(lights, switches)])
    total_presses += part_two(switches, target_joltage)

print(total_presses)
