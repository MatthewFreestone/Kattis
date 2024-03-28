import random
import os
import tqdm
N = 10
FILENAME = 'fuzz.in'
if os.path.exists(FILENAME): os.remove(FILENAME)
for _ in tqdm.tqdm(range(N)):
    # num = random.randint(1, 1500) # can go to 2k
    num = 1000
    values = [random.randint(1, 15) for _ in range(num)]
    weights = [random.randint(1, 15) for _ in range(num)]
    # max_weight = max(2000, int(random.random() * sum(weights)))
    max_weight = 2000
    with open(FILENAME, 'a') as f:
        f.write(f"{max_weight} {num}\n")
        for v, w in zip(values, weights):
            f.write(f"{v} {w}\n")
