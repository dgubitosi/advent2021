
def bresenhams_line(p1, p2):
        points_in_line = []

        x0 = p1[0]
        y0 = p1[1]
        x1 = p2[0]
        y1 = p2[1]

        dx = abs(x1 - x0)
        dy = abs(y1 - y0)
        x, y = x0, y0
        sx = -1 if x0 > x1 else 1
        sy = -1 if y0 > y1 else 1
        if dx > dy:
            err = dx / 2.0
            while x != x1:
                points_in_line.append((x, y))
                err -= dy
                if err < 0:
                    y += sy
                    err += dx
                x += sx
        else:
            err = dy / 2.0
            while y != y1:
                points_in_line.append((x, y))
                err -= dx
                if err < 0:
                    x += sx
                    err += dy
                y += sy
        points_in_line.append((x, y))
        return points_in_line

matrix = dict()
intersections = set()
with open('input.txt') as f:
    for line in f:
        start, end = line.strip().split(' -> ')
        start = [int(i) for i in start.split(',')]
        end = [int(i) for i in end.split(',')]
        print(start, end)

        for p in bresenhams_line(start, end):
            matrix.setdefault(p, 0)
            matrix[p] += 1
            if matrix[p] > 1: 
                intersections.add(p)

print(len(intersections))
