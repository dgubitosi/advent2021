alu = {
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

# inp a   : a = input
# add a b : a = a + b
# mul a b : a = a * b
# div a b : a = a // b
# mod a b : a = a % b
# eql a b : a = (a == b)

with open('input.txt') as f:
    instructions = [line.split() for line in f.readlines()]

blocks = [instructions[i:i+18] for i in range(0, len(instructions), 18)]
for i in range(len(blocks[0])):
    t = blocks[0][i]
    temp = list()
    temp.append(t)
    for j in range(1, len(blocks)):
        inst = blocks[j][i]
        temp.append(inst)
    c = temp.count(t)
    st = f'{i:02} '
    if c == len(temp):
        st += ' '.join(t)
    else:
        p = list()
        for c in temp:
            p.append(c[-1])
        st += ' '.join(t[0:2])
        st += ' ' + str(p)
    print(st)
