max_x = 0
max_y = 0
matrix = dict()
instructions = list()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if ',' in line:
            x, y = [int(i) for i in line.split(',')]
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            matrix.setdefault((x, y), True)
        if '=' in line:
            a = line.split()
            axis, value = a[-1].split('=')
            instructions.append((axis, int(value)))

def print_matrix():
    for y in range(max_y + 1):
        row = ''
        for x in range(max_x+ 1):
            if matrix.get((x,y), False):
                row += '#'
            else:
                row += '.'
        print(row)

print_matrix()
for i, instruction in enumerate(instructions):
    if i > 0:
        break
    axis, value = instruction
    print()
    print(axis, '=', value)

    # fold bottom over top
    if axis == 'y':
        for z, y in enumerate(range(value + 1, max_y + 1)):
            for x in range(max_x + 1):
                if matrix.get((x,y), False):
                    del matrix[(x,y)]
                    yy = value - (z + 1)
                    matrix.setdefault((x, yy), True)
        max_y = value - 1

    # fold right over left
    if axis == 'x':
        for y in range(max_y + 1):
            for z, x in enumerate(range(value + 1, max_x + 1)):
                if matrix.get((x,y), False):
                    del matrix[(x,y)]
                    xx = value - (z + 1)
                    matrix.setdefault((xx, y), True)
        max_x = value - 1

    print_matrix()
    print(len(matrix))