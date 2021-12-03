
h = 0
d = 0

with open('input.txt') as f:
    for line in f:
        instruction, value = line.split(' ', 2)
        if instruction == 'forward':
            h += int(value)
        elif instruction == 'down':
            d += int(value)
        elif instruction == 'up':
            d -= int(value)

print(h*d)