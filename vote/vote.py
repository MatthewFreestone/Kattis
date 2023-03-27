from collections import Counter
t = int(input())
for _ in range(t):
    n = int(input())
    votes = [int(input()) for _ in range(n)]
    most_votes = max(votes)
    if most_votes / sum(votes) > .50:
        winner = votes.index(most_votes)
        print(f"majority winner {winner+1}")
    elif Counter(votes)[most_votes] != 1:
        # max votes occured at least twice
        print("no winner")
    else:
        winner = votes.index(most_votes)
        print(f"minority winner {winner+1}")