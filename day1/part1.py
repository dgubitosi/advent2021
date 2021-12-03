
with open('input.txt') as f:
    measurements = f.readlines()

c = 0
i = 1
n = len(measurements)
while i < n:
    if int(measurements[i]) > int(measurements[i-1]):
        c += 1
    i += 1
print(c)
