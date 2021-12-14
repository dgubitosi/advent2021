
template = ''
pairs = dict()
with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        if '->' in line:
            a, b = [x.strip() for x in line.split('->', 2)]
            pairs.setdefault(a, b)
        else:
            template = line

#print(template)
for i in range(40):
    t = ''
    for pos in range(len(template)):
        pair = template[pos:pos+2]
        insert = pairs.get(pair, None)
        if insert is not None:
            if not t:
                t += template[pos]
            t += insert
            t += template[pos+1]
    #print(f'Step {i+1}', len(t))
    template = t

polymers = dict()
for c in template:
    polymers.setdefault(c, 0)
    polymers[c] += 1

s = sorted(polymers.items(), key=lambda p: p[1])
print(s[-1][1] - s[0][1])