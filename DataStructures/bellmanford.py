
from heapq import heappop as pop, heappush as push
start = 2
graph = {1: {2: 1, 3: 3, 4: -2},
            2: {1: 2, 3: 4, 4: 22},
            3: {1:3, 2: -2, 4: 7},
            4: {1: 13, 2: 8, 3: 2}}


def bellman_ford(
        graph: dict[int, dict[int, int]], # Node: [Node, EdgeWeight]
        source: int
    )-> dict[int, int]: # Node: Cost
    num_points = len(graph)
    # initialize distances to infinity
    dist = {i: float("inf") for i in graph.keys()}
    # set distance toward source to 0
    dist[source] = 0
    # relax edges repeatedly
    for _ in range(num_points):
        for start in graph.keys():
            for end in graph[start].keys():
                if dist[end] > dist[start] + graph[start][end]:
                    dist[end] = dist[start] + graph[start][end]
    # check for negative cycles
    for start in graph.keys():
        for end in graph[start].keys():
            if dist[end] > dist[start] + graph[start][end]:
                print("Negative cycle detected")
                return None
    return dist

res = bellman_ford(graph, source=start)
print(res)
