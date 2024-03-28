#https://open.kattis.com/problems/nodup
s = input().split(' ')
set_version = set(s)
if len(s) == len(set_version):
    print("yes")
else:
    print("no")

s = input().split(' ')
for i, c1 in enumerate(s):
    for j, c2 in enumerate(s):
        if i == j:
            continue
        if c1 == c2:
            print("no")
            exit()
print("yes")


