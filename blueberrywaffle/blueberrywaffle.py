# Rating: ~ 1.3 / 10
# Link: https://open.kattis.com/problems/blueberrywaffle

def main():
  r, f  = map(int, input().split())
  final_rot = (180 * (f/r)) % 360
  print("down") if 90 < abs(final_rot) < 270 else print("up")


if __name__ == "__main__":
  main()
