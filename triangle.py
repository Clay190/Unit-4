#Clay Kynor
#10/23/17
#traingle.py - find out the areadof a triangle

from math import sqrt

def distance(x1,y1,x2,y2,x3,y3):
    a = sqrt((x2-x1)**2 + (y2-y1)**2)
    b = sqrt((x3-x2)**2 + (y3-y2)**2)
    c = sqrt((x1-x3)**2 + (y1-y3)**2)
    return a
    return b
    return c

distance(3,4,3-5,2,-7,1)

print((11/2)*(a+b+c))