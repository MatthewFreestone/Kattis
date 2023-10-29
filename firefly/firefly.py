# Rating: ~ 3.6 / 10
# Link: https://open.kattis.com/problems/firefly
from bisect import bisect_left, bisect_right
def main():
    n,h = map(int,input().split())
    ground = []
    ceiling = []
    for i in range(n):
        s = int(input())
        if i % 2 == 1:
            ceiling.append(s)
        else:
            ground.append(s)
    ground.sort()
    ceiling = sorted([h - i for i in ceiling])
    def countHits(level):
        # the obstacles below us are left, taller than us are right
        l = bisect_right(ground, level)
        hits = len(ground) - l

        # the obstacles above us are right, hanging lower than us are left
        u = bisect_right(ceiling, level)
        hits += u
        return hits
    best = 1e6
    best_count = 0
    for i in range(h):
        c = countHits(i)
        if c < best:
            best = c
            best_count = 1
        elif c == best:
            best_count += 1

    print(best, best_count)





if __name__ == "__main__":
    main()
