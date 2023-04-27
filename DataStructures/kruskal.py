# use kruskal's algorithm to find the minimum spanning tree

num_vertices, num_edges = 5,5
# src, dest, weight
edges = [
    (0, 1, 1),
    (0, 2, 2),
    (1, 2, 3),
    (1, 3, 4),
    (2, 3, 5)
]

# Use union find to find the minimum spanning tree
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
print("Total weight:", total_weight)
print(mst)