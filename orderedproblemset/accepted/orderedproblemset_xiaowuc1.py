n = int(input())
l = [int(input()) for _ in range(n)]
ret = []
for k in range(2, n+1):
  sz = n // k
  if n%k:
    continue
  lvals = []
  rvals = []
  for i in range(k):
    lvals.append(min(l[i*sz:(i+1)*sz]))
    rvals.append(max(l[i*sz:(i+1)*sz]))
  if all(lvals[i] > rvals[i-1] for i in range(1, k)): ret.append(k)
if not ret: ret.append(-1)
for x in ret: print(x)