with open('day02.txt') as file:
    data = file.read().split('\n')

output = 0

for line in data:
    halves = line.split(':')
    print(halves[0])
    games  = halves[1].split(';')
    
    red   = 0
    green = 0
    blue  = 0

    for game in games:
        draws = game.split(',')
        for draw in draws:
            a = draw.split(' ')
            if a[2] == 'red' and int(a[1]) > red:
                red = int(a[1])
            elif a[2] == 'green' and int(a[1]) > green:
                green = int(a[1])
            elif a[2] == 'blue' and int(a[1]) > blue:
                blue = int(a[1])

    output += (red * green * blue)
    print(f'{red}, {green}, {blue}')
    print(output)

    print ('_______________\n')        

print(output)