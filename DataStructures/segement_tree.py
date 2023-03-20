from pprint import pprint
a = [8,1,3,9,5,7, 10]

# naive approach
def get_min(left, right):
    return min(a[left:right+1])
def get_sum(left, right):
    return sum(a[left:right+1])

prefix_sum = [a[0]]
for i in range(1, len(a)):
    prefix_sum.append(prefix_sum[-1] + a[i])
# print(prefix_sum)

def get_sum(left, right):
    if left == 0:
        return prefix_sum[right]
    return prefix_sum[right] - prefix_sum[left-1]

print("Prefix Summing")
print(a[0:4], get_sum(0, 3))
print(a[4:7], get_sum(4, 6), end='\n\n')

n = len(a)
min_dp = [[float('inf') for _ in range(n)] for _ in range(n)]
for i in range(n):
    min_dp[i][i] = a[i]
for i in range(n):
    for j in range(i+1, n):
        min_dp[i][j] = min(min_dp[i][j-1], a[j])

def get_min(left, right):
    return min_dp[left][right]
print("DP Approach (min)")
print(a[0:4], get_min(0, 3))
print(a[4:7], get_min(4, 6), end='\n\n')

# Segment Tree
tree = [float('inf')] * (4*n)
def build_tree(left, right, c=0):
    if left==right:
        tree[c] = a[left]
        return
    middle = (left+right) // 2
    build_tree(left, middle, c*2+1)
    build_tree(middle+1, right, c*2+2)
    tree[c] = min(tree[2*c+1], tree[2*c+2]) 
build_tree(0, len(a)-1)


def update_tree(index, new_val, left=0, right=len(a)-1, c=0):
    if left == right == index:
        prev = tree[c]
        tree[c] = new_val
        # print(f"Update {c=} {left=} {right=} from {prev} to {tree[c]}")
    else:
        middle = (left + right) // 2
        if index <= middle:
            update_tree(index, new_val, left, middle, 2*c+1)
        else:
            update_tree(index, new_val, middle+1, right, 2*c+2)
        prev = tree[c]
        tree[c] = min(tree[2*c+1], tree[2*c+2])
        # print(f"Update {c=} {left=} {right=} from {prev} to {tree[c]}")
update_tree(index=4, new_val=1)

def query_tree(query_left, query_right, left=0, right=len(a)-1, c=0):
    print(f"Query {c=} {left=} {right=}")
    if query_left > right or query_right < left:
        return float('inf')
    if query_left <= left and query_right >= right:
        return tree[c]
    middle = (left + right) // 2
    return min(query_tree(query_left, query_right, left, middle, c*2+1), \
               query_tree( query_left, query_right, middle+1, right, c*2+2))

print(a[3:7], query_tree(3,6))

build_tree(0, len(a)-1)
a[4] = 1
print(a[3:7], query_tree(3,6))

