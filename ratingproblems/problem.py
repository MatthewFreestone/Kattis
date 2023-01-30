n, k = map(int,input().split())
judges = [-5] * n
for i in range(k):
	curr = int(input())
	judges[i] = curr

worst = list([judges[i] if judges[i] != -5 else -3 for i in range(len(judges))])
best = list([judges[i] if judges[i] != -5 else 3 for i in range(len(judges))])

print(sum(worst)/len(worst), sum(best)/len(best))
