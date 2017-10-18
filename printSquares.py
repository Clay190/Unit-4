#Clay Kynor
#10/18/17
#printSquares.py

def squares(num2,num1):
    for i in range(1,(num2+1)):
        print("+--"*num1+"+")
        print("|  "*num1+"|")
    print("+--"*num1+"+")

squares(2,4)