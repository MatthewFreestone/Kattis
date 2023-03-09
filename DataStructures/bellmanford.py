
num_points, start, end = 4, 1, 3
distances = [[0, 1, 3, -2], 
             [2, 0, 4, 22], 
             [3, -2, 0, 7], 
             [13, 8, 2, 0]]

def bellman_ford():
    # initialize distances to infinity
    dist = [float("inf")] * num_points
    # set distance to start to 0
    dist[start] = 0
    # relax edges repeatedly
    for _ in range(num_points):
        for i in range(num_points):
            for j in range(num_points):
                if dist[j] > dist[i] + distances[i][j]:
                    dist[j] = dist[i] + distances[i][j]
    # check for negative cycles
    for i in range(num_points):
        for j in range(num_points):
            if dist[j] > dist[i] + distances[i][j]:
                print(dist)
                print("Negative cycle detected")
                return
    print(dist)

bellman_ford()
