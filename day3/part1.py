
n = 0
array = [0] * len('000011000110')
with open('input.txt') as f:
    for line in f:
        n += 1
        line = line.strip()
        for i, b in enumerate(line):
            array[i] += int(b)

print(n, array)
gamma = [0] * len('000011000110')
epsilon = [1] * len('000011000110')
for p, i in enumerate(array):
    j = n - i
    if i > j:
        gamma[p] = 1
        epsilon[p] = 0

print(gamma)
print(epsilon)

g = int(''.join(str(i) for i in gamma), 2)
e = int(''.join(str(i) for i in epsilon), 2)
print(g * e)


