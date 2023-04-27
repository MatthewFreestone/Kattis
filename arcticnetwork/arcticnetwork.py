from heapq import heappop, heappush
from math import sqrt
n = int(input())
for _ in range(n):
    s, p = map(int, input().split())
    points = set()
    for _ in range(p):
        x,y = map(int, input().split())
        points.add((x,y))

    # find MST
    x,y = next(iter(points))
    points_in_tree = {(x,y)}
    pq = []
    points.remove((x,y))
    for x2,y2 in points:
        c_dist = sqrt((x-x2)**2 + (y-y2)**2)
        e = (c_dist, (x,y), (x2,y2))
        heappush(pq, e)

    selected_edges = []
    while len(points_in_tree) < p and pq:
        dist, (sx, sy), (dx, dy) = heappop(pq)
        if (dx,dy) in points_in_tree:
            continue
        points_in_tree.add((dx,dy))
        points.remove((dx,dy))
        selected_edges.append((dist, (sx, sy), (dx, dy)))
        for x2,y2 in points:
            c_dist = sqrt((dx-x2)**2 + (dy-y2)**2)
            e = (c_dist, (dx,dy), (x2, y2))
            heappush(pq, e)

    # remove s largest edges
    selected_edges.sort()
    # print(selected_edges)
    print(f"{selected_edges[-s][0]:.2f}")





    
