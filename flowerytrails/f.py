# Rating: ~ 3.8 / 10
# Link: https://open.kattis.com/problems/flowerytrails
import sys
from heapq import heappop as pop, heappush as push
from collections import defaultdict, namedtuple
from pprint import pprint


def main():
    p, t = map(int, input().split())
    trails = [[] for _ in range(p)]
    for line in sys.stdin:
        p1, p2, l = map(int, line.split())
        trails[p1].append((p2, l))
        trails[p2].append((p1, l))
    possible_paths = defaultdict(list)
    vis = {}
    pq = [(0, 0, [(0, 0)])]
    while pq and len(vis) < len(trails):
        dist, curr, path = pop(pq)
        if curr in vis:
            if vis[curr][0] == dist:
                possible_paths[curr].append(path)
            continue
        # pprint(pq)
        vis[curr] = (dist, path)
        for (nxt, w) in trails[curr]:
            if nxt not in vis:
                push(pq, (dist + w, nxt, path+[(nxt, w)]))
    for v in vis.keys():
        possible_paths[v].append(vis[v][1])

    # pprint(possible_paths)
    flower_power = 0
    visited = set()
    queue = set()
    for final in possible_paths[p-1]:
        queue.add(final[-2][0])
        flower_power += final[-1][1]
    visited.add(p-1)
#   print(queue)
    while queue:
        curr = queue.pop()
        if curr == 0:
            continue
        for path in possible_paths[curr]:
            queue.add(path[-2][0])
            flower_power += path[-1][1]
    print(flower_power*2)


if __name__ == "__main__":
    main()
