# Rating: ~ 2.9 / 10
# Link: https://open.kattis.com/problems/anothercandies
from sys import stdin

def main():
  n = int(next(stdin))
  for _ in range(n):
    next(stdin)
    kids_count = int(next(stdin))
    total = 0
    kids = map(int, [next(stdin) for _ in range(kids_count)])
    for k in kids:
      total += k
    if total % kids_count == 0:
      print('YES')
    else:
      print('NO')
      
if __name__ == "__main__":
  main()
