from collections import deque, defaultdict

adj_list = defaultdict(set)
adj_list[1].add(2)
adj_list[2].add(1)
adj_list[2].add(4)
adj_list[4].add(2)
adj_list[3].add(2)
adj_list[2].add(3)
adj_list[3].add(4)
adj_list[4].add(3)

def bfs(vertex, destination):
    visited = set()
    to_visit = deque()
    # keep track of the previous node on path for each 
    previous_node = dict()

    to_visit.appendleft((vertex, vertex))
    while to_visit:
        current, prev = to_visit.pop()
        previous_node[current] = prev

        # If we've reached the destination, we can stop search
        if current == destination:
            break

        for neighbor in adj_list[current]:
            if neighbor not in visited:
                to_visit.appendleft((neighbor, current))
                visited.add(neighbor)
    
    path_to_destination = []
    current = destination
    while current != vertex:
        path_to_destination.append(current)
        current = previous_node[current]
    path_to_destination.append(vertex)
    path_to_destination.reverse()
    print(path_to_destination)

bfs(1, 4)
