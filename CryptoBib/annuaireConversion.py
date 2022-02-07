print("")
helloworldChar = "Hello world"
#============DEPART CHAR============#

#Conversion d'une chaine de caractères à la liste de ses codes ASCII
helloworldCharToASCII = []
for lettre in range(len(helloworldChar)) :
    helloworldCharToASCII.append(ord(helloworldChar[lettre]))
print(helloworldCharToASCII)

#Conversion d'une chaine de caractères en son équivalent binaire (via ASCII)
helloworldCharToBinary = []
for lettre in range(len(helloworldChar)) :
    helloworldCharToBinary.append(format(ord(helloworldChar[lettre]), 'b'))
print(helloworldCharToBinary)

#Conversion d'une chaine de caractères en son équivalent hexadécimal (via ASCII)
helloworldCharToHex = []
for lettre in range(len(helloworldChar)) :
    helloworldCharToHex.append(format(ord(helloworldChar[lettre]), 'x'))
print(helloworldCharToHex)
#===================================#


print("")
helloworldASCII = helloworldCharToASCII
#===========DEPART ASCII============#

#Conversion d'une liste d'int en leur correspondance ASCII (char)
helloworldASCIIToChar = []
for integer in range(len(helloworldASCII)) :
    helloworldASCIIToChar.append(chr(helloworldASCII[integer]))
print(helloworldASCIIToChar)

#Conversion d'une liste d'int en bianaire
helloworldASCIIToBinary = []
for integer in range(len(helloworldASCII)) :
    helloworldASCIIToBinary.append(format(helloworldASCII[integer], 'b'))
print(helloworldASCIIToBinary)

#Conversion d'une liste d'int en hexadécimal
helloworldASCIIToHex = []
for integer in range(len(helloworldASCII)) :
    helloworldASCIIToHex.append(format(helloworldASCII[integer], 'x'))
print(helloworldASCIIToHex)
#===================================#


print("")
helloworldBinary = helloworldCharToBinary
#============DEPART BIN=============#

#Conversion d'une liste de binaires en leur correspondance ASCII (char)
helloworldBinaryToChar = []
for binary in range(len(helloworldBinary)) :
    helloworldBinaryToChar.append(chr(int(helloworldBinary[binary], 2)))
print(helloworldBinaryToChar)

#Conversion d'une liste de binaires en int
helloworldBinaryToASCII = []
for binary in range(len(helloworldBinary)) :
    helloworldBinaryToASCII.append(int(helloworldBinary[binary], 2))
print(helloworldBinaryToASCII)

#Conversion d'une liste de binaires en hexadécimal
helloworldBinaryToHex = []
for binary in range(len(helloworldBinary)) :
    helloworldBinaryToHex.append(format(int(helloworldBinary[binary], 2), 'x'))
print(helloworldBinaryToHex)
#===================================#