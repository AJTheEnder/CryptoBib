from pickle import NONE
from sage.all import *
import annuaireConversion as AC

class cleAES :
    def __init__(self, cle) :
        asciiCle = AC.conversionCharTo(cle, 'a')
        print(asciiCle)
        matriceCle = sage.all.matrix(4, 4)
        indexStrCle = 0
        for i in range(4) :
            for j in range(4) :
                matriceCle[i, j] = asciiCle[indexStrCle]
                indexStrCle += 1
        self.cle = matriceCle 
            
class messageAES :
    def __init__(self, message) :        
        self.messageHacher = []
        asciiMessage = AC.conversionCharTo(message, 'a')
        indexStrMessage = 0
        for parts in range(len(asciiMessage) // 16) :
            matricePartieMessage = sage.all.matrix(4, 4)
            for i in range(4) :
                for j in range(4) :
                    matricePartieMessage[i, j] = asciiMessage[indexStrMessage]
                    indexStrMessage += 1
            self.messageHacher.append(matricePartieMessage)    
        if(len(asciiMessage) % 16 != 0) :   
            matricePartieMessage = sage.all.matrix(4, 4)
            for i in range(4) :
                for j in range(4) :
                    if(indexStrMessage >= len(asciiMessage)) :
                        matricePartieMessage[i, j] = 32
                    else :
                        matricePartieMessage[i, j] = asciiMessage[indexStrMessage]
                    indexStrMessage += 1
            self.messageHacher.append(matricePartieMessage)
        
'''          
mdp = "Cdfp56qpr8Z4G73c"
cle = cleAES(mdp)
print(cle.cle)
'''  
message = "Les chaussettes de l'archiduchesse sont-elle sèches, archisèches ?"
lastBlock = 1
if(len(message) % 16 != 0) :
    lastBlock = 1
else :
    lastBlock = 0
print("le message est d'une longueur de ", len(message), 
      " caractères, il possède ", len(message) // 16, 
      " blocks de 16 caractères et possède ", lastBlock, 
      " block incomplet de ", len(message) % 16, "caractères")
messageHacher = messageAES(message)
print(messageHacher.messageHacher)
        
            