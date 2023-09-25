def main():
    n,dirs = input().split(' ')
    n = int(n)
    tree = range(2**(n+1))[::-1]
    index = 0

    for d in dirs:
        if d == "L":
            index = index*2 + 1
        if d == "R":
            index = index*2 + 2
    print(tree[index])


if __name__ == "__main__":
    main()
