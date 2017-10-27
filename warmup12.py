#Clay Kynor
#10/27/17
#warmup12.py

def calc(x,y):
    n=y
    while n>0:
        if x%n == 0 and y%n == 0:
            print(n)
            break
        else:
            n=-1
            
calc(64,24)