from functools import cache

connections = {}

for line in open("11.txt"):
    xs = line.strip().split(':')

    connected_nodes = tuple(xs[1].strip().split())
    connections[xs[0]] = connected_nodes

@cache
def traverse(start, fft, dac):
    if start == "out":
        if (fft and dac):
            return 1
        else:
            return 0
    elif start == 'fft':
        return sum([traverse(x, True, dac) for x in connections[start]])
    elif start == 'dac':
        return sum([traverse(x, fft, True) for x in connections[start]])
    else:
        return sum([traverse(x, fft, dac) for x in connections[start]])

print(traverse('svr', False, False))
