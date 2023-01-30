from collections import defaultdict

class DFS_Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def recVisit(self, v, visited, contains):
        visited[v] = True
        contains.append(v)
        #print(v)
        for i in self.graph[v]:
            if visited[i] == False: #unvisited
                self.recVisit(i, visited, contains)
                
    def search(self,v):
        contains = []
        if len(self.graph) != 0:
            visited = [False] * (max(self.graph)+1)
            self.recVisit(v, visited, contains)
        return contains

   


 
def checkAround(x):
    if x % c != c-1 and flat[x] == flat[x+1]: #add to the right
        graph.addEdge(x, x+1)
    if x % c != 0 and flat[x] == flat[x-1]: #add to the left
        graph.addEdge(x, x-1)
    if x - c > 0 and flat[x] == flat[x-c]: #add above
        graph.addEdge(x, x-c)
    if (x + c) < (r*c) and flat[x] == flat[x+c]: #add below
        graph.addEdge(x, x+c)


r,c = input().split()
r=int(r)
c=int(c)
flat = []
for i in range(r):
    mapLine = input()
    for num in mapLine:
        flat.append(int(num))
    
n = int(input())
points = [[]] * n
for i in range(n):
    coords = []
    pointsLine = input().split()
    for num in pointsLine:
        coords.append(int(num))
    points[i]= coords

graph = DFS_Graph()

for i in range(len(flat)):
    checkAround(i) #creates edges

for (y1,x1,y2,x2) in points:
    #print("points ", x1,y1,x2,y2)
    sIndex = (x1-1) + c*(y1-1)
    eIndex = (x2-1) + c*(y2-1)
    #print("from ", sIndex, " to ", eIndex)
    if (sIndex != eIndex):
        contains = graph.search(sIndex)
    else:
        contains = [eIndex]
    #print(contains)
    if eIndex in contains:
        if flat[eIndex] == 1:
            print("decimal")
        else:
            print("binary")  
    else:
        print("neither")
        



