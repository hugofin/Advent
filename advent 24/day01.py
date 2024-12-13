with open('day01.txt') as file:
    data = file.read().split('\n')

fst = []
snd = []

for line in data:
    halves = line.split('   ')
    fst.append(int(halves[0]))
    snd.append(int(halves[1]))

fst.sort()
snd.sort()

acc = 0

for i in range(len(fst)):
    if fst[i] >= snd[i]:
        acc += (fst[i] - snd[i])
    else:
        acc += (snd[i] - fst[i])

print(acc)
acc = 0

dct = {}

for i in range(len(fst)):
    if fst[i] not in dct:
        dct.update({fst[i]: 0})

for i in range(len(snd)):
    if snd[i] in dct:
        dct.update({snd[i]: dct[snd[i]] + 1})

for i in range(len(fst)):
    acc += fst[i] * dct[fst[i]]

print(dct)