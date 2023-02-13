n = int(input())
need_first = True
first = -1
for _ in range(n):
    if need_first:
        first = int(input())
        need_first = False
        continue
    c = int(input())
    if c % first == 0:
        print(c)
        need_first = True

    
