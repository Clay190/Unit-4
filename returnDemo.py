#Clay Kynor
#10/18/17
#returnDemo.py - Learning how to use return

from random import randint

def randevenint(low,high):
    num = randint(low,high)
    while num%2 == 1: #while the number is odd
        num = randint(low,high)
    return num
    
r1 = randevenint(1,100)
r2 = randevenint(1,100)
r3 = randevenint(1,100)
print(r1, r2, r3)