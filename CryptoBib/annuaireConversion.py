'''
||==============================================||
||         Version Annuaire fonctionnel         ||
||==============================================||
'''

'''
  <<==============Conversion char=============>>
'''
def conversionCharTo(texteChar, typeRetour) :
    
    if (typeRetour == 'c') :
        return texteChar
   
    elif (typeRetour == 'a') :
        texteASCII = []
        for lettre in range(len(texteChar)) :
            texteASCII.append(ord(texteChar[lettre]))
        return texteASCII

    elif (typeRetour == 'b') : 
        texteBin = []
        for lettre in range(len(texteChar)) :
            texteBin.append(format(ord(texteChar[lettre]), 'b'))
        return texteBin
    
    elif (typeRetour == 'h') :
        texteHex = []
        for lettre in range(len(texteChar)) :
            texteHex.append(format(ord(texteChar[lettre]), 'x'))
        return texteHex
    
    else :
        print("ce n'est pas le bon type de retour")
        return texteChar
    
'''
  <<==============Conversion Int==============>>
'''
def conversionASCIITo(texteASCII, typeRetour) :
    
    if (typeRetour == 'c') :
        texteChar = []
        for integer in range(len(texteASCII)) :
            texteChar.append(chr(texteASCII[integer]))
        return texteChar

    elif (typeRetour == 'a') :
        return texteASCII
    
    elif (typeRetour == 'b') :
        texteBin = []
        for integer in range(len(texteASCII)) :
            texteBin.append(format(texteASCII[integer], 'b'))
        return texteBin
    
    elif (typeRetour == 'h') :
        texteHex = []
        for integer in range(len(texteASCII)) :
            texteHex.append(format(texteASCII[integer], 'x'))
        return texteHex
    
    else :
        print("ce n'est pas le bon type de retour")
        return texteASCII
    
'''
  <<==============Conversion Bin==============>>
'''
def conversionBinTo(texteBin, typeRetour) :
    
    if (typeRetour == 'c') :
        texteChar = []
        for binary in range(len(texteBin)) :
            texteChar.append(chr(int(texteBin[binary], 2)))
        return texteChar
    
    elif (typeRetour == 'a') :
        texteASCII = []
        for binary in range(len(texteBin)) :
            texteASCII.append(int(texteBin[binary], 2))
        return texteASCII
    
    elif (typeRetour == 'b') :
        return texteBin
    
    elif (typeRetour == 'h') :
        texteHex = []
        for binary in range(len(texteBin)) :
            texteHex.append(format(int(texteBin[binary], 2), 'x'))
        return texteHex
    
    else :
        print("ce n'est pas le bon type de retour")
        return texteBin
    
'''
  <<==============Conversion Bin==============>>
'''
def conversionHexTo(texteHex, typeRetour) :
    
    if (typeRetour == 'c') :
        texteChar = []
        for hexadecimal in range(len(texteHex)) :
            texteChar.append(chr(int(texteHex[hexadecimal], 16)))
        return texteChar
    
    elif (typeRetour == 'a') :
        texteASCII = []
        for hexadecimal in range(len(texteHex)) :
            texteASCII.append(int(texteHex[hexadecimal], 16))
        return texteASCII
    
    elif (typeRetour == 'b') :
        texteBin = []
        for hexadecimal in range(len(texteHex)) :
            texteBin.append(format(int(texteHex[hexadecimal], 16), 'b'))
        return texteBin
    
    elif (typeRetour == 'a') :
        return texteHex
    
    else :
        print("ce n'est pas le bon type de retour")
        return texteHex
    
 
    
'''
||==============================================||
||                 Zone de test                 ||
||==============================================||
'''

print("")
helloworldChar = "Hello world"
#============DEPART CHAR============#

#Aucune conversion
helloworldCharToChar = conversionCharTo(helloworldChar, 'c')
print(helloworldCharToChar)

#Conversion d'une chaine de caractères à la liste de ses codes ASCII
helloworldCharToASCII = conversionCharTo(helloworldChar, 'a')
print(helloworldCharToASCII)

#Conversion d'une chaine de caractères en son équivalent binaire (via ASCII)
helloworldCharToBinary = conversionCharTo(helloworldChar, 'b')
print(helloworldCharToBinary)

#Conversion d'une chaine de caractères en son équivalent hexadécimal (via ASCII)
helloworldCharToHex = conversionCharTo(helloworldChar, 'h')
print(helloworldCharToHex)

#Erreur
helloworldErreur = conversionCharTo(helloworldChar, 'z')
print(helloworldErreur)

#===================================#


print("")
helloworldASCII = helloworldCharToASCII
#===========DEPART ASCII============#

#Conversion d'une liste d'int en leur correspondance ASCII (char)
helloworldASCIIToChar = conversionASCIITo(helloworldASCII, 'c')
print(helloworldASCIIToChar)

#Aucune conversion
helloworldASCIIToASCII = conversionASCIITo(helloworldASCII, 'a')
print(helloworldASCIIToASCII)

#Conversion d'une liste d'int en bianaire
helloworldASCIIToBinary = conversionASCIITo(helloworldASCII, 'b')
print(helloworldASCIIToBinary)

#Conversion d'une liste d'int en hexadécimal
helloworldASCIIToHex = conversionASCIITo(helloworldASCII, 'h')
print(helloworldASCIIToHex)

#Erreur
helloworldErreur = conversionASCIITo(helloworldASCII, 'z')
print(helloworldErreur)

#===================================#


print("")
helloworldBinary = helloworldCharToBinary
#============DEPART BIN=============#

#Conversion d'une liste de binaires en leur correspondance ASCII (char)
helloworldBinaryToChar = conversionBinTo(helloworldBinary, 'c')
print(helloworldBinaryToChar)

#Conversion d'une liste de binaires en int
helloworldBinaryToASCII = conversionBinTo(helloworldBinary, 'a')
print(helloworldBinaryToASCII)

#Aucune conversion
helloworldBinaryToBinary = conversionBinTo(helloworldBinary, 'b')
print(helloworldBinaryToBinary)

#Conversion d'une liste de binaires en hexadécimal
helloworldBinaryToHex = conversionBinTo(helloworldBinary, 'h')
print(helloworldBinaryToHex)

#Erreur
helloworldErreur = conversionBinTo(helloworldBinary, 'z')
print(helloworldErreur)

#===================================#


print("")
helloworldHex = helloworldCharToHex
#============DEPART HEX=============#

#Conversion d'une liste d'hexadécimales en leur correspondance ASCII (char)
helloworldHexToChar = conversionHexTo(helloworldHex, 'c')
print(helloworldHexToChar)

#Conversion d'une liste d'hexadécimales en int
helloworldHexToASCII = conversionHexTo(helloworldHex, 'a')
print(helloworldHexToASCII)

#Conversion d'une liste d'hexadécimales en binaire
helloworldHexToBinary = conversionHexTo(helloworldHex, 'b')
print(helloworldHexToBinary)

#Aucune conversion
helloworldHexToHex = conversionHexTo(helloworldHex, 'h')
print(helloworldHexToHex)

#Erreur
helloworldErreur = conversionHexTo(helloworldHex, 'z')
print(helloworldErreur)

#===================================#