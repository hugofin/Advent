with open('day06data.txt') as file:
    data = file.read()

for i in range(len(data) - 14):
    last_four = data[i : i + 14]

    if len(set(last_four)) == len(last_four):
        print(i + 14)
