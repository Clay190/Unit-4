#Clay Kynor
#10/23/17
#traingle.py - find out the areadof a triangle

from math import sqrt

x1 = float(input("Enter your first x1 "))
y1 = float(input("Enter your first y1 "))
x2 = float(input("Enter your first x2 "))
y2 = float(input("Enter your first y2 "))
x3 = float(input("Enter your first x3 "))
y3 = float(input("Enter your first y3 "))

def distance(x1,y1,x2,y2):
    return sqrt((x2-x1)**2 + (y2-y1)**2)

a = distance(x1,y1,x2,y2,)
b = distance(x1,y1,x3,y3)
c = distance(x2,y2,x3,y3)
s = (1/2)*(a+b+c)

print(sqrt(s*(s-a)*(s-b)*(s-c)))