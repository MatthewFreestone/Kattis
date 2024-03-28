from collections import namedtuple
n,k = map(int,input().split())
l = [int(c)-1 for c in input().split()]
print(l)
cycles = []
cycle_size = [1]*len(l)
# VisitedNode = namedtuple('VisitedNode', 'index depth runnum')
visited = {}
runnum = 0
def dfs(x, depth=0):
    if x in visited:
        if visited[x][1] == runnum:
            return depth - visited[x][0]
        else:
            return cycle_size[x] + 1
    else:
        visited[x]=(depth, runnum)
        if x != l[x]:
            # dfs(l[x], depth+1)
            cycle_size[x] = dfs(x, depth+1)
        
for start in range(len(l)):
    dfs(start)
    runnum += 1

print(visited, cycle_size)