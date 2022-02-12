from sage.all import *
import annuaireConversion as AC

S_BOX = ['''   0     1     2     3     4     5     6     7     8     9     A     B     C     D     E     F  '''
  ''' 0 ''' ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5', '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
  ''' 1 ''' ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0', 'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
  ''' 2 ''' ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc', '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
  ''' 3 ''' ['04', 'c7', '23', 'c3', '18', '96', '05', '9a', '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
  ''' 4 ''' ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0', '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
  ''' 5 ''' ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b', '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
  ''' 6 ''' ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85', '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
  ''' 7 ''' ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5', 'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
  ''' 8 ''' ['cd', '0c', '13', 'ec', '5f', '97', '44', '17', 'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
  ''' 9 ''' ['60', '81', '4f', 'dc', '22', '2a', '90', '88', '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
  ''' A ''' ['e0', '32', '3a', '0a', '49', '06', '24', '5c', 'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
  ''' B ''' ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9', '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
  ''' C ''' ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6', 'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
  ''' D ''' ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e', '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
  ''' E ''' ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94', '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
  ''' F ''' ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68', '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
]

'''
||==============================================||
||           Fonctions de la clé AES            ||
||==============================================||
'''
class cleAES :
    '''
  <<===========Constructeur clé AES===========>>
    '''
    def __init__(self, cle) :
        #Conversion de la clé en code ASCII
        asciiCle = AC.conversionCharTo(cle, 'a')
        matriceCle = sage.all.matrix(4, 4)
        #Initialisation d'un index qui servira à suivre l'avancement dans la chaine
        indexStrCle = 0
        #Remplissage de la matrice avec les codes ascii récupérés
        for i in range(4) :
            for j in range(4) :
                matriceCle[i, j] = asciiCle[indexStrCle]
                indexStrCle += 1
        self.cle = matriceCle 

'''
||==============================================||
||           Fonctions du message AES           ||
||==============================================||
'''            
class messageAES :
    '''
  <<=========Constructeur message AES=========>>
    '''
    def __init__(self, message) :        
        self.messageHacher = []
        #Conversion du message en code ASCII
        asciiMessage = AC.conversionCharTo(message, 'a')
        #Initialisation d'un index qui servira à suivre l'avancement dans la chaine
        indexStrMessage = 0
        
        #Pour chaque blocks complet de 16 caractères que contient le message
        for parts in range(len(asciiMessage) // 16) :
            #On créé une matrice 4x4
            matricePartieMessage = sage.all.matrix(4, 4)
            
            #Remplissage de la matrice avec les codes ascii récupérés
            for i in range(4) :
                for j in range(4) :
                    matricePartieMessage[i, j] = asciiMessage[indexStrMessage]
                    indexStrMessage += 1
            
            self.messageHacher.append(matricePartieMessage)    
        
        #Si le message contient de un dernier block qui ne contient pas 16 caractères
        if(len(asciiMessage) % 16 != 0) :   
            #On créé une matrice 4x4
            matricePartieMessage = sage.all.matrix(4, 4)
            
            #Que l'on rempli des codes ascii ou de 32 (ascii code de l'espace)
            for i in range(4) :
                for j in range(4) :
                    
                    #Remplissage d'espaces
                    if(indexStrMessage >= len(asciiMessage)) :
                        matricePartieMessage[i, j] = 32
                    #Remplissage avec les codes ascii
                    else :
                        matricePartieMessage[i, j] = asciiMessage[indexStrMessage]
                    
                    indexStrMessage += 1
            
            self.messageHacher.append(matricePartieMessage)
        
               
'''
||==============================================||
||                 Zone de test                 ||
||==============================================||
'''

mdp = "Cdfp56qpr8Z4G73c"
cle = cleAES(mdp)
print(cle.cle)
  
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
        
            