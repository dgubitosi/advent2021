
lanternfish = [0]*9
with open('input.txt') as f:
    for line in f:
        fish = [int(i) for i in line.strip().split(',')]
        for i in range(len(lanternfish)):
            lanternfish[i] = fish.count(i)
print(lanternfish)

for i in range(256):
    new_fish = lanternfish.pop(0)
    lanternfish[6] += new_fish
    lanternfish.append(new_fish)
    print(i+1, sum(lanternfish), lanternfish)
