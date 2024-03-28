n, k = map(int, input().split())
l = [int(c)-1
      for c in input().split()]

c = 0
for _ in range(len(l)):
    for i in range(len(l)):
        if not l[i] == 0:
            if l[i] == i+1 or l[l[i]-1] == 0:
                l[i] = 0
                c += 1

print(min(k,c))