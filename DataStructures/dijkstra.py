from heapq import heappop, heappush

num_points, start, end = 4, 1, 3
distances = [[0, 1, 3, 14], 
             [2, 0, 4, 22], 
             [3, 10, 0, 7], 
             [13, 8, 2, 0]]
finalized_distances = [-1] * num_points

current_distances = []
heappush(current_distances, (0, start))
while current_distances:
    dist, index = heappop(current_distances)
    if finalized_distances[index] != -1:
        # we've already finalized this node, we should move on
        continue
    # finalize this distance
    finalized_distances[index] = dist
    for i in range(num_points):
        if i == index:
            continue
        if finalized_distances[i] == -1:
            # only try to improve distance if it is not finalized
            heappush(current_distances, (dist + distances[index][i], i))

print(finalized_distances[end])
        