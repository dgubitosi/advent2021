
max_p = 0
positions = dict()
with open('input.txt') as f:
    for line in f:
        for i in line.strip().split(','):
            i = int(i)
            max_p = max(max_p, i)
            positions.setdefault(i, 0)
            positions[i] += 1

pos = 0
fuel = -1
for target_p in range(max_p):
    f = 0
    for p in positions:
        d = abs(target_p - p)
        f += d * positions[p]
    if fuel < 0 or f < fuel:
        fuel = f
        pos = target_p

print(pos, fuel)
