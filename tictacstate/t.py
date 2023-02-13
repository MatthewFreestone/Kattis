n = int(input())
for _ in range(n):
    # convert to base 10 int
    int_inp = int(input(), 8)
    # conver to binary and throw out b'turn'
    bits = list(bin(int_inp)[2:])
    if len(bits) < 18:
        bits = ['0'] * (18-len(bits)) + bits
    elif len(bits) == 19:
        _, *bits = bits
    bits = list(map(int, bits))
    bits.reverse()
    # print(bits)
    # print(list(range(10)) + list(range(8)))
    def check_winner(bits):
        # left and right:
        for i in range(0,7,3):
            if all([bits[i], bits[i+1], bits[i+2]]):
                if not any([bits[9+i], bits[9+i+1], bits[9+i+2]]):
                    return "O wins"
                elif all([bits[9+i], bits[9+i+1], bits[9+i+2]]):
                    return "X wins"
        # up and down
        for i in range(3):
            if all([bits[i], bits[i+3], bits[i+6]]):
                if not any([bits[9+i], bits[9+i+3], bits[9+i+6]]):
                    return "O wins"
                elif all([bits[9+i], bits[9+i+3], bits[9+i+6]]):
                    return "X wins"

        # diagonals
        if all([bits[0], bits[4], bits[8]]):
            if not any([bits[9], bits[13], bits[17]]):
                return "O wins"
            elif all([bits[9], bits[13], bits[17]]):
                return "X wins"
        if all([bits[2], bits[4], bits[6]]):
            if not any([bits[11], bits[13], bits[15]]):
                return "O wins"
            elif all([bits[11], bits[13], bits[15]]):
                return "X wins"

        for i in range(9):
            if not bits[i]:
                return "In progress"
        return "Cat's"

    print(check_winner(bits))

    # chunks = [''.join(bits[i:i+3]) for i in range(0, len(bits), 3)] 
    
    # print(bits)

    '''
    O|X|X
    X|O|O
    X|O|O
    
    X|X|X
    O|O|   ? 
     | |
    
    '''