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
    def __init__(self, p, q) :
        self.n = 0
        self.PhiN = 0
        self.exponent = 0
        self.privateKey = 0
        self.publicKey = (0, 0)
        
    def calculPhiN(self, p, q) :
        n = p * q
        self.PhiN = (p - 1) * (q - 1)
    
    def chooseExponent(self, e) :
        self.exponent = e
        
    def getPrivateKey(self) :
        self.privateKey = arithmetic.bezoutEquation(self.exponent, self.PhiN)[0]
        
    def getPublicKey(self) :
        self.publicKey = (self.n, self.exponent)



'''
||==============================================||
||           Fonctions du message RSA           ||
||==============================================|| 
'''        
class MessageRSA :
    def __init__(self, message) :
        self.message = message



'''
||==============================================||
||         Fonctions de décryptage RSA          ||
||==============================================|| 
'''        
class DecryptMessageRSA :
    def __init__(self, message) :
        self.message = message