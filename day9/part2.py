
matrix = list()
with open("input.txt") as f:
    for line in f:
        matrix.append(line.strip())

basins = list()
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

        basin = set()
        basin.add(pos)

        visited = set()
        to_visit = set()
        to_visit.add(pos)
        while to_visit:
            p = to_visit.pop()
            if p in visited:
                continue
            visited.add(p)

            px = p[0]
            py = p[1]
            for dy in [ 1, -1 ]:
                adj_y = py + dy
                while adj_y >= 0 and adj_y < len(matrix):
                    h = int(matrix[adj_y][px])
                    # not in basin
                    if h == 9:
                        break
                    else:
                        adj_p = (px, adj_y)
                        basin.add(adj_p)
                        if adj_p not in visited:
                            to_visit.add(adj_p)
                        adj_y += dy

            for dx in [ 1, -1 ]:
                adj_x = px + dx
                while adj_x >= 0 and adj_x < len(matrix[py]):
                    h = int(matrix[py][adj_x])
                    # not in basin
                    if h == 9:
                        break
                    else:
                        adj_p = (adj_x, py)
                        basin.add(adj_p)
                        if adj_p not in visited:
                            to_visit.add(adj_p)
                        adj_x += dx

        basins.append(len(basin))

basins.sort()
print(basins[-1] * basins[-2] * basins[-3])
