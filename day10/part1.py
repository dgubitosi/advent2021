
close_open = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

score = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

error = 0
with open('input.txt') as f:
    for line in f:
        q = list()
        for c in list(line.strip()):
            #print(c, q)
            if c in close_open.values():
                q.append(c)
            if c in close_open.keys():
                last = q.pop(-1)
                if last != close_open[c]:
                    error += score[c]
print(error)