in_str = input()
a_wins = 0
b_wins = 0
win_scenarios = []
for i, c in enumerate(in_str):
    if c == 'A':
        a_wins += 1
    else:
        b_wins += 1
    if (a_wins - b_wins) > 0:
        if not win_scenarios or win_scenarios[-1] != a_wins:
            win_scenarios.append(a_wins)
print(len(win_scenarios))
print(*win_scenarios, sep=' ')