from sys import stdin
from collections import Counter
b = []
for line in stdin:
    b.append(line.strip())
c = Counter(b)
for tree in sorted(c.keys()):
    print(tree, c[tree]/len(b)*100)