winner = 0;
winnerPts = -1;
i = 1;
for _ in range(5):
	t = sum(map(int,input().split()))
	if (t > winnerPts):
		winnerPts = t
		winner = i
	i+=1
print(winner, winnerPts)
