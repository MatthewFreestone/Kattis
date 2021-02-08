n,h,v = input().split(' ')
n = int(n)
h = int(h)
v = int(v)
nh = n-h
nv = n-v
print(4*max(h*v, h*nv, v*nh, nv*nh))