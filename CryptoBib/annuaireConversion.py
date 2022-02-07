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

