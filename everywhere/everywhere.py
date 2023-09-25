t = int(input())
for _ in range(t):
    n = int(input())
    c = {input() for _ in range(n)}
    print(len(c))