# use prim's algorithm to find the minimum spanning tree
from heapq import heappush, heappop, heapify
num_vertices, num_edges = 5,5
# src: dest, weight
edges = {
    0: [(1, 1), (2,2)],
    1: [(2, 3), (3,4)],
    2: [(3, 5)],
}
mst = set()  # set to store the edges in the MST
visited = {0}  # set to store the visited vertices
total_weight = 0
start_node = 0
edge_pq = [(float('inf'), i, None) for i in edges.keys() if i != start_node]
for x, weight in edges[start_node]:
    new_item = (weight, x, (start_node, x))
    # we will always do better than infinity
    heappush(edge_pq, new_item) 

while edge_pq and len(visited) < num_vertices:
    cost, dest, edge = heappop(edge_pq)

    if dest not in visited:
        visited.add(dest)
        mst.add(edge)
        total_weight += cost
        for c_dest, c_cost in edges.get(dest, []):
            if c_dest not in visited:
                heappush(edge_pq, (c_cost, c_dest, (dest, c_dest)))
print("Total weight: ", total_weight)
print(mst)

