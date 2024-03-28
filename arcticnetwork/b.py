from math import hypot
n = int(input())

for _ in range(n):
    s, p = map(int, input().split())

    nodes = []
    for _ in range(p):
        x,y = map(int, input().split())
        nodes.append((x,y))
    
    # edges_lengths = [hypot(x2-x1,y2-y1) for x1,y1 in nodes for x2,y2 in nodes if x1 != x2 and y1 != y2]

    edges = []
    for i in range(p):
        for j in range(i+1, p):
            edges.append((i, j, hypot(nodes[i][0] - nodes[j][0], nodes[i][1] - nodes[j][1])))
    
    num_vertices = p
    parents = [i for i in range(num_vertices+1)]
    def find(x):
        if parents[x] == x:
            return x
        parents[x] = find(parents[x])
        return parents[x]
    def union(x, y):
        parents[find(x)] = find(y)

    total_weight = 0
    mst = set()
    # take the edges in sorted order (min weight first)
    for src, dest, weight in sorted(edges, key=lambda x: x[2]):
        if find(src) != find(dest):
            union(src, dest)
            total_weight += weight
            mst.add((src, dest, weight))

    mst = list(sorted(mst, key = lambda x: x[2]))
    while s > 1:
        mst.pop()
        s -= 1
    print(f"{mst[-1][2]:.2f}")
    
    