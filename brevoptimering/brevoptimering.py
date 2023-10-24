from collections import deque, namedtuple
#batched is in python 3.12, define it with other stuff
from itertools import islice
def batched(iterable, n):
    # batched('ABCDEFG', 3) --> ABC DEF G
    if n < 1:
        raise ValueError('n must be at least one')
    it = iter(iterable)
    while batch := tuple(islice(it, n)):
        yield batch

Edge = namedtuple('Edge', 'destination capacity flow')

n = int(input())
max_speeds = [0]*(n+2)
node_in_degree = [0] * (n+2)
edges = [{} for _ in range(n+2)]
for i in range(n):
    m, k, *line = input().split()
    m, k = int(m), int(k)
    max_speeds[i+1] = m
    if k > 0:
        line = map(int,line)
        for j,w in batched(line, 2):
            dest = Edge(j, w*m/100, 0)
            edges[i+1][j] = dest
            # go ahead and add backward edges
            back = Edge(i+1, 0, 0)
            edges[j][i+1] = back
            node_in_degree[j] += 1
    else:
        # add an edge to the sink
        dest = Edge(n+1, m, 0)
        edges[i+1][n+1] = dest
        node_in_degree[(n+1)] += 1
max_speeds[0] = 1e9
for i,v in enumerate(node_in_degree):
    if i != 0 and v == 0:
        dest = Edge(i, 1e9, 0)
        edges[0][i] = dest

# we can forget about in degree from now on
doing_full_paths = True
while True:
    queue = deque()
    visited = set()
    prevs = {}
    queue.append((0, 1e9, 0))
    bottleneck = -1
    last_prev = -1
    while doing_full_paths and queue:
        curr, curr_flow, prev = queue.popleft()
        prevs[curr] = prev
        for i, out_edge in edges[curr].items():
            dest, capacity, flow = out_edge
            # no flow, or already visited
            if flow >= capacity or dest in visited:
                continue
            pos_flow = min(capacity-flow, curr_flow)
            # we can get to the sink
            if dest == (n+1):
                bottleneck = pos_flow
                prevs[n+1] = curr
                last_prev = n+1
                break
            queue.append((dest, pos_flow, curr))
            visited.add(dest)
    if len(queue) == 0:
        doing_full_paths = False
        continue

    if bottleneck == -1:
        # no path found to sink, try to push more through
        doing_full_paths = False
        while queue:
            curr, curr_flow, prev = queue.popleft()
            prevs[curr] = prev
            last_prev = curr
            bottleneck = curr_flow
            for i, out_edge in edges[curr].items():
                dest, capacity, flow = out_edge
                # no flow, or already visited
                if flow >= capacity or dest in visited:
                    continue
                pos_flow = min(capacity-flow, curr_flow)
                queue.append((dest, pos_flow, curr))
                visited.add(dest)
    if last_prev == 0:
        break

        
    # we now have a shortest augementing path
    curr = last_prev   
    while curr != 0:
        prev = prevs[curr]
        #update flow on forward edge (prev, curr)
        old = edges[prev][curr] 
        edges[prev][curr] = old._replace(flow = old.flow + bottleneck)
        #and reverse (curr, prev), only if not source or sink
        if prev != 0 and curr != (n+1):
            old = edges[curr][prev]
            edges[curr][prev] = old._replace(flow = old.flow - bottleneck)

        curr = prev
# here, we're done doing max flow.
total_in = [0] * (n+2)
for i in range(0,n+1):
    for source, (dest, capacity, flow) in edges[i].items():
        if capacity != 0:
            total_in[dest] += flow

res = set()
for i, v in enumerate(total_in):
    if v >= max_speeds[i]:
        res.add(i)

if n+1 in res:
    res.remove(n+1)

from pprint import pprint
pprint(edges)
print(*sorted(res))


