#Clay Kynor
#10/16/17
#functionDemo.py - learning functions

def hw():
    print("Hellow, world!")

"""
hw() #actually runs the function"""

def bigger(num1, num2): #prints which number is bigger
    if num1 > num2:
        print(num1)
    else:
        print(num2)
        
#bigger(13,15)
#bigger(-10,-192)
#bigger("Clay", "Pedro")

def slope(x1,y1,x2,y2): #calculate slope
    print((y2-y1)/(x2-x1))
    
slope(1,2,2,4)