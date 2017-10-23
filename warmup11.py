#Clay Kynor
#10/23/17
#warmup11.py - determinds prime numbers

def isPrime(num1):
    for i in range(2,(num1)):
        if num1%i==0:
            return print("False")
        else:
            return print("True")

isPrime(3)
