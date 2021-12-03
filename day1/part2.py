
with open('input.txt') as f:
    measurements = f.readlines()

c = 0
i = 3
n = len(measurements)
while i < n:
    x = sum([int(i) for i in measurements[i-2:i+1]])
    y = sum([int(i) for i in measurements[i-3:i]])
    if x > y:
        c += 1
    i += 1
print(c)
