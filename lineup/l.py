def main():
    n = int(input())
    names = [input() for _ in range(n)]
    sortedList = sorted(names)
    if sortedList == names:
        print("INCREASING")
    elif sortedList[::-1] == names:
        print("DECREASING")
    else:
        print("NEITHER")

if __name__ == "__main__":
    main()