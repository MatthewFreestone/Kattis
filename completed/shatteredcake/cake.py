w = int(input())
n = int(input())
a = 0
for _ in range(n):
	wi,li = map(int, input().split())
	a+= wi*li
print(int(a/w));
