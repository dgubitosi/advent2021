
graph = dict()
with open('input.txt') as f:
    for line in f:
        a, z = line.strip().split('-')
        graph.setdefault(a, list()).append(z)
        graph.setdefault(z, list()).append(a)

def find_all_paths(start, end, active_path=list()):
    active_path = active_path + [start]
    if start == end:
        return [active_path]
    paths = list()
    for n in sorted(graph[start]):
        can_visit = False
        if n.isupper():
            can_visit = True
        # n.islower()
        else:
            if n not in active_path:
                can_visit = True
            else: # n.islower()
                if n not in active_path:
                    can_visit = True
                elif n not in ['start', 'end']:
                    repeats = [ v for v in active_path if v.islower() and active_path.count(v) > 1 ]
                    can_visit = len(repeats) == 0
        if can_visit:
            for p in find_all_paths(n, end, active_path):
                paths.append(p)
    return paths

paths = find_all_paths('start', 'end')
for p in paths:
    print(",".join(p))
print(len(paths))