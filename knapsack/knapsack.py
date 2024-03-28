from sys import stdin

def main():
    while True:
        line = stdin.readline()
        if not line:
            break
        values = []
        weights = []
        c,n = map(int,line.split())
        for _ in range(n):
            v,w = map(int,stdin.readline().split())
            values.append(v)
            weights.append(w)
        memo = [[-1]*(c+1) for _ in range(n+1)]
        path_memo = [[0]*(c+1) for _ in range(n+1)]
        def dp(id, remainingW, path):
            if (id == n) or (remainingW == 0):
                return 0, path
            if memo[id][remainingW] != -1:
                return memo[id][remainingW], path_memo[id][remainingW]
            if weights[id] > remainingW:
                memo[id][remainingW], path_memo[id][remainingW] = dp(id+1, remainingW, path) # don't take id
                return memo[id][remainingW], path_memo[id][remainingW]
            pos1, path1 = dp(id+1, remainingW, path)
            pos2, path2 = dp(id+1, remainingW-weights[id], path | (1<<id))
            pos2 += values[id] 
            ans = (pos1, path1) if pos1 > pos2 else (pos2, path2)
            memo[id][remainingW] = ans[0]
            path_memo[id][remainingW] = ans[1]
            return memo[id][remainingW], path_memo[id][remainingW]
        dp(0, c, 0)
        path = path_memo[0][-1]
        res = []
        i = 0
        while path:
            t = 1 << i
            if path & t:
                res.append(str(i))
                path ^= t
            i += 1
        print(len(res), ' '.join(res), sep='\n')
if __name__ == '__main__':
    main()
