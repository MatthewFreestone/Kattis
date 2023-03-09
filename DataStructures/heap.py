from heapq import heappush, heappop, heapify

a = [5, 7, 9, 1, 3]
heapify(a)
print(a)

heappush(a, 4)
print(a)

print(heappop(a))
print(a)