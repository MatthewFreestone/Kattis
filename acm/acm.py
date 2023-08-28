# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/acm
import sys
from collections import defaultdict as dd
def main():
    scores = dd(int)
    solved = set()
    correct = 0
    for line in sys.stdin:
        if line.strip() == '-1':
            break
        time, problem, judge = line.strip().split()
        time = int(time)
        judge = judge == 'right'
        if not judge:
            scores[problem] += 20
        else:
            scores[problem] += time
            solved.add(problem)
            correct += 1
    total_time = sum((scores[s] for s in solved))
    print(f"{correct} {total_time}")



if __name__ == "__main__":
  main()
