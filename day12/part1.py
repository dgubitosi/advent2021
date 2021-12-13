
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
    for n in graph[start]:
        if n not in active_path or n.isupper():
            for p in find_all_paths(n, end, active_path):
                paths.append(p)
    return paths

paths = find_all_paths('start', 'end')
for p in paths:
    print(p)
print(len(paths))