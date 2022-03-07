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