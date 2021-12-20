
def _print(matrix, border=0):
    # from top to bottom
    for y in range(border, len(matrix)-border):
        row = ''
        # from left to right
        for x in range(border, len(matrix[y])-border):
            row += matrix[y][x]
        print(row)

def _lit(matrix, border=0):
    c = 0
    # from top to bottom
    for y in range(border, len(matrix)-border):
        # from left to right
        for x in range(border, len(matrix[y])-border):
            p = matrix[y][x]
            if p == '#': c += 1
    return c

algo = ''
border = 200
matrix = list()
with open('input.txt') as f:
    algo = f.readline().strip()
    line = f.readline()
    while line:
        line = line.strip()
        if line:
            # extend each line
            line = '.'*border + line + '.'*border
            # extend the top
            if not matrix:
                for i in range(border):
                    matrix.append([p for p in list('.'*len(line))])
            # add lines
            matrix.append([p for p in list(line)])
        line = f.readline()
    # extend the bottom
    line = matrix[0]
    for i in range(border):
        matrix.append(line)

for c in range(50):
    next_matrix = list()

    # top
    line = matrix[0]
    next_matrix.append(line)

    # from top to bottom
    for y in range(1, len(matrix)-1):
        row = '.'
        # from left to right
        for x in range(1, len(matrix[y])-1):
            # get nine pixels and algo index
            index = ''
            for i in [-1, 0, 1]:
                for j in [-1, 0, 1]:
                    p = matrix[y+i][x+j]
                    if p == '.':
                        bit = '0'
                    else:
                        bit = '1'
                    index += bit
            index = int(index, 2)
            row += algo[index]
        row += '.'
        next_matrix.append([p for p in list(row)])

    # bottom
    next_matrix.append(line)

    matrix = next_matrix
    print(c+1, _lit(matrix, border//2))
