from datetime import datetime

tile = list()
with open("input.txt") as f:
    for line in f:
        tile.append([int(x) for x in list(line.strip())])

# dijkstra algorithm
# nodes are (y,x) position in the graph
# graph is 5 x the tile in each direction
to_visit = list()
cost = dict()
graph = list()
for y in range(5*len(tile)):
    row = list()
    for x in range(5*len(tile[y % 5])):
        to_visit.append((y,x))
        # initialize cost to nodes to inifinity
        cost[(y,x)] = float('inf')

        # tile
        y_div = y // len(tile)
        x_div = x // len(tile[y % 5])

        # position in tile
        y_mod = y % len(tile)
        x_mod = x % len(tile[y % 5])

        pc = tile[y_mod][x_mod] + y_div + x_div
        while pc > 9:
            pc -= 9
        row.append(pc)
    graph.append(row)

#for row in graph:
#    print("".join([str(x) for x in row]))

# starting node cost is zero
cost[(0,0)] = 0

# maintain path by keeping the parent to each node
parent = dict()

while to_visit:
    l = len(to_visit)
    if l % 1000 == 0:
        print(datetime.now(), l)
    
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

exit(0)

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