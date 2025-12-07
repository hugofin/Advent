x = open("05.txt").read().split('\n\n')

def collapse(listOf):
    new_ranges = []
    for start, stop in listOf:
        added = False

        for i, (lower, upper) in enumerate(new_ranges):
            if start <= upper and start > lower and stop > upper:       # lower--start/upper--stop
                new_ranges[i] = (lower, stop)
                added = True
                break
            elif start < lower and stop <= upper and stop >= lower:     # start--lower/stop--upper
                new_ranges[i] = (start, upper)
                added = True
                break
            elif start <= lower and stop >= upper:                      # start/lower---upper/stop
                new_ranges[i] = (start, stop)
                added = True
                break
            elif start >= lower and stop <= upper:                      # lower-start---stop-upper
                added = True
                break

        if (not added):                                                 # lower-upper---start-stop
            new_ranges.append((start, stop))                            # start-stop---lower-upper
    return new_ranges

fresh_ranges = []
for range in x[0].split('\n'):
    ids = range.split('-')
    fresh_ranges.append((int(ids[0]), int(ids[1])))

old_ranges = []
while len(old_ranges) != len(fresh_ranges):
    old_ranges = fresh_ranges
    fresh_ranges = collapse(fresh_ranges)

total = 0
for lower_boundary, upper_boundary in old_ranges:
    total += (upper_boundary - lower_boundary) + 1

print(total)
