from collections import deque, defaultdict

adj_list = {
    1: {2},
    2: {1, 4, 3},
    3: {2, 4},
    4: {2, 3}
}

def bfs(vertex, adj_list: defaultdict(set)):

    # keep track of visited vertices, could use list
    visited = set()
    # using Queue, so BFS
    bfs_queue = deque()

    bfs_queue.appendleft(vertex)
    visited.add(vertex)
    while bfs_queue:
        current = bfs_queue.pop()

        # visit the node, could do something here
        print(current)

        # if not using defaultdict, you'd need to ensure
        # that current is in ajd_list
        for neighbor in adj_list[current]:
            if neighbor not in visited:
                bfs_queue.appendleft(neighbor)
                visited.add(neighbor)

def dfs_iter(vertex, adj_list):
    # keep track of visited vertices, could use list
    visited = set()
    # using Stack, so DFS
    dfs_stack = list()

    dfs_stack.append(vertex)
    while dfs_stack:
        current = dfs_stack.pop()

        # if DFS, we visit on pop, not enqueue
        if current in visited:
            continue
        visited.add(current)

        # visit the node, could do something here
        print(current)

        # if not using defaultdict, you'd need to ensure
        # that current is in ajd_list
        for neighbor in adj_list[current]:
            if neighbor not in visited:
                dfs_stack.append(neighbor)

dfs_iter(2, adj_list)
