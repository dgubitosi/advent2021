
matrix = list()
with open('input.txt') as f:
    for line in f:
        matrix.append([ p for p in list(line.strip()) ])

def _print(matrix):
    for row in matrix:
        print("".join(row))
    print()

i = 0
print(i)
_print(matrix)

while True:
    i += 1
    moves = 0
    # east-west goes before north-south
    for cc in ['>', 'v']:
        _next = [ row[:] for row in matrix ]
        for y in range(len(matrix)):
            for x in range(len(matrix[y])):
                c = matrix[y][x]
                if c != cc: continue
                # east-west
                if c == '>':
                    # next space is x+1
                    xx = x + 1
                    if xx >= len(matrix[y]):
                        xx = 0
                    if matrix[y][xx] == '.':
                        _next[y][xx] = c
                        _next[y][x] = '.'
                        moves += 1
                # north-south
                elif c == 'v':
                    # next space is y+1
                    yy = y + 1
                    if yy >= len(matrix):
                        yy = 0
                    if matrix[yy][x] == '.':
                        _next[yy][x] = c
                        _next[y][x] = '.'
                        moves += 1
        matrix = _next
    _print(_next)
    print(i, moves)
    if moves == 0: break
    matrix = _next
