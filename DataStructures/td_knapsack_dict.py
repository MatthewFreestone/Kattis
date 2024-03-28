from functools import cache
weights = [3, 9, 7, 9, 8, 8, 6, 8, 6, 7, 8, 5, 3, 9, 8, 8, 7, 4, 6, 4,1,2,3]
values = [8, 3, 5, 7, 3, 8, 3, 8, 8, 4, 6, 4, 6, 3, 8, 3, 8, 3, 6, 9,1,2,3]
MAX_W = 90

@cache
def dp(idx, remW):
    if idx == len(weights) or remW == 0: return 0
    if weights[idx] > remW: 
        ans = dp(idx + 1, remW)
        return ans
    ans = max(dp(idx+1, remW), 
               values[idx] + dp(idx + 1, remW - weights[idx])) # take it
    return ans

print(dp(0, MAX_W))
