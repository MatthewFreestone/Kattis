n, k = map(int,input().split())
queries = []
for _ in range(k):
    q, *p = input().split()
    if q == 'F':
        queries.append(('F', int(p[0]) - 1))
    elif q == 'C':
        l, r = map(int, p)
        queries.append(('C', (l-1, r-1)))
tree = [0] * (4*n)
# no need to build tree, it's initialized at 0

def update_st(index, left=0, right=n-1, c=0):
    if left == right == index:
        tree[c] = (tree[c] + 1) % 2
    else:
        middle = (left + right) // 2
        if index <= middle:
            update_st(index, left, middle, 2*c+1)
        else:
            update_st(index, middle+1, right, 2*c+2)
        tree[c] = tree[2*c+1] + tree[2*c+2]

def query_st(query_left, query_right, left=0, right=n-1, c=0):
    if right < query_left or left > query_right:
        return 0
    elif left >= query_left and right <= query_right:
        return tree[c]
    else:
        middle = (left + right) // 2
        return query_st(query_left, query_right, left, middle, 2*c+1) + \
              query_st(query_left, query_right, middle+1, right, 2*c+2)
    
for action, params in queries:
    if action == 'F':
        update_st(params)
    else:
        print(query_st(*params))  
