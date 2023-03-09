n, l, h  = map(int,input().split())
profits = [int(input()) for _ in range(n)]
left = [profits[0]]
for i in range(1, n):
    left.append(left[-1] + profits[i])
get_range = lambda s,e: left[e] - (left[s-1] if s-1 >= 0 else 0)

min_profitable = float('inf')
max_profitable = 0
for curr_k in range(l, h+1):
    for start_delay in range(0,curr_k):
        profitable = 0 
        if start_delay != 0:
            # print("start:", 0, start_delay-1)
            first = get_range(0, start_delay-1)
            if first > 0:
                profitable += 1
        passes = (n - start_delay) // curr_k
        # print(f"{curr_k=} {start_delay=} {passes=}")
        profits = []
        for i in range(passes):
            start, end = i*curr_k + start_delay, (i+1)*curr_k + start_delay - 1
            # print(start, end)
            profits.append(get_range(start, end))
        last_start = passes*curr_k + start_delay
        if last_start <= n-1:
            # print("end:", last_start, n-1)
            profits.append(get_range(last_start, n-1))
        # print()

        profitable += sum([(1 if p > 0 else 0) for p in profits])
        max_profitable = max(max_profitable, profitable)
        min_profitable = min(min_profitable, profitable)
print(f"{min_profitable} {max_profitable}")
