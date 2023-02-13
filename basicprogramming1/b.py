n, t = map(int, input().split())
a = list(map(int, input().split()))
if t == 1:
    print(7)
elif t == 2:
    if a[0] > a[1]:
        print("Bigger")
    elif a[0] < a[1]:
        print("Smaller")
    else:
        print("Equal")
elif t == 3:
    sub = sorted(a[:3])
    print(sub[1])
elif t == 4:
    print(sum(a))
elif t == 5:
    print(sum([x for x in a if x % 2 == 0]))
elif t == 6:
    start = ord('a')
    print(''.join([chr(start+(x % 26)) for x in a]))
elif t == 7:
    visited = set()
    curr = 0
    while True:
        curr = a[curr]
        if curr == (n-1):
            break
        if not (0 <= curr < n):
            print("Out")
            exit()  
        if curr in visited:
            print("Cyclic")
            exit()
        visited.add(curr)
    print("Done")