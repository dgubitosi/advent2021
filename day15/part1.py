
graph = list()
with open("input.txt") as f:
    for line in f:
        graph.append([int(x) for x in list(line.strip())])

# dijkstra algorithm
# nodes are (y,x) position in the graph
to_visit = list()
cost = dict()
for y in range(len(graph)):
    for x in range(len(graph[y])):
        to_visit.append((y,x))
        # initialize cost to nodes to inifinity
        cost[(y,x)] = float('inf')

# starting node cost is zero
cost[(0,0)] = 0

# maintain path by keeping the parent to each node
parent = dict()

while to_visit:
    # find the nearest node
    nearest = None
    for n in to_visit:
        if nearest == None:
            nearest = n
        elif cost[n] < cost[nearest]:
            nearest = n

    # get all neighbors to nearest node
    y, x = nearest
    neighbors = list()
    if y > 0:
        neighbors.append((y-1, x))
    if y < len(graph)-1:
        neighbors.append((y+1, x))
    if x > 0:
        neighbors.append((y, x-1))
    if x < len(graph[y])-1:
        neighbors.append((y, x+1))

    # check each neighbor
    for n in neighbors:
        y, x = n
        c = cost[nearest] + graph[y][x]
        if c < cost[n]:
            cost[n] = c
            parent[n] = nearest

    to_visit.remove(nearest)
    
y = len(graph)-1
x = len(graph[y])-1
p = (y, x)
print(p, cost[p])

# find path working backwards
path = [(p)]
while p != (0,0):
    y, x = p
    c = graph[y][x]
    tc = cost[p]
    pp = parent[p]
    print(pp, '-->', p, c, tc)
    p = pp
    path.append(p)

# path
print(path[::-1])