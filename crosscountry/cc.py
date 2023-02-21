from heapq import heappop, heappush

n, s, t = map(int, input().split())
distances = [list(map(int, input().split())) for _ in range(n)]
finalized_distances = [-1] * n

current_distances = []
heappush(current_distances, (0, s))
while current_distances:
    dist, index = heappop(current_distances)
    if finalized_distances[index] != -1:
        # we've already finalized, we should move on
        continue
    # finalize this distance
    finalized_distances[index] = dist
    for i in range(n):
        if i == index:
            continue
        if finalized_distances[i] == -1:
            # only try to improve distance if it is not finalized
            heappush(current_distances, (dist + distances[index][i], i))

print(finalized_distances[t])
        