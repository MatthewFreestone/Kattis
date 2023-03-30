from sys import stdin
n, k = map(int, input().split())

tree = [0] * (4*n)

def update(index, left=0, right=n-1, c=0):
    if left == right == index:
        tree[c] = int(not bool(tree[c]))
    else:
        middle = (left + right) // 2
        if index <= middle:
            update(index, left, middle, 2*c+1)
        else:
            update(index, middle+1, right, 2*c+2)
        tree[c] = tree[2*c+1] + tree[2*c+2]
        
def query_tree(query_left, query_right, left=0, right=n-1, c=0):
    if query_left > right or query_right < left:
        return 0
    if query_left <= left and query_right >= right:
        return tree[c]
    middle = (left + right) // 2
    return query_tree(query_left, query_right, left, middle, c*2+1) + \
               query_tree( query_left, query_right, middle+1, right, c*2+2)

for line in stdin:
    q, *params = line.split()
    if q == 'F':
        i = int(params[0]) - 1
        update(i)
    else:
        l, r = map(int, params)
        res = query_tree(l-1, r-1)
        print(res)