# use kruskal's algorithm to find the minimum spanning tree

num_vertices, num_edges = 5,5
# src, dest, weight
edges = [
    (1, 2, 1),
    (1, 3, 2),
    (2, 3, 3),
    (2, 4, 4),
    (3, 4, 5)
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
# take the edges in sorted order (min weight first)
for src, dest, weight in sorted(edges, key=lambda x: x[2]):
    if find(src) != find(dest):
        union(src, dest)
        total_weight += weight
print("Total weight:", total_weight)