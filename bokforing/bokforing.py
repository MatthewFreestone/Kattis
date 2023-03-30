# on leaderboard for shortness, but pretty unreadable lol
from sys import stdin as s
input()
b=0
m={}
for l in s:
    c,*p=l.split()
    if c=="SET":
        n,v=map(int, p)
        m[n]=v
    elif c[0]=="P":
        n = int(p[0])
        print(m.get(n,b))
    else:
        b=int(p[0])
        m={}
