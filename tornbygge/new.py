input()
heights = list(map(int, input().split()))
count = 1
for i in range(len(heights) -1):
    if heights[i] < heights[i+1]:
        count += 1

print(count)