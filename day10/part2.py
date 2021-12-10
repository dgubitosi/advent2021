
close_open = {
    ')': '(',
    ']': '[',
    '}': '{',
    '>': '<',
}

score = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}

completion_cost = list()
with open('input.txt') as f:
    for line in f:
        q = list()
        for c in list(line.strip()):
            if c in close_open.values():
                q.append(c)
            if c in close_open.keys():
                last = q.pop(-1)
                # corrupt line
                if last != close_open[c]:
                    q.clear()
                    break
        # incomplete line
        if q:
            #print("".join(q))
            error = 0
            while q:
                c = q.pop(-1)
                error *= 5
                error += score[c]
            completion_cost.append(error)

completion_cost.sort()
#print(completion_cost)
print(completion_cost[int(len(completion_cost)/2)])