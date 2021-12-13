
caves = dict()
with open('test1.txt') as f:
    for line in f:
        a, z = line.strip().split('-')
        caves.setdefault(a, set()).add(z)
        caves.setdefault(z, set()).add(a)

parent = 'start'
visited = set({parent})
to_visit = list()

to_visit.extend(list(caves[parent]))
while to_visit:
    n = to_visit.pop()
    print(parent, n)
    if n.islower():
        visited.add(n)
    parent = n
    if parent not in visited:
        to_visit.extend(list(caves[parent]))
