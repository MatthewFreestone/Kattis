# Rating: ~ 1.6 / 10
# Link: https://open.kattis.com/problems/orderedproblemset

def main():
    n = int(input())
    difficulty = [int(input()) for _ in range(n)]
    ans = []
    for k in range(2, n+1):
        if n % k != 0: continue
        size = n // k
        smallest_lefts = []
        biggest_rights = []
        for i in range(k):
            interval = difficulty[i*size:(i+1)*size]
            smallest_lefts.append(min(interval))
            biggest_rights.append(max(interval))
        if all(smallest_lefts[i] > biggest_rights[i-1] for i in range(1,k)):
            ans.append(k)
    if len(ans) == 0:
        print(-1)
    else:
        print(*ans, sep='\n')


if __name__ == "__main__":
  main()
