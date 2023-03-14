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
    Node = namedtuple('Node', ['dist', 'curr', 'prev', 'last_hop'])
    possible_paths = defaultdict(list)
    vis = {}
    pq = [Node(0, 0, None, None)]
    while pq:
        dist, curr, prev, last_hop = pop(pq)
        if curr in vis:
            if vis[curr][0] == dist:
                possible_paths[curr].append((prev, last_hop))
            continue
        vis[curr] = (dist, prev, last_hop)
        for (nxt, w) in trails[curr]:
            if nxt not in vis:
                push(pq, Node(dist + w, nxt, curr, w))
    for v in vis.keys():
        possible_paths[v].append((vis[v][1], vis[v][2]))

    flower_power = 0
    visited = set()
    queue = []
    for prev, w in possible_paths[p-1]:
        queue.append(prev)
        flower_power += w
    visited.add(p-1)
    visited.add(0)
    while queue:
        curr = queue.pop()
        if curr in visited:
            continue
        for prev, w  in possible_paths[curr]:
            queue.append(prev)
            flower_power += w
        visited.add(curr)
    print(flower_power*2)


if __name__ == "__main__":
    main()
