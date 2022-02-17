def main():
    n = int(input())
    for _ in range(n):
        input()
        stores = sorted(list(map(int, input().split())))
        # print(stores)
        dist = 0
        for i,v in enumerate(stores):
            if i == len(stores) - 1:
                continue
            else:
                dist += stores[i+1]-v
        print(dist)

if __name__ == "__main__":
    main()