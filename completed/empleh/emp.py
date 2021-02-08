white = input().split(':')[1][1:];
black = input().split(':')[1][1:];

whitePeices = white.split(',')
getPeices = {}
for peice in whitePeices: #upper case
	if (len(peice) == 3):
		getPeices[peice[1:]] = peice[0].upper()
	else:
		getPeices[peice] = 'P'
blackPeices = black.split(',')
for peice in blackPeices: #upper case
	if (len(peice) == 3):
		getPeices[peice[1:]] = peice[0].lower()
	else:
		getPeices[peice] = 'p'



switch = {
			0:'a',
			1:'b',
			2:'c',
			3:'d',
			4:'e',
			5:'f',
			6:'g',
			7:'h',
		}

filler = '.';
for r in range(8):
	print("+---+---+---+---+---+---+---+---+")
	line = ""
	for c in range(8):
		line += '|'
		line += filler; 

		coord = switch.get(c, 'z')
		coord += str(8-r)
		line += getPeices.get(coord,filler)

		line += filler; 
		filler = ':' if (filler == '.') else '.'
	line += '|'
	print(line)
	filler = ':' if (filler == '.') else '.'
print("+---+---+---+---+---+---+---+---+")

		
