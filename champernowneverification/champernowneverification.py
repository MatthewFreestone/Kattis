r=range
try:
 print([''.join(map(str,r(1,i+1))) for i in r(1,11)].index(input())+1)
except:
 print(-1)
