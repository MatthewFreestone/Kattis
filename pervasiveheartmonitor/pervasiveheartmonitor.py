# Rating: ~ 1.8 / 10
# Link: https://open.kattis.com/problems/pervasiveheartmonitor
from sys import stdin
def main():
    for line in stdin:
        tokens = line.strip().split()
        name = []
        non_name_count = 0
        heartrate_total = 0
        for t in tokens:
            if t[0].isalpha():
                name.append(t)
            else:
                heartrate_total += float(t)
                non_name_count += 1
        print(f"{heartrate_total/non_name_count} {' '.join(name)}")
if __name__ == "__main__":
  main()
