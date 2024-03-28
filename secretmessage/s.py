from math import ceil, sqrt
# from pprint import pprint
n = int(input())
for _ in range(n):
    message = input()
    nextSqrt = ceil(sqrt(len(message)))
    numStars = nextSqrt**2 - len(message)
    message += '*' * numStars
    table = [[] for _ in range(nextSqrt)]
    c = 0
    for i in range(nextSqrt):
        for _ in range(nextSqrt):
            table[i].append(message[c])
            c += 1
    # pprint(table)
    table = [*zip(*table)]
    table = [[*reversed(i)] for i in table]
    # pprint(table)
    ans = []
    for i in table:
        for c in i:
            if c != '*':
                ans.append(c)
    print(''.join(ans))
    # break
