
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

# initialize pair count using the template
pair_count = dict()
for pos in range(len(template)):
    pair = template[pos:pos+2]
    insert = pairs.get(pair, None)
    if insert:
        pair_count.setdefault(pair, 0)
        pair_count[pair] += 1
print(0, pair_count)

# replace each pair with two new pairs every iteration
for i in range(40):
    t = pair_count.copy()
    # every pair gets replaced by two new pairs
    for p in pair_count:
        if pair_count[p] <= 0: continue
        insert = pairs.get(p, None)
        if insert:
            # increase count of new pairs
            # pair 1
            p1 = p[0] + insert
            t.setdefault(p1, 0)
            t[p1] += pair_count[p] #1

            # pair 2
            p2 = insert + p[1]
            t.setdefault(p2, 0)
            t[p2] += pair_count[p] #1

            # reduce count of previous pair
            t[p] -= pair_count[p]

    pair_count = t
    print(i+1, pair_count)

# count the individual polymers in every pair
polymers = dict()
for p in pair_count:
    c = pair_count[p]
    if c <= 0: continue
    polymers.setdefault(p[0], 0)
    polymers[p[0]] += c
    polymers.setdefault(p[1], 0)
    polymers[p[1]] += c

# correct for double counting,
# always rounding up
for p in polymers:
    c = (polymers[p] // 2) + (polymers[p] % 2)
    polymers[p] = c

s = sorted(polymers.items(), key=lambda p: p[1])
print(s)
print(s[-1][1] - s[0][1])