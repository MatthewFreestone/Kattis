from bisect import bisect_left
items = [5,12,1,3,2,11,7,8,9,10,6,4]
items.sort()

def binary_search(items, target):
    i = bisect_left(items, target)
    if i != len(items) and items[i] == target:
        return i
    return -1
print(binary_search(items, 5))