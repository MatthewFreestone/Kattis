import sys
from collections import defaultdict

class DFS_Graph:
    def __init__(self):
        self.graph = defaultdict(set)
        
    def rec(self, n, visited, contains):
    	visited[n] = True
    	contains.append(n)

    	for i in self.graph[n]:
    		if visited[i] == False:
    			self.rec(i, visited, contains)
    def search(self, n):
    	visited = [False] * (max(self.graph) + 1)
    	contains = []

    	self.rec(n, visited, contains)
    	return contains
    def addEdge(self, n, m):
    	self.graph[n].add(m)
    	self.graph[m].add(n)



houses,cables = [int(a) for a in input().split()]
graph = DFS_Graph()

for i in range(cables):
	n,m = [int(a) for a in input().split()]
	graph.addEdge(n,m)

if houses > 1:
    toWeb = graph.search(1)
    notCon = list([h+1 for h in range(houses) if h+1 not in toWeb])
else:
    notCon = []
    
if (len(notCon) != 0):
    for h in notCon:
        print(h)
else:
    print("Connected")
