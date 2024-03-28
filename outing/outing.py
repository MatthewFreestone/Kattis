from collections import namedtuple, defaultdict
from bisect import bisect_right
n,k = map(int,input().split())
l = [int(c)-1 for c in input().split()]

parents = [i for i in range(len(l))]
def find(x):
    if x == parents[x]:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]
def union(x,y):
    parents[find(x)] = find(y)

for i, v in enumerate(l):
    union(i,v)

for i in range(len(l)):
    find(i)

# print(parents)

cycles = []
cycles_in_group = [0] * len(l)
# VisitedNode = namedtuple('VisitedNode', 'index depth runnum')
visited = {}
runnum = 0
def dfs(x, depth=0):
    if x in visited:
        if visited[x][1] == runnum:
            cycles_in_group[x] = depth - visited[x][0]
            # cycles.append(depth - visited[x][0])
    else:
        visited[x]=(depth, runnum)
        dfs(l[x], depth+1)
        
for start in range(len(l)):
    dfs(start)
    runnum += 1
# print(visited, cycles)
group_to_size_and_cycle_size = defaultdict(lambda: [0,0])
for g, c in zip(parents, cycles_in_group):
    group_to_size_and_cycle_size[g][0] += 1
    group_to_size_and_cycle_size[g][1] = max(group_to_size_and_cycle_size[g][1], c)
# print(dict(group_to_size_and_cycle_size))

vals = [(y, x-y) for x,y in group_to_size_and_cycle_size.values()]
# vals.sort(key=lambda x: (x[1], x[0]), reverse=True)
vals.sort(reverse=True)
# print(vals)
best_overall = [0]
def recTry(total_cycle, total_free, curr):
    # print(total_cycle, total_free, curr)
    if total_cycle <= k and curr <= len(vals)-1:
        best_overall[0] = max(best_overall[0], total_free+total_cycle)
        if best_overall[0] >= k:
            print(k)
            exit()
        recTry(total_cycle+vals[curr][0], total_free+vals[curr][1], curr+1)
        recTry(total_cycle, total_free, curr+1)
recTry(0, 0, -1)

print(min(best_overall[0], k))