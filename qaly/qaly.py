n = int(input())
total = 0
for _ in range(n):
    a,b=map(float, input().split())
    total += a*b
print(total)