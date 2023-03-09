num_vertices, num_edges = 5,5
# note the cycle from 1 to 3 to 5 to 1
edges = {
    1: [3],
    2: [],
    3: [5],
    4: [2],
    5: [1]
}

'''Use dfs to detect a cycle in the graph'''
# visited[i] is True if node i has been visited
visited = [False] * (num_vertices+2)
# on_stack[i] is True if node i is on the current dfs stack
on_stack = [False] * (num_vertices+2)
# stack is the current dfs stack
stack = []
# cycle is True if a cycle is detected
cycle = False

def dfs(x):
    '''Recursively visit all nodes connected to x'''
    visited[x] = True
    on_stack[x] = True
    for i in edges[x]:
        if not visited[i]:
            dfs(i)
        elif on_stack[i]:
            # if i is on the current stack, a cycle is detected
            print("CYCLE DETECTED")
            return
    # after all nodes connected to x have been visited
    # # remove x from the stack
    on_stack[x] = False

# visit all nodes
for i in range(1, num_vertices+1):
    if not visited[i]:
        dfs(i)