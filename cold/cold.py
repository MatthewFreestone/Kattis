_ = input()
res = len(list(filter(lambda x: x < 0, map(int, input().split(' ')))))
print(res)