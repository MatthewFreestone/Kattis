from collections import deque
import math
class Graph:
	def __init__(self, r,c,graph):
		self.graph = graph
		self.r = r
		self.c = c
	def validPoint(self,i,j):
		return (i >= 0 and j >= 0 and i < self.r and j < self.c and self.graph[i][j] == "#")

	def dfs(self, i, j):
		self.graph[i][j] = '.'
		rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]
		colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]

		for k in range(8):
			if self.validPoint(i + rowNbr[k], j + colNbr[k]):
				self.dfs(i + rowNbr[k], j + colNbr[k])

	def findCircles(self):
		circles = 0
		for i in range(self.r):
			for j in range(self.c):
				if (self.graph[i][j] == '#'):
					circles += 1
					self.dfs(i,j)
		return circles
	


m,n = [int(x) for x in input().split(' ')]
dish = []
for y in range(m):
	dish.append(list([c for c in input()]))

g = Graph(m,n,dish)
print(g.findCircles())