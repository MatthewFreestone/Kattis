def main():
    input()
    a = map(int,input().split())
    total = 1
    last = float('inf')
    for v in a:
        if v > last:
            total += 1
            last = float('inf')
        last = v
    print(total)

        

if __name__ == "__main__":
    main()