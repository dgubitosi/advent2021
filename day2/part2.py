
h = 0
d = 0
a = 0

with open('input.txt') as f:
    for line in f:
        instruction, value = line.split(' ', 2)
        if instruction == 'forward':
            h += int(value)
            d += a*int(value)
        elif instruction == 'down':
            a += int(value)
        elif instruction == 'up':
            a -= int(value)

print(h*d)