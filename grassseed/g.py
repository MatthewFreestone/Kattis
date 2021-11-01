def main():
    c = float(input())
    n = int(input())
    t = 0
    for _ in range(n):
        w,l = map(float,input().split(' '))
        t += (w*l*c)
    print(t)

if __name__ == "__main__":
    main()