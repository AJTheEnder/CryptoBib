from sage.all import * 

factorielTest = sage.all.factorial(9)

matriceTestA = sage.all.matrix(4, 4)
for x in range(4) :
    for y in range(4) :
        matriceTestA[x, y] = hex(x + y)
matriceTestB = sage.all.matrix([[5, 6, 1], [0, 0, 4], [3, 4, 2], [0, 1, 5]])

hexConvert = 89

moduloTest = sage.all.mod(30, 5)
a = 10
b = 2
c = a // b

print(factorielTest)
print(matriceTestA)

#print(matriceTestA * matriceTestB)
print(moduloTest)
print(c)
