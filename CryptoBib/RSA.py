import arithmetiqueRSA as arithmetic

'''
||==============================================||
||           Fonctions de la clé RSA            ||
||==============================================|| 
'''
class CleRSA :
    '''
  <<===========Constructeur clé RSA===========>>
    '''
    def __init__(self) :
        self.n = 0
        self.PhiN = 0
        self.exponent = 0
        self.privateKey = 0
        self.publicKey = (0, 0)
        
    '''
  <<===========Fonction calcul PhiN===========>>
    '''
    def calculPhiN(self, p, q) :
        self.n = p * q
        self.PhiN = (p - 1) * (q - 1)
    
    '''
  <<===========Fonction choose Exp============>>
    '''
    def chooseExponent(self, e) :
        self.exponent = e
    
    '''
  <<===========Fonction public key============>>
    '''
    def calculPublicKey(self) :
        self.publicKey = (self.exponent, self.n)
        
    '''
  <<===========Fonction private key===========>> 
    '''
    def calculPrivateKey(self) :
        self.privateKey = (arithmetic.bezoutEquation(self.exponent, self.PhiN)[0], self.n)
        


'''
||==============================================||
||           Fonctions du message RSA           ||
||==============================================|| 
'''        
class MessageRSA :
    '''
  <<=========Constructeur message RSA=========>>
    '''
    def __init__(self, message) :
        messageNum = []
        for i in range(len(message)) :
            messageNum.append(ord(message[i]))
        self.message = messageNum
        self.encryptedMessage = []
        
    '''
  <<===========Fonction encryption============>>
    '''
    def encryption(self, publicKey) :
        for i in range(len(self.message)) :
            self.encryptedMessage.append(pow(self.message[i], publicKey[0], publicKey[1]))     
            
    '''
  <<=========Fonction turn into char==========>>
    '''
    def turnIntoChar(self) :
        messageChar = ""
        for i in range(len(self.encryptedMessage)) :
            messageChar += chr(self.encryptedMessage[i])
        print(messageChar)



'''
||==============================================||
||         Fonctions de décryptage RSA          ||
||==============================================|| 
'''        
class DecryptMessageRSA :
    '''
  <<=====Constructeur decryptmessage RSA======>>
    '''
    def __init__(self, message) :
        self.encryptedMessage = message
        self.decryptedMessage = []
            
    '''
  <<===========Fonction decryption============>>
    '''
    def decryption(self, d, n) :
        for i in range(len(self.encryptedMessage)) :
            self.decryptedMessage.append(pow(self.encryptedMessage[i], d, n))
            
    '''
  <<=========Fonction turn into char==========>>
    '''
    def turnIntoChar(self) :
        messageChar = ""
        for i in range(len(self.decryptedMessage)) :
            messageChar += chr(self.decryptedMessage[i])
        print(messageChar)