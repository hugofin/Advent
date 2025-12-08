import math

junctions = []
for line in open("08.txt"):
    coordinates = line.strip().split(',')
    junctions.append([(int(coordinates[0]), int(coordinates[1]), int(coordinates[2]))])

def get_distance(first, second):
    return math.sqrt(abs(second[0] - first[0])**2 + abs(second[1] - first[1])**2 +  abs(second[2] - first[2])**2)

closest = []
while len(junctions) != 1:
    min_distance = 100000000

    for i, group_1 in enumerate(junctions):
        for j, group_2 in enumerate(junctions):
            if i != j:
                for x, junct_1 in enumerate(group_1):
                    for y, junct_2 in enumerate(group_2):
                        distance = get_distance(junct_1, junct_2)

                        if distance <= min_distance:
                            min_distance = distance
                            closest = [i,j, junct_1, junct_2]

    a, b, j1, j2 = closest

    junctions[a] = junctions[a] + junctions[b]
    junctions = junctions[:b] + junctions[b + 1:]

print(closest[2][0] * closest[3][0])