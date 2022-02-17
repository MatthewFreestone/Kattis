# most java-like solution
index = 0
ans = 0
while index < 100:
	ans += index
	index += 1
print(ans)


ans = 0
for i in range(100):
	ans += i
print(ans)

ans = sum(range(100))