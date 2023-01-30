def main():
    n = int(input())
    heights = list(map(int, input().split()))

    best_h = 0
    lowest_i = -1
    for i in range(n):
        lowest = float('inf')
        for j in range(i,n):
            lowest = min(lowest, heights[j])
            tallest = min(heights[i], heights[j])
            best_h = max(best_h, tallest-lowest)
    print(best_h)

if __name__ == "__main__":
    main()