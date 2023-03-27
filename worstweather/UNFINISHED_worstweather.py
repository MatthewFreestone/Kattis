from sys import stdin

imp = lambda: stdin.readline().strip().split()
while True:
    n = int(stdin.readline().strip())
    inputs = []
    if n == 0:
        exit()
    for _ in range(n):
        year, rain_amount = map(int, imp())
        inputs.append((year, rain_amount))
    inputs.sort()
    inputs = {year: value for year, value in inputs}
    YEAR_OFFSET = inputs[0][0]
    tree = [-1] * (4*n)
    def build_max_st(left=0, right=n-1, c=0):
        if left == right:
            tree[c] = inputs[left][1]
        else:
            middle = (left + right) // 2
            build_max_st(left, middle, 2*c+1)
            build_max_st(middle+1, right, 2*c+2)
            tree[c] = max(tree[2*c+1], tree[2*c+2])
    build_max_st()
    print(tree)
    def query_max_st(ql, qr, left=0, right=n-1, c=0):
        if ql > right or qr < left:
            return -1
        if ql >= left and qr <= right:
            return tree[c]
        middle = (left+right) // 2
        return max(query_max_st(ql, qr, left, middle, 2*c+1),
                   query_max_st(ql, qr, middle+1, right, 2*c+2))

    m = int(stdin.readline())
    for _ in range(m):
        x,y = map(int, imp())
        x,y = x-YEAR_OFFSET, y-YEAR_OFFSET
        print(x,y, end='\t')
        print(query_max_st(x,y))
    # Get rid of white space
    stdin.readline()
# input()
# for line in stdin:
#     year, rain_amount = map(int, line.strip().split())
#     inputs.append((year, rain_amount))
# inputs.sort()
# print(inputs)