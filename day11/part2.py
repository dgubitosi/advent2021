
matrix = list()
with open('input.txt') as f:
    for line in f:
        matrix.append([int(c) for c in line.strip()])

def find_neighbors(y0, x0):
    neighbors = list()
    for dy in [-1, 0, 1]:
        y = y0 + dy
        if y < 0 or y >= len(matrix):
            continue
        for dx in [-1, 0, 1]:
            x = x0 + dx
            if x < 0 or x >= len(matrix[y]):
                continue
            if matrix[y][x] is not None:
                neighbors.append((y, x))
    return neighbors

def print_matrix():
    for row in matrix:
        print(''.join(map(str, row)))

flashes = 0
i = 0
while True:
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] is None:
                continue
            matrix[y][x] += 1
            if matrix[y][x] > 9:
                matrix[y][x] = None
                flashes += 1
                neighbors = list()
                neighbors.extend(find_neighbors(y, x))
                while neighbors:
                    yy, xx = neighbors.pop()
                    if matrix[yy][xx] is None:
                        continue
                    matrix[yy][xx] += 1
                    if matrix[yy][xx] > 9:
                        matrix[yy][xx] = None
                        flashes += 1
                        neighbors.extend(find_neighbors(yy, xx))

    total = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            if matrix[y][x] is None:
                matrix[y][x] = 0
            total += matrix[y][x]

    print_matrix()
    print(i+1, flashes)
    print()

    if total == 0:
        break

    i += 1
