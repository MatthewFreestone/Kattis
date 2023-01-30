

def value(number, dominant):
	if (dominant):
		switch = {
		'A' : 11,
		'K' : 4,
		'Q' : 3,
		'J' : 20,
		'T' : 10,
		'9' : 14,
		'8' : 0,
		'7' : 0
		}
	else:
		switch = {
		'A' : 11,
		'K' : 4,
		'Q' : 3,
		'J' : 2,
		'T' : 10,
		'9' : 0,
		'8' : 0,
		'7' : 0
		}

	return switch.get(number, -9999); 
	


n, dom = input().split(' ')

total = 0
for _ in range(4*int(n)):
	inp = input()
	card = inp[0]
	suit = inp[1]
	#card, suit = input().split('');
	total += value(card, suit == dom)

print(total)
