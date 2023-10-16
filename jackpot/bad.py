import math
from math import prod

machine = int(input())


for i in range(machine):
    wheels = int(input())
    
    often = [*map(int, input().split())]
    #"often" has the periodicties of each wheel
    
    g = []
    #"g" keeps track of common divisors that need to be multiplied in the end to find the LCM

    for j in range(wheels-1):
        for k in range(j+1, wheels):
            gd = math.gcd(often[j], often[k])
            g.append(gd)
            #finding a common divisor
            
            often[j] //= gd
            for l in range(k, wheels):
                often[l] //= math.gcd(often[l], gd)
            #dividing these numbers and every number to the right by that divisor (if divisible) so it's not recounted
        
    # print(often, g)

    product = prod(g)
    #multiply for each divisor
    
    for j in range(len(often)):
        if(often[j] != 1):
            product*=often[j]
    #multiply for the numbers who don't share any more divisors 
    #with other numbers (relatively prime) but aren't equal to 1
            
    if product > 1e9:
        print("More than a billion.")
        
    else:
        print(int(product))
    