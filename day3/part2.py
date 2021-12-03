
def rating(measurements):
    a = [0] * len(measurements[0])
    g = [0] * len(measurements[0])
    for n, m in enumerate(measurements):
        for i, b in enumerate(m):
            a[i] += int(b)
            if a[i] >= n + 1 - a[i]:
                g[i] = 1
            else:
                g[i] = 0
        print(n, g, a)
    return ''.join([str(i) for i in g])

measurements = list()
with open('input.txt') as f:
    for line in f:
        measurements.append(line.strip())

o = rating(measurements)
print(o)
