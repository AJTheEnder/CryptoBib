from typing import final
from sage.all import *
import annuaireConversion as AC

S_BOX = [
    ['0x63', '0x7c', '0x77', '0x7b', '0xf2', '0x6b', '0x6f', '0xc5', '0x30', '0x01', '0x67', '0x2b', '0xfe', '0xd7', '0xab', '0x76'],
    ['0xca', '0x82', '0xc9', '0x7d', '0xfa', '0x59', '0x47', '0xf0', '0xad', '0xd4', '0xa2', '0xaf', '0x9c', '0xa4', '0x72', '0xc0'],
    ['0xb7', '0xfd', '0x93', '0x26', '0x36', '0x3f', '0xf7', '0xcc', '0x34', '0xa5', '0xe5', '0xf1', '0x71', '0xd8', '0x31', '0x15'],
    ['0x04', '0xc7', '0x23', '0xc3', '0x18', '0x96', '0x05', '0x9a', '0x07', '0x12', '0x80', '0xe2', '0xeb', '0x27', '0xb2', '0x75'],
    ['0x09', '0x83', '0x2c', '0x1a', '0x1b', '0x6e', '0x5a', '0xa0', '0x52', '0x3b', '0xd6', '0xb3', '0x29', '0xe3', '0x2f', '0x84'],
    ['0x53', '0xd1', '0x00', '0xed', '0x20', '0xfc', '0xb1', '0x5b', '0x6a', '0xcb', '0xbe', '0x39', '0x4a', '0x4c', '0x58', '0xcf'],
    ['0xd0', '0xef', '0xaa', '0xfb', '0x43', '0x4d', '0x33', '0x85', '0x45', '0xf9', '0x02', '0x7f', '0x50', '0x3c', '0x9f', '0xa8'],
    ['0x51', '0xa3', '0x40', '0x8f', '0x92', '0x9d', '0x38', '0xf5', '0xbc', '0xb6', '0xda', '0x21', '0x10', '0xff', '0xf3', '0xd2'],
    ['0xcd', '0x0c', '0x13', '0xec', '0x5f', '0x97', '0x44', '0x17', '0xc4', '0xa7', '0x7e', '0x3d', '0x64', '0x5d', '0x19', '0x73'],
    ['0x60', '0x81', '0x4f', '0xdc', '0x22', '0x2a', '0x90', '0x88', '0x46', '0xee', '0xb8', '0x14', '0xde', '0x5e', '0x0b', '0xdb'],
    ['0xe0', '0x32', '0x3a', '0x0a', '0x49', '0x06', '0x24', '0x5c', '0xc2', '0xd3', '0xac', '0x62', '0x91', '0x95', '0xe4', '0x79'],
    ['0xe7', '0xc8', '0x37', '0x6d', '0x8d', '0xd5', '0x4e', '0xa9', '0x6c', '0x56', '0xf4', '0xea', '0x65', '0x7a', '0xae', '0x08'],
    ['0xba', '0x78', '0x25', '0x2e', '0x1c', '0xa6', '0xb4', '0xc6', '0xe8', '0xdd', '0x74', '0x1f', '0x4b', '0xbd', '0x8b', '0x8a'],
    ['0x70', '0x3e', '0xb5', '0x66', '0x48', '0x03', '0xf6', '0x0e', '0x61', '0x35', '0x57', '0xb9', '0x86', '0xc1', '0x1d', '0x9e'],
    ['0xe1', '0xf8', '0x98', '0x11', '0x69', '0xd9', '0x8e', '0x94', '0x9b', '0x1e', '0x87', '0xe9', '0xce', '0x55', '0x28', '0xdf'],
    ['0x8c', '0xa1', '0x89', '0x0d', '0xbf', '0xe6', '0x42', '0x68', '0x41', '0x99', '0x2d', '0x0f', '0xb0', '0x54', '0xbb', '0x16']
]

RIJNDAEL_MATRIX = sage.all.matrix([
    [2, 3, 1, 1],
    [1, 2, 3, 1],
    [1, 1, 2, 3],
    [3, 1, 1, 2]
])

PX = [1, 0, 0, 0, 1, 1, 0, 1, 1]

