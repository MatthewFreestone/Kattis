
s = int(input())

def generate_random(s):
    res = s + s//13 + 15
    return res

def dist(guess, wump):
    gx, gy = map(int, [c for c in guess])
    wx, wy = map(int, [c for c in wump])
    return abs(gx-wx) + abs(gy-wy)

wumpuseses = set()
while len(wumpuseses) < 4:
    s =  generate_random(s)
    wumpuseses.add(str(s)[-2:])
score = 0
while c := input():
    score += 1
    if c in wumpuseses:
        print("You hit a wumpus!")
        wumpuseses.remove(c)
    if not wumpuseses:
        print(f"Your score is {score} moves.")
        exit()
    min_dist = float('inf')
    for w in wumpuseses:
        min_dist = min(min_dist, dist(c, w))
    print(min_dist)
