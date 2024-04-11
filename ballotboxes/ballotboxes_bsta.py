# Rating: ~ 4.1 / 10
from sys import stdin

def check_feasible(cities, max_pop, boxes):
    rem_boxes = boxes
    for i in cities:
        q,r = divmod(i, max_pop)
        rem_boxes -= q + min(1, r)
        if rem_boxes < 0:
            return False
    return True

def main():
    input = lambda: stdin.readline().strip()
    answers = []
    while True:
        n,b = map(int,input().split())
        if n == -1 == b:
            break
        cities = []
        for _ in range(n):
            p = int(input())
            cities.append(p)

        # better chance of check_feasible returning faster
        cities.sort(reverse=True)
        l,r = 0, 5_000_000
        while (l+1) < r:
            m = (l+r) // 2
            valid = check_feasible(cities, m, b)
            if valid:
                # could maybe do more people
                r = m
            else:
                l = m
        out = r if check_feasible(cities, r, b) else l
        answers.append(out)
        input()
    print(*answers, sep="\n")
if __name__ == "__main__":
  main()
