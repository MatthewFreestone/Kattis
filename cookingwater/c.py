def main():
    n = int(input())
    a_start = -1
    a_end = 10000
    for _ in range(n):
        s,e = map(int,input().split())
        a_start = max(a_start, s)
        a_end = min(a_end, e)
        if (a_end < a_start):
            print('edward is right')
            return
    print('gunilla has a point')
    

if __name__ == "__main__":
    main()