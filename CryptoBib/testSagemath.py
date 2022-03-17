from sage.all import * 
import arithmetiqueRSA as arithmetic
import RSA

print('')
factorielTest = sage.all.factorial(9)
print(factorielTest)

print('')
matriceTestA = sage.all.matrix(4, 4)
for x in range(4) :
    for y in range(4) :
        matriceTestA[x, y] = x + y
print(matriceTestA)

print('')
matriceTestB = sage.all.matrix([
    [5, 6, 1], 
    [0, 0, 4], 
    [3, 4, 2], 
    [0, 1, 5]])
print(matriceTestA * matriceTestB)

print('')
sousMatriceB = sage.all.matrix(matriceTestB.column(2))
print('')
print(type(sousMatriceB))
print(sousMatriceB)

print('')
moduloTest = sage.all.mod(30, 5)
print(moduloTest)

print('')
a = 10
print(bin(a))
print(type(bin(a)))
b = 2
c = a // b
print(c)

print('')
str1 = ''
str2 = 'e'
print(str1 + str2)
str3 = 'b'
str4 = str3 + str2
print(str4)

print('')
liste = [0, 1, 2, 3, 4, 5]
liste.append(liste.pop(liste[1]))
print(liste)

print('')
print(chr(96))

print('')
print(hex(1))

print('')
result = arithmetic.bezoutEquation(277, 32040)
print(result)

print('')
keyRSA = RSA.CleRSA()
keyRSA.calculPhiN(179, 181)
print('n = ', keyRSA.n, ', Phi(n) = ', keyRSA.PhiN)
keyRSA.chooseExponent(277)
print('e = ', keyRSA.exponent)
keyRSA.calculPublicKey()
print('publicKey(n and e) = ', keyRSA.publicKey)
keyRSA.calculPrivateKey()
print('privateKey(d = inverse of exponent modulo Phi(n)) = ', keyRSA.privateKey)

n = (179 - 1) * (181 - 1)
print(n)
print(arithmetic.pgcd(n, 277))

print('')
strNum = '69'
numStrNum = int(strNum)
print(type(numStrNum), ' : ', numStrNum)

print('')
print(arithmetic.isPrime(10))
print(arithmetic.isPrime(7))