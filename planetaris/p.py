def main():
    _, total_ships = map(int, input().split())
    ans = 0
    beat_ships = sorted([int(a)+1 for a in input().split()], reverse=True)
    # print(beat_ships)
    while(beat_ships and total_ships - beat_ships[-1] >= 0):
        total_ships -= beat_ships.pop()
        ans += 1
    print(ans)
if __name__ == "__main__":
    main()