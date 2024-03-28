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
        for i in range(n): memo[i][0] = 0
        for w in range(c): memo[0][w] = 0

        for id in range(n):
            for cw in range(c):

                


if __name__ == '__main__':
    main()
