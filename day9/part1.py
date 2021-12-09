
matrix = list()
with open("input.txt") as f:
    for line in f:
        matrix.append(line.strip())

low_points = list()
risk = 0
for y in range(len(matrix)):
    for x in range(len(matrix[y])):
        pos = (x, y)
        height = int(matrix[y][x])

        # adjacent points
        lowest = True
        adjacent = dict()

        # find adjacent y points
        for dy in [ 1, -1 ]:
            adj_y = y + dy
            # skip out of bounds
            if adj_y < 0 or adj_y >= len(matrix):
                continue
            h = int(matrix[adj_y][x])
            # not lower
            if height >= h:
                lowest = False
                break
            # add point to adjacent points
            else:
                adjacent.setdefault((x, adj_y), h)

        if not lowest:
            continue

        # find adjacent x points
        for dx in [ 1, -1 ]:
            adj_x = x + dx
            # skip of out bounds
            if adj_x < 0 or adj_x >= len(matrix[y]):
                continue
            h = int(matrix[y][adj_x])
            # not lower
            if height >= h:
                lowest = False
                break
            else:
                adjacent.setdefault((x, adj_y), h)

        if not lowest:
            continue

        low_points.append((pos, height))
        risk += height + 1
        print('pos', pos, height)
        for a in adjacent:
            print('  adj', a, adjacent[a])

print('risk', risk)