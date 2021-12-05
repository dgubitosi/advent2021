
matrix = dict()
intersections = set()
with open('input.txt') as f:
    for line in f:
        start, end = line.strip().split(' -> ')
        start = [int(i) for i in start.split(',')]
        end = [int(i) for i in end.split(',')]
        print(start, end)

        max_x = max(start[0], end[0])
        min_x = min(start[0], end[0])
        max_y = max(start[1], end[1])
        min_y = min(start[1], end[1])

        # vertical, x is the same
        if min_x == max_x:
            for y in range(min_y, max_y + 1):
                p = (start[0], y)
                matrix.setdefault(p, 0)
                matrix[p] += 1
                if matrix[p] > 1: 
                    intersections.add(p)

        # horizontal, y is the same
        if min_y == max_y:
            for x in range(min_x, max_x + 1):
                p = (x, start[1])
                matrix.setdefault(p, 0)
                matrix[p] += 1
                if matrix[p] > 1: 
                    intersections.add(p)

print(len(intersections))
