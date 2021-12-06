
lanternfish = list()
with open('input.txt') as f:
    for line in f:
        lanternfish = [int(i) for i in line.strip().split(',')]

for i in range(80):
    new_fish = 0
    for j in range(len(lanternfish)):
        lanternfish[j] -= 1
        if lanternfish[j] < 0:
            lanternfish[j] = 6
            new_fish += 1
    lanternfish.extend([8]*new_fish)
    print(i+1, len(lanternfish))
