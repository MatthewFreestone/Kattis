n, b, h, w = map(int,input().split())
best = 2**32
for _ in range(h):
    p = int(input())
    beds = map(int, input().split())
    if max(beds) > n and p*n <= b:
        best = min(best, p*n)
if best == 2**32:
    print("stay home")
else:
    print(best)