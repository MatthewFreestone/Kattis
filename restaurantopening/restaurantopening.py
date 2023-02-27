n, m = map(int, input().split())
population = [list(map(int, input().split())) for _ in range(n)]
best = float('inf')
def calc_dist(x,y):
    dist = 0
    for i in range(n):
        for j in range(m):
            dist += population[i][j] * (abs(x-i) + abs(y-j))
    return dist
for i in range(n):
    for j in range(m):
        best = min(best, calc_dist(i,j))
print(best)