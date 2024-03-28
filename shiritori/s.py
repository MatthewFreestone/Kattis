n  = int(input())
words = [input() for _ in range(n)]
isPlayerOne = False
usedWords = set()
currentWord = words[0]
gameLost = False

for i in range(1,n):
    lastWord = currentWord
    usedWords.add(lastWord)
    currentWord = words[i]

    if currentWord in usedWords or lastWord[-1] != currentWord[0]:
        if isPlayerOne:
            print("Player 1 lost") 
            gameLost = True
            break
        else:
            print("Player 2 lost")
            gameLost = True
            break
    isPlayerOne = not isPlayerOne

if (not gameLost):
    print('Fair Game')