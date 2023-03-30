n, q  = map(int,input().split())
problems = sorted(list(map(int, input().split())))
queries = [tuple(map(int, input().strip().split())) for _ in range(q)]
for t, d in queries:
    if t == 1:
        idx = 0
        while idx < len(problems):
            if problems[idx] > d:
                print(problems[idx])
                problems.pop(idx)
                break
            idx += 1
        else:
            print(-1)
    else:
        idx = len(problems) - 1
        while idx >= 0:
            if problems[idx] <= d:
                print(problems[idx])
                problems.pop(idx)
                break
            idx -= 1
        else:
            print(-1)