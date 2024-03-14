# Rating: ~ 8.2 / 10
# Link: https://open.kattis.com/problems/streetsbehind
from math import ceil
from functools import cache

@cache
def solve(n,k,a,b):
  y = (b-a) * n // a
  if y == 0:
    return -1
  days = 0
  while k > 0:
    y = (b-a) * n // a
    x = ceil(a * (y+1) / (b-a))
    dist_to_x = x - n
    steps = ceil(min(k, dist_to_x) / y)
    days += steps
    n += steps * y
    k -= steps * y
  return days

def main():
  t = int(input())
  for _ in range(t):
    days = solve(*map(int, input().split()))
    print(days)

if __name__ == "__main__":
  main()
