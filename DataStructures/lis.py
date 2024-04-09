from bisect import bisect_left

a = [-7, 10, 9, 2, 3, 8, 8, 1, 2, 3, 4]

def lis(a):
    current = []
    current_ids = []
    length = 0
    for i, val in enumerate(a):
        pos = bisect_left(current, val)
        if pos == length:
            length += 1
            current.append(val)
            current_ids.append(i)
        else:
            current[pos] = val
            current_ids[pos] = i
    return length
print(lis(a))  # 5

def lis_parents(a):
    current = []
    current_ids = []
    length = 0
    parents = [-1] * len(a)
    lis_end = -1
    for i, val in enumerate(a):
        pos = bisect_left(current, val)
        if pos == length:
            length += 1
            current.append(val)
            current_ids.append(i)
            lis_end = i
        else:
            current[pos] = val
            current_ids[pos] = i
        if pos > 0:
            parents[i] = current_ids[pos - 1]

    lis_path = []
    while lis_end != -1:
        lis_path.append(a[lis_end])
        lis_end = parents[lis_end]
    return length, lis_path[::-1]

print(lis_parents(a))  # (5, [-7, 1, 2, 3, 4])