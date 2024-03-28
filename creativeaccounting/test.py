n, l, h = input().split()
n = int(n)
l = int(l)
h = int(h)

days = []
for _ in range(n):
    days.append(int(input()))

prefix = [days[0]]
for i in range(1, len(days)):
    new_val = days[i] + prefix[i-1]
    prefix.append(new_val)

print(prefix)