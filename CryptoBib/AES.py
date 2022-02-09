from operator import index
from sage.all import *
from annuaireConversion import conversionCharTo

class cleAES :
    def __init__(self, cle) :
        hexCle = conversionCharTo(cle, 'h')
        print(hexCle)
        matriceCle = sage.all.matrix(4, 4)
        indexStrCle = 0
        for i in range(4) :
            for j in range(4) :
                matriceCle[i, j] = hexCle[indexStrCle]
                indexStrCle += 1
        self.cle = matriceCle 
            
class messageAES :
    def __init__(self, message) :
        self.messageHacher = []
        messageHex = []
        for char in range(len(message)) : 
            charHex = format(ord(message[char]), "x")
            messageHex.append(charHex)
            
mdp = "Cdfp56qpr8Z4G73c"
cle = cleAES(mdp)
print(cle.cle)
        
            