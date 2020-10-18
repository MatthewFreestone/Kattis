#! /usr/bin/python3
import sys
dictionary = dict()
for i in sys.stdin:
    if (i == '\n'):
        break
    eng, foreign = i.split(' ')
    dictionary[foreign] = eng
    

for i in sys.stdin:
    if i in dictionary:
        print(dictionary[i])
    else:
        print("eh")
            
