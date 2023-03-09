# Rating: ~ 5.0 / 10
# Link: https://open.kattis.com/problems/pickupsticks
from collections import defaultdict
from time import sleep
import sys

sys.setrecursionlimit(10_000)

def main():
  n, m = map(int, input().split())
  edges = defaultdict(list)

  for _ in range(m):
    # a is on top of b
    a, b = map(int, input().split())
    edges[a].append(b)

  # detect cycle in edges
  visited = [False] * (n+2)
  in_stack = [False] * (n+2)

  def cyclic(x):
    visited[x] = True
    in_stack[x] = True
    for i in edges[x]:
      if not visited[i]:
        if cyclic(i):
          return True
      elif in_stack[i] == True:
        return True
    in_stack[x] = False
    return False
  
  for node in range(1, n+1):
    if not visited[node]:
      if cyclic(node):
        print("IMPOSSIBLE")
        return

  stack = []
  visited = [False] * (n+2)

  def dfs(x):
    visited[x] = True
    for i in edges[x]:
      if not visited[i]:
        dfs(i)
    stack.append(x)

  try:
    for i in range(1, n+1):
      if not visited[i]:
        dfs(i)
    print(*stack[::-1], sep="\n")
  except RuntimeError:
    print("Bad Answer")


if __name__ == "__main__":
  main()
