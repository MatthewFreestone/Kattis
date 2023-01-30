n, m = map(int,input().split())
unread = list([0 for i in range(n)])
for _ in range(m):
	send = int(input()) - 1
	for i in range(len(unread)):
		unread[i] += 1
	unread[send] = 0
	print(sum(unread))


