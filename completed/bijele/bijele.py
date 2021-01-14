#! /usr/bin/python3
import sys

#for line in sys.stdin:
line = input()
t = line.split()
k = int(t[0])
q = int(t[1])
r = int(t[2])
b = int(t[3])
kn = int(t[4])
p = int(t[5])
print(1-k, 1-q, 2-r, 2-b, 2-kn, 8-p)

    
