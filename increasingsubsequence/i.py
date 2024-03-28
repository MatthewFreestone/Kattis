while (line := input()) != '0':
    n, *s = line.split()
    n = int(n)
    s = [*map(int, s)]
    best = 0
    best_idx = -1

    dp = [1] * n  
    prev = [-1] * n  
    for i in range(n):
        for j in range(i):
            if s[i] > s[j]:
                if dp[j]+1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
                    if dp[i] > best:
                        best = dp[i]
                        best_idx = i
    curr = best_idx
    res = []
    while curr != -1:
        res.append(str(s[curr]))
        curr = prev[curr]
    print(best, ' '.join(reversed(res)))
