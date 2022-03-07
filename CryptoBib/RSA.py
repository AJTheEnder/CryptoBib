from sage.all import *
import annuaireConversion as AC
import arithmetiqueRSA as arithmetic
import constantes as const

'''
||==============================================||
||           Fonctions de la clé RSA            ||
||==============================================|| 
'''
class CleRSA :
    def __init__(self) :
        self.n = 0
        self.PhiN = 0
        self.exponent = 0
        self.privateKey = 0
        self.publicKey = (0, 0)
        
    def calculPhiN(self, p, q) :
        self.n = p * q
        self.PhiN = (p - 1) * (q - 1)
    
    def chooseExponent(self, e) :
        self.exponent = e
    
    def calculPublicKey(self) :
        self.publicKey = (self.n, self.exponent)
        
    def calculPrivateKey(self) :
        self.privateKey = arithmetic.bezoutEquation(self.exponent, self.PhiN)[0]
        


'''
||==============================================||
||           Fonctions du message RSA           ||
||==============================================|| 
'''        
class MessageRSA :
    def __init__(self, message) :
        messageNum = []
        for i in range(len(message)) :
            messageNum.append(ord(message[i]))
        self.message = messageNum
        self.encryptedMessage = []
        
    def Encryption(self, n, e) :
        for i in range(len(self.message)) :
            self.encryptedMessage.append(pow(self.message[i], e, n))



'''
||==============================================||
||         Fonctions de décryptage RSA          ||
||==============================================|| 
'''        
class DecryptMessageRSA :
    def __init__(self, message) :
        self.encryptedMessage = message
        for i in range(len(message)) :
            i = 0