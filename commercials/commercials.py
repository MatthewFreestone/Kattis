# Rating: ~ 1.9 / 10
# Link: https://open.kattis.com/problems/commercials

def main():
    n, p = map(int,input().split())
    a = [*map(int,input().split())]
    for i in range(len(a)):
        a[i] -= p
    score = 0
    ans = 0
    for i in a:
        score += i
        ans = max(ans, score)
        if score < 0: score = 0
    print(ans)

if __name__ == "__main__":
  main()

