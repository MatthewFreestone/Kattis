n = int(input())
input_str = input()
rows = [input_str[n*i:n*(i+1)] for i in range(n)]

# "IXIXX", "XXCXA", "XSXXP", ...
goal = "ICPCASIASG"

moves = ((1,2), (2, 1), (-1,2), (-2, 1), (1,-2), (2, -1), (-1,-2), (-2, -1))

def isvalid(x,y):
	return 0 <= x < n and 0 <= y < n

def dfs(x,y, index_in_goal):
	if index_in_goal == len(goal) - 1:
		print("YES")
		exit(0)

	neighbors = [(x + dx, y+dy) for dx, dy in moves if isvalid(x+dx, y+dy)]
	for new_x, new_y in neighbors:
		if rows[new_x][new_y] == goal[index_in_goal+1]:
			dfs(new_x, new_y, index_in_goal+1)

for x in range(n):
	for y in range(n):
		if rows[x][y] == 'I':
			dfs(x, y, 0)

print("NO")