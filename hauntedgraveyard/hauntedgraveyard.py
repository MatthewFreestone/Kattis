# Rating: ~ 7.5 / 10
# Link: https://open.kattis.com/problems/hauntedgraveyard
from collections import namedtuple
from pprint import pprint
def main():
  while True:
    w, h = map(int, input().split())
    if w == h == 0:
      return
    g = int(input())
    gravestones = set()
    for _ in range(g):
      x, y = map(int,input().split())
      gravestones.add((x,y))
    e = int(input())
    holes = {}
    for _ in range(e):
      x1,y1,x2,y2,t = map(int,input().split())
      holes[(x1,y1)] = (x2,y2,t)

    dist = {(wc,hc): float('inf') for wc in range(w) for hc in range(h)}
    edges = []
    Edge = namedtuple('Edge', 'x1 y1 x2 y2 t')
    around = lambda x,y: [(x+1, y), (x-1, y), (x, y+1), (x,y-1)]
    for x in range(w):
      for y in range(h):
        if (x,y) in gravestones:
          continue
        if (x,y) in holes:
          x2,y2,t = holes[(x,y)]
          edges.append(Edge(x,y,x2,y2, t))
          continue
        for cx, cy in around(x,y):
          if 0 <= cx < w and 0 <= cy < h:
            edges.append(Edge(x,y, cx, cy, 1))

    #bellman-ford
    dist[(0,0)] = 0
    for _ in range(w*h):
      for x1, y1, x2, y2, t in edges:
        dist[(x2, y2)] = min(dist[(x2, y2)], dist[(x1, y1)] + t)

    # check negative cycle
    for x1, y1, x2, y2, t in edges:
      if dist[(x2, y2)] > dist[(x1, y1)] + t:
        print("Never")
        break
    else:
      res = dist[w-1, h-1]
      if res == float('inf'):
        print("Impossible")
      else:
        print(res)



if __name__ == "__main__":
  main()
