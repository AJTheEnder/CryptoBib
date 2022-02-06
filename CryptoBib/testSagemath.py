from sage.all import *

factorielTest = sage.all.factorial(9)

matriceTestA = sage.all.matrix([[1, 2, 3], [3, 2, 1], [5, 0, 2]])
matriceTestB = sage.all.matrix([[5, 6, 1], [0, 0, 4], [3, 4, 2]])

moduloTest = sage.all.mod(30, 5)

print(factorielTest)
print(matriceTestA * matriceTestB)
print(moduloTest)