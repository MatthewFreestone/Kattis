def main():
    n = int(input())
    t = [int(i) for i in input().split(' ')]
    minTemp = 50
    startDay = -1
    for i in range(n-2):
        if max(t[i], t[i+2]) < minTemp:
            minTemp = max(t[i], t[i+2])
            startDay = i
    print(startDay+1, minTemp)

if __name__ == "__main__":
    main()