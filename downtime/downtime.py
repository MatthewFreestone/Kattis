# Rating: ~ 3.1 / 10
# Link: https://open.kattis.com/problems/downtime
from sys import stdin
from bisect import bisect_left
def main():

    n, k = map(int, next(stdin).strip().split())
    ans = 0
    requests = list(map(int, stdin))
    for i, r in enumerate(requests):
        loc = bisect_left(requests, r+1000)
        ans = max(ans, loc-i)
    print(ans // k if ans % k == 0 else ans // k + 1)

    

if __name__ == "__main__":
  main()
