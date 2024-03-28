modulus = len(input().split())
n = int(input())
names = [input() for _ in range(n)]
removed = 0
team1 = []
team2 = []
team1Turn = True
count = 0
i = 0
while removed < n:
    # i = (i+1)%n
    if names[i] is not None:
        count += 1
    # print(i, count)

    if count != 0 and (count+1) % modulus == 0:
        if team1Turn:
            team1.append(names[i])
        else:
            team2.append(names[i])
        names[i] = None
        team1Turn = not team1Turn
        removed += 1
        count = 0
        if removed < n:
            while names[i] is None:
                i = (i+1)%n
        # print(removed, names)
    else:
        i = (i+1)%n


print(len(team1))
print(*team1, sep='\n')
print(len(team2))
print(*team2, sep='\n')
