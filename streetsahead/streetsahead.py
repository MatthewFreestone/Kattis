n, q = map(int, input().split())
i = 0
roads = {}
for i in range(n):
    road_name = input()
    roads[road_name] = i
for _ in range(q):
    start, end = input().split()
    print(abs(roads[start] - roads[end])-1)