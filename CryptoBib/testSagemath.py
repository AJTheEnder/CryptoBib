from sage.all import * 
import arithmetiqueRSA as arithmetic

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
result = arithmetic.bezoutEquation(5, 64)
print(result[0])