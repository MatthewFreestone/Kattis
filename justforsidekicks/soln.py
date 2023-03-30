from sys import stdin
from pprint import pprint

n, q = map(int, input().split())
values = list(map(int, input().split()))
array = [int(a) for a in input()]
# print(array)
tree = [[0,0,0,0,0,0] for _ in range(4*n)]
def sum_vals(first,second):
    res = [0,0,0,0,0,0]
    for i in range(6):
        res[i] = first[i] + second[i]
    return res

def build_tree(left, right, c):
    if left == right:
        val = [0,0,0,0,0,0]
        val[array[left]-1] = 1
        tree[c] = val
    else:
        middle = (left + right) // 2
        build_tree(left, middle, 2*c+1)
        build_tree(middle+1, right, 2*c+2)
        left_tree, right_tree = tree[2*c+1], tree[2*c+2]
        tree[c] = sum_vals(left_tree, right_tree)

def query_tree(query_left, query_right, left=0, right=n-1,c=0):
    if left > query_right or right < query_left:
        return [0,0,0,0,0,0]
    if left >= query_left and right <= query_right:
        return tree[c]
    middle = (left + right) // 2
    left_tree = query_tree(query_left, query_right, left, middle, 2*c+1)
    right_tree = query_tree(query_left, query_right, middle+1, right, 2*c+2)
    return sum_vals(left_tree, right_tree)

def update_tree(index, value, left=0, right=n-1,c=0):
    if left == right == index:
        val = [0,0,0,0,0,0]
        val[value-1] = 1
        tree[c] = val
    else:
        middle = (left + right) // 2
        if index <= middle:
            update_tree(index, value, left, middle, 2*c+1)
        else:
            update_tree(index, value, middle+1, right, 2*c+2)
        left_tree, right_tree = tree[2*c+1], tree[2*c+2]
        tree[c] = sum_vals(left_tree, right_tree)
        
build_tree(0, n-1, 0)
# pprint(tree)
for line in stdin:
    q, p1, p2 = line.strip().split()
    if q == '1':
        k, p = int(p1)-1, int(p2)
        update_tree(k, p)
        # update
    elif q == '2':
        p, v = int(p1), int(p2)
        values[p-1] = v
    else:
        l, r = int(p1)-1, int(p2)-1
        res = query_tree(l, r)
        # print(l,r, res)
        val = 0
        for i in range(6):
            val += values[i] * res[i]
        print(val)
        #query