def main():
    # n=5
    n = int(input()) 
    board = input()
    b = lambda x,y : board[y*n + x]
    desired_word = "ICPCASIASG"
    inboard = lambda x,y: 0 <= x < n and 0 <= y < n
    def neighbors(x,y):
        around = [(1,2), (1,-2), (-1,2), (-1,-2), (2, 1), (-2,1), (2,-1), (-2,-1)]
        return ((x+x0, y+y0) for (x0,y0) in around if inboard(x+x0, y+y0))

    def dfs(pos, letter_index):
        if letter_index == len(desired_word)-1:
            print("YES")
            quit()
        x,y = pos
        for x0,y0 in neighbors(x,y):
            if desired_word[letter_index+1] == b(x0,y0):
                dfs((x0,y0), letter_index+1)
    i_pos = []
    for x in range(n):
        for y in range(n):
            if b(x,y) == 'I':
                dfs((x,y), 0)
    
    print("NO")


if __name__ == "__main__":
    main()