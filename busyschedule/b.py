def main():
    n = int(input())
    while(n):
        times = []
        for _ in range(n):
            raw = input()
            t,ampm = raw.split()
            h,m = map(int,t.split(":"))
            if h == 12:
                h = 0
            if ampm == "p.m.":
                h += 12
            times.append((h*100+m,raw))
        times.sort()
        for _,t in times:
            print(t)
        print() # newline
        n = int(input())


if __name__ == "__main__":
    main()