def main():
    n = int(input())
    for _ in range(n):
        dir, D, H, M = input().split()
        D, H, M = map(int, (D,H,M)) 
        if D == 0:
            print(H,M)
            continue
        if dir == "B": #back
            changeM = M - D
            if changeM <= 0:
                H -= (-changeM) // 61 + 1
            newM = changeM % 60
            print(H % 24, newM)
        else:
            changeM = M + D
            if changeM >= 60:
                H += changeM // 60
            newM = changeM % 60
            print(H % 24, newM)


if __name__ == "__main__":
    main()