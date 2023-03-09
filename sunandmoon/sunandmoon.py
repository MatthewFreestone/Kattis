ds, ys = map(int, input().split())
dm, ym = map(int, input().split())
for i in range(0, 7000):
    if (ds + i) % ys == 0 and (dm + i) % ym == 0:
        print(i)
        break