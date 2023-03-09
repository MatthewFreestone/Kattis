# Rating: ~ 5.0 / 10
# Link: https://open.kattis.com/problems/pickupsticks
from collections import defaultdict

def main():
  n, m = map(int, input().split())
  edges = defaultdict(list)

  for _ in range(m):
    # a is on top of b
    a, b = map(int, input().split())
    edges[a].append(b)

  # detect cycle

  # def cyclic(x):
  #   visited[x] = True
  #   in_stack[x] = True
  #   for i in edges[x]:
  #     if not visited[i]:
  #       if cyclic(i):
  #         return True
  #     elif in_stack[i] == True:
  #       return True
  #   in_stack[x] = False
  #   return False
  visited = [False] * (n+1)
  in_stack = [False] * (n+1)
  for node in range(1, n+1):
    if not visited[node]:
      rec_stack = []
      rec_stack.append(node)
      while rec_stack:
        curr = rec_stack.pop()
        visited[curr] = True
        in_stack[curr] = True
        for i in edges[curr]:
          if not visited[i]:
            rec_stack.append(i)
          elif in_stack[i] == True:
            print("IMPOSSIBLE")
            return
        in_stack[curr] = False

  print(visited)
  stack = []
  visited = [False] * (n+1)

  def dfs(x):
    visited[x] = True
    for i in edges[x]:
      if not visited[i]:
        dfs(i)
    stack.append(x)

  for i in range(1, n+1):
    if not visited[i]:
      dfs(i)
  print('\n'.join((str(i) for i in reversed(stack))))


if __name__ == "__main__":
  main()
