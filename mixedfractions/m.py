def main():
    while True:
        n,m = map(int,input().split())
        if n == 0 and m == 0:
            break
        w = n // m
        r = n % m
        print(f"{w} {r} / {m}")


if __name__ == "__main__":
    main()