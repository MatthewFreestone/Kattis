import math
h,v = map(int, input().split())
'''
  |\
  | \
  |  \ ?
h |   \
  |  v \
  |_____\

sin(v) = opposite/hypot = h/?
? = h / sin(v)
'''
rad_v = v * (math.pi / 180) 
length = h / math.sin(rad_v)
print(math.ceil(length))