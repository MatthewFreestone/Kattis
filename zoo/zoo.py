from collections import Counter
i = 0
while True:
    i += 1
    n = int(input())
    if n == 0: break
    animals = [input().split()[-1].lower() for _ in range(n)]
    counts = Counter(animals)
    print(f"List {i}:")
    for animal in sorted(counts):
        print(f"{animal} | {counts[animal]}")