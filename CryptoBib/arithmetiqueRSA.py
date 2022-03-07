import math

'''
||==============================================||
||              Arithmetique RSA                ||
||==============================================||
'''

def pgcd(a, b) :
    while(a != b) :
        d = abs(b - a)
        b = a
        a = d
    return d

def bezoutEquation(a, b) :
    if (b == 0) :
        return 1, 0
    else :
        u , v = bezoutEquation(b, a % b)
        return v, u - (a//b) * v
    
def isPrime(n) :
    a = 2
    while (a <= math.sqrt(n)) :
        if (n % a < 1) :
            return False
        a = a + 1
    return True