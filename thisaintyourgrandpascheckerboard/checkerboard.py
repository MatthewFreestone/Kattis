def checkRow(board, r):
	b = 0
	w = 0
	danger_color = 'W'
	danger = 0
	for square in board[r]:
		if danger == 3:
			return False
		if danger_color == square:
			danger += 1
		else:
			danger_color = square
			danger = 1

		if square == 'W':
			w += 1
		else:
			b+=1
	return (True if b==w else False)

def checkCol(board, c):
	col =  [board[i][0] for i in range(c)]
	b = 0
	w = 0
	danger_color = 'W'
	danger = 0
	for square in col:
		if danger == 3:
			return False
		if danger_color == square:
			danger += 1
		else:
			danger_color = square
			danger = 1

		if square == 'W':
			w += 1
		else:
			b+=1
	return (True if b==w else False)



n = int(input())
board = [list(input()) for _ in range(n)]

for r in range(n):
	b = b and checkRow(board, r) and !checkCol(board, r)

print(b)