'''
||==============================================||
||           Fonctions de la clé AES            ||
||==============================================||
'''
class CleAES :
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
class MessageAES :
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
  <<============Fonction SubBytes=============>>
    '''   
    def subBytes(self) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacher)) :
            #Pour chaque élément de la matrice
            for i in range(4) :
                for j in range(4) :
                    #Transformation d'un nombre en liste de 1 nombre (pour la conversion)
                    preConversion = [self.messageHacher[messageParts][i, j]]
                    
                    #Conversion de ce nombre en son équivalent hexadécimal
                    hexByte = AC.conversionASCIITo(preConversion, 'h')
                    
                    #Séparation des 2 composant du nombre hexadécimal en les convertissant en int
                    indiceByte0 = int((hexByte[0][0]), 16)
                    indiceByte1 = int((hexByte[0][1]), 16)
                    
                    #Remplacement de l'élément de la matrice par son équivalent dans la S_BOX
                    self.messageHacher[messageParts][i, j] = int(S_BOX[indiceByte0][indiceByte1], 16)
                
    '''
  <<===========Fonction ShiftRows=============>>
    ''' 
    def shiftRows(self) :
        #Pour chaque matrice dans le message
        for messageParts in range(len(self.messageHacher)) :
            #On garde en mémoire les anciennes valeurs de la ligne 1
            element10Tampon = self.messageHacher[messageParts][1, 0]
            element11Tampon = self.messageHacher[messageParts][1, 1]
            element12Tampon = self.messageHacher[messageParts][1, 2]
            element13Tampon = self.messageHacher[messageParts][1, 3]
            #On change la disposition des éléments de la ligne 1
            self.messageHacher[messageParts][1, 0] = element11Tampon
            self.messageHacher[messageParts][1, 1] = element12Tampon
            self.messageHacher[messageParts][1, 2] = element13Tampon
            self.messageHacher[messageParts][1, 3] = element10Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 2
            element20Tampon = self.messageHacher[messageParts][2, 0]
            element21Tampon = self.messageHacher[messageParts][2, 1]
            element22Tampon = self.messageHacher[messageParts][2, 2]
            element23Tampon = self.messageHacher[messageParts][2, 3]
            #On change la disposition des éléments de la ligne 2
            self.messageHacher[messageParts][2, 0] = element22Tampon
            self.messageHacher[messageParts][2, 1] = element23Tampon
            self.messageHacher[messageParts][2, 2] = element20Tampon
            self.messageHacher[messageParts][2, 3] = element21Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 3
            element30Tampon = self.messageHacher[messageParts][3, 0]
            element31Tampon = self.messageHacher[messageParts][3, 1]
            element32Tampon = self.messageHacher[messageParts][3, 2]
            element33Tampon = self.messageHacher[messageParts][3, 3]
            #On change la disposition des éléments de la ligne 3
            self.messageHacher[messageParts][3, 0] = element33Tampon
            self.messageHacher[messageParts][3, 1] = element30Tampon
            self.messageHacher[messageParts][3, 2] = element31Tampon
            self.messageHacher[messageParts][3, 3] = element32Tampon 
            
    '''
  <<===========Fonction ShiftRows=============>>
    ''' 
    def mixColumn(self) :
        #Pour chaque matrice du message
        for index in range(len(self.messageHacher)) :
            messageParts = self.messageHacher[index]
            
            #Pour chaque ligne de la matrice de rijndael
            for i in range(4) :
                rijndaelRow = sage.all.matrix(RIJNDAEL_MATRIX.row(i))
                
                #Pour chaque colonne de la matrice courante
                for j in range(4) : 
                    messagePartsColumn = sage.all.matrix(messageParts.column(j))
                    
                    #Initialisation d'une liste qui servira au calcul de l'élément final
                    #Notament pour l'opération XOR
                    counterTab = [0, 0, 0, 0, 0, 0, 0, 0, 0]           
                                 #8, 7, 6, 5, 4, 3, 2, 1, 0      
                                 #X[ 2eme bin  ][ 1er bin  ]
                    
                    #Pour chaque élément d'une ligne et d'une colonne 
                    for m in range(4) :
                        #Conversion de l'élément m de la colonne courante en binaire
                        binaryData = format(messagePartsColumn[0][m], 'b')
                        listBinary = []
                        
                        #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                        for b in range(len(binaryData)) :
                            listBinary.append(binaryData[b])
                        while (len(listBinary) != 8) :
                            #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                            listBinary.insert(0, '0')

                        #Pour chaque chiffre binaire de la liste
                        for b in range(len(listBinary)) :
                            #Opérations dans la counterList pour connaitre le binaire de fin
                            if (rijndaelRow[0][m] == 1) :
                                if (listBinary[b] == '1') :   
                                    counterTab[b + 1] += 1
                            elif (rijndaelRow[0][m] == 2) :
                                if (listBinary[b] == '1') :   
                                    counterTab[b] += 1
                            elif (rijndaelRow[0][m] == 3) :
                                if (listBinary[b] == '1') :   
                                    counterTab[b + 1] += 1
                                    counterTab[b] += 1
                        
                        #Quand un élément de la liste est impair mettre 1 sinon mettre 0
                        for b in range(len(counterTab)) :
                            if (counterTab[b] % 2 == 1) :
                                counterTab[b] = 1
                            else :
                                counterTab[b] = 0
                                
                        #Si le 9ème bit est 1 alors XOR la counterList avec P(X)
                        if (counterTab[0] == 1) :
                            for b in range(len(counterTab)) :
                                if (counterTab[b] == PX[b]) :
                                    counterTab[b] = 0
                                else :
                                    counterTab[b] = 1
                    
                    #Conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(len(counterTab)) :
                        counterTab[b] = str(counterTab[b])
                        finalBinary += counterTab[b]                        
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    self.messageHacher[index][i, j] = finalNumber
                        
                        
                        
'''
||==============================================||
||                 Zone de test                 ||
||==============================================||
'''

mdp = "Cdfp56qpr8Z4G73c"
cle = CleAES(mdp)
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

print('')
messageHacher = MessageAES(message)
print(messageHacher.messageHacher)

print('')
messageHacher.subBytes()
print(messageHacher.messageHacher)  

print('')
messageHacher.shiftRows()
print(messageHacher.messageHacher)

print('')
messageHacher.mixColumn()
print(messageHacher.messageHacher)