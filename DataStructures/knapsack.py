import numpy as np
weights = [2,3,1,9,4,2]
values = [8,3,1,7,3,3]
MAX_W = 20

prev_ans = [[-1]*(1+MAX_W) for _ in range(len(weights))]
def dp(idx, remW):
    if idx == len(weights) or remW == 0: return 0
    ans = prev_ans[idx][remW]
    if ans != -1: return ans
    if weights[idx] > remW: 
        ans = dp(idx + 1, remW)
        prev_ans[idx][remW] = ans
        return ans
    ans = max(dp(idx+1, remW), # leave it 
               values[idx] + dp(idx + 1, remW - weights[idx])) # take it
    prev_ans[idx][remW] = ans
    return ans

print(dp(0, MAX_W))
print(np.array(prev_ans))
