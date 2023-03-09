num_vertices, num_edges = 5,5
# means 1 being done allows 2 to be done
# 2 being done allows 3 and 5 to be done
edges = {
    1: [2],
    2: [3,5],
    3: [5],
    4: [3],
    5: []
}

finished_stack = []
visited = [False] * (num_vertices+2)

def dfs(x):
    '''Recursively visit all nodes connected to x'''
    visited[x] = True
    for i in edges[x]:
        if not visited[i]:
            dfs(i)
    # after all nodes connected to x have been visited
    # # add x to the finished stack
    finished_stack.append(x)

# visit all nodes
for i in range(1, num_vertices+1):
    if not visited[i]:
        dfs(i)
# finished_stack in reverse order is the topological order
topo_order = finished_stack[::-1]
print(topo_order)