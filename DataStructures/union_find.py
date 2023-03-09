items = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def find(x):
    if items[x] == x:
        return x
    items[x] = find(items[x])
    return items[x]

def union(x, y):
    items[find(x)] = find(y)

# to combine two sets, union an element from each set
union(1, 5)
print(find(5), find(1))