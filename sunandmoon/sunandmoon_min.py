a=lambda:map(int,input().split())
s,t=a()
m,n=a()
for i in range(7000):
 if(s+i)%t==0==(m+i)%n:print(i);break
