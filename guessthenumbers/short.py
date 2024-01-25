from itertools import permutations as p
while 1:
 l=[*map(int,input().split())]
 if l[0]==0:break
 nums=l[1:-1]
 res=l[-1]
 e=input()
 l=[*{a for a in e if a.isalpha()}]
 s=[]
 for c in e:
  if c.isalpha():s.append(f"v['{c}']")
  else:s.append(c)
 py_expr=eval('lambda :' + ''.join(s))
 for combo in p(nums):
  v={l:n for l,n in zip(l,combo)}
  cres=py_expr()
  if cres==res:
    print("YES")
    break
 else:print("NO")
