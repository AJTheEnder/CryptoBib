from sage.all import *
import annuaireConversion as AC
import constantes as const

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
        self.originalCle = matriceCle 
        self.subCleList = []
        self.currentKey = self.originalCle
        
    '''
  <<===========Fonction KeySchedule===========>>
    '''  
    def keySchedule(self) :
        for key in range(10) :
            #Création d'un sous-clé vide
            subKey = sage.all.matrix([[0, 0, 0, 0],
                                      [0, 0, 0, 0],
                                      [0, 0, 0, 0],
                                      [0, 0, 0, 0],])
            
            #Shuffle de la première colonne de la current key
            subKey[0, 0] = self.currentKey[1][3] 
            subKey[1, 0] = self.currentKey[2][3]
            subKey[2, 0] = self.currentKey[3][3]
            subKey[3, 0] = self.currentKey[1][3]  
            
            #Pour chaque élément de la 1ère colonne
            for i in range(4) :
                #Transformation d'un nombre en liste de 1 nombre (pour la conversion)
                preConversion = [subKey[i][0]]
                
                #Conversion de ce nombre en son équivalent hexadécimal
                hexByte = AC.conversionASCIITo(preConversion, 'h')
                
                if (len(hexByte[0]) != 2) :
                    hexByte[0] = '0' + hexByte[0]
                
                #Séparation des 2 composant du nombre hexadécimal en les convertissant en int
                indiceByte0 = int((hexByte[0][0]), 16)
                indiceByte1 = int((hexByte[0][1]), 16)
                
                #Remplacement de l'élément de la matrice par son équivalent dans la const.S_BOX
                subKey[i, 0] = int(const.S_BOX[indiceByte0][indiceByte1], 16)
                
                #Initialisation d'une liste qui servira au calcul de l'élément final
                #Notament pour l'opération XOR
                counterTab = [0, 0, 0, 0, 0, 0, 0, 0]           
                            # 7, 6, 5, 4, 3, 2, 1, 0      
                            #[ 2eme bin ][ 1er bin  ]
            
                #Conversion de l'élément i de la première colonne de la subKey en binaire
                binaryDataSubKey = format(subKey[i][0], 'b')               
                listBinarySubKey = []
                
                #Conversion de l'élément i de la première colonne de la currentKey en binaire
                binaryDataCurrentKey = format(self.currentKey[i][0], 'b')
                listBinaryCurrentKey = []
                
                #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                for b in range(len(binaryDataSubKey)) :
                    listBinarySubKey.append(binaryDataSubKey[b])
                while (len(listBinarySubKey) != 8) :
                    #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                    listBinarySubKey.insert(0, '0')
                    
                #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                for b in range(len(binaryDataCurrentKey)) :
                    listBinaryCurrentKey.append(binaryDataCurrentKey[b])
                while (len(listBinaryCurrentKey) != 8) :
                    #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                    listBinaryCurrentKey.insert(0, '0')
                    
                #Pour chaque chiffre binaire de la liste
                for b in range(8) :
                    #Opérations dans la counterList pour connaitre le binaire de fin
                    if (i == 0) :
                        counterTab[b] += const.RCON[key][b]
                    if (listBinaryCurrentKey[b] == '1') :
                        counterTab[b] += 1
                    if (listBinarySubKey[b] == '1') :
                        counterTab[b] += 1
                        
                #Quand un élément de la liste est impair mettre 1 sinon mettre 0
                for b in range(len(counterTab)) :
                    if (counterTab[b] % 2 == 1) :
                        counterTab[b] = 1
                    else :
                        counterTab[b] = 0
                        
                #Conversion du chiffre binaire final en int
                finalBinary = '0b'
                for b in range(len(counterTab)) :
                    counterTab[b] = str(counterTab[b])
                    finalBinary += counterTab[b]                        
                finalNumber = int(finalBinary, 2)
                #Remplacement de l'ancienne valeur par la nouvelle
                subKey[i, 0] = finalNumber
            
            for column in range(1, 4) :
                for j in range(4) :
                    #Conversion de l'élément j de la "column - 1" colonne de la subKey en binaire
                    binaryDataSubKey = format(subKey[j][column - 1], 'b')               
                    listBinarySubKey = []
                    
                    #Conversion de l'élément j de la "column" colonne de la currentKey en binaire
                    binaryDataCurrentKey = format(self.currentKey[j][column], 'b')
                    listBinaryCurrentKey = []
                    
                    #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataSubKey)) :
                        listBinarySubKey.append(binaryDataSubKey[b])
                    while (len(listBinarySubKey) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinarySubKey.insert(0, '0')

                    #Remplissage de la liste de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataCurrentKey)) :
                        listBinaryCurrentKey.append(binaryDataCurrentKey[b])
                    while (len(listBinaryCurrentKey) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryCurrentKey.insert(0, '0')
                        
                    #Calcul et conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(8) :
                        if (listBinarySubKey[b] != listBinaryCurrentKey[b]) :
                            finalBinary += '1'
                        else :
                            finalBinary += '0'
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    subKey[j, column] = finalNumber
                
            self.subCleList.append(subKey)
            self.currentKey = subKey
        self.currentKey = self.originalCle
        


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
                    
                    if (len(hexByte[0]) != 2) :
                        hexByte[0] = '0' + hexByte[0]
                    
                    #Séparation des 2 composant du nombre hexadécimal en les convertissant en int
                    indiceByte0 = int((hexByte[0][0]), 16)
                    indiceByte1 = int((hexByte[0][1]), 16)
                    
                    #Remplacement de l'élément de la matrice par son équivalent dans la const.S_BOX
                    self.messageHacher[messageParts][i, j] = int(const.S_BOX[indiceByte0][indiceByte1], 16)
                
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
  <<===========Fonction MixColumn=============>>
    ''' 
    def mixColumn(self) :
        #Pour chaque matrice du message
        for index in range(len(self.messageHacher)) :
            messageParts = self.messageHacher[index]
            
            #Pour chaque ligne de la matrice de rijndael
            for i in range(4) :
                rijndaelRow = sage.all.matrix(const.RIJNDAEL_MATRIX.row(i))
                
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
                                if (counterTab[b] == const.PX[b]) :
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
  <<==========Fonction AddRoundKey============>>
    '''                         
    def addRoundKey(self, roundKey) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacher)) :
            #Pour chaque élément de la matrice message courante et la cle courante 
            for i in range(4) :
                for j in range(4) :                   
                    #Conversion de l'élément courant de la matrice et la cle en binaire
                    binaryDataMessage = format(self.messageHacher[messageParts][i][j], 'b') 
                    binaryDataCle = format(roundKey[i][j], 'b')  
                    listBinaryMessage = []
                    listBinaryCle = []
                        
                    #Remplissage de la liste message de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataMessage)) :
                        listBinaryMessage.append(binaryDataMessage[b])
                    while (len(listBinaryMessage) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryMessage.insert(0, '0') 
                        
                    #Remplissage de la liste clé de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataCle)) :
                        listBinaryCle.append(binaryDataCle[b])
                    while (len(listBinaryCle) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryCle.insert(0, '0')
                        
                    resultat = []
                    #Pour chaque bit
                    for b in range(8) :
                        #Si le bit de la cle et du message sont différent alors le bit du résultat est 1
                        if (listBinaryMessage[b] != listBinaryCle[b]) :
                            resultat.append(1)
                        #sinon c'est 0
                        else :
                            resultat.append(0)
                    
                    #Conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(len(resultat)) :
                        resultat[b] = str(resultat[b])
                        finalBinary += resultat[b]                        
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    self.messageHacher[messageParts][i, j] = finalNumber
                    
    '''
  <<=========Fonction TurnIntoChar============>>
    '''
    def turnIntoChar(self) :
        codedMessage = ""
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacher)) :
            #Pour chaque élément de la matrice
            for i in range(4) : 
                for j in range(4) :
                    codedMessage += chr(self.messageHacher[messageParts][i][j])
        print("Le message encrypté est : ")
        print(''.join([str(elem) for elem in codedMessage])) 
                    


'''
||==============================================||
||         Fonctions de décryptage AES          ||
||==============================================||
'''            
class DecryptMessageAES :
    '''
  <<=======Constructeur décrypteur AES========>>
    '''
    def __init__(self, encryptedMessage) : 
        self.messageHacherCypter = encryptedMessage
    
    '''
  <<========Fonction ReverseSubBytes==========>>
    '''   
    def reverseSubBytes(self) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacherCypter)) :
            #Pour chaque élément de la matrice
            for i in range(4) :
                for j in range(4) :
                    #Conversion de l'élément en hexadécimal
                    hexByte = format(self.messageHacherCypter[messageParts][i][j], 'x')
                    
                    #Si c'est un hexa à un chiffre formatage en format 2 chiffre
                    if (len(hexByte) != 2) :
                        hexByte = '0' + hexByte
                        
                    #Formatage sous la forme 0x00 pour la recherche dans const.S_BOX
                    hexByte = '0x' + hexByte
                    
                    #Parcours de toute la const.S_BOX
                    for x in range(len(const.S_BOX)) :
                        for y in range(len(const.S_BOX[x])) :
                            #Si l'élément et l'élément x, y de la const.S_BOX sont les mêmes
                            if (const.S_BOX[x][y] == hexByte) :
                                #L'int 0xXY devient le nouvel élément i, j de la matrice
                                decryptInt = '0x' + format(x, 'x') + format(y, 'x')
                                self.messageHacherCypter[messageParts][i, j] = int(decryptInt, 16)
                                
    '''
  <<=======Fonction ReverseShiftRows==========>>
    '''
    def reverseShiftRows(self) :
        #Pour chaque matrice dans le message
        for messageParts in range(len(self.messageHacherCypter)) :
            #On garde en mémoire les anciennes valeurs de la ligne 1
            element10Tampon = self.messageHacherCypter[messageParts][1, 0]
            element11Tampon = self.messageHacherCypter[messageParts][1, 1]
            element12Tampon = self.messageHacherCypter[messageParts][1, 2]
            element13Tampon = self.messageHacherCypter[messageParts][1, 3]
            #On change la disposition des éléments de la ligne 1
            self.messageHacherCypter[messageParts][1, 0] = element13Tampon
            self.messageHacherCypter[messageParts][1, 1] = element10Tampon
            self.messageHacherCypter[messageParts][1, 2] = element11Tampon
            self.messageHacherCypter[messageParts][1, 3] = element12Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 2
            element20Tampon = self.messageHacherCypter[messageParts][2, 0]
            element21Tampon = self.messageHacherCypter[messageParts][2, 1]
            element22Tampon = self.messageHacherCypter[messageParts][2, 2]
            element23Tampon = self.messageHacherCypter[messageParts][2, 3]
            #On change la disposition des éléments de la ligne 2
            self.messageHacherCypter[messageParts][2, 0] = element22Tampon
            self.messageHacherCypter[messageParts][2, 1] = element23Tampon
            self.messageHacherCypter[messageParts][2, 2] = element20Tampon
            self.messageHacherCypter[messageParts][2, 3] = element21Tampon
            
            #On garde en mémoire les anciennes valeurs de la ligne 3
            element30Tampon = self.messageHacherCypter[messageParts][3, 0]
            element31Tampon = self.messageHacherCypter[messageParts][3, 1]
            element32Tampon = self.messageHacherCypter[messageParts][3, 2]
            element33Tampon = self.messageHacherCypter[messageParts][3, 3]
            #On change la disposition des éléments de la ligne 3
            self.messageHacherCypter[messageParts][3, 0] = element31Tampon
            self.messageHacherCypter[messageParts][3, 1] = element32Tampon
            self.messageHacherCypter[messageParts][3, 2] = element33Tampon
            self.messageHacherCypter[messageParts][3, 3] = element30Tampon 
            
    '''
  <<=======Fonction Reverse MixColumn=========>>
    ''' 
    def reverseMixColumn(self) :
        todo = "A FAIRE"
        
    '''
  <<======Fonction Reverse AddRoundKey========>>
    ''' 
    def reverseAddRoundKey(self, roundKey) :
        #Pour chaque matrice du message
        for messageParts in range(len(self.messageHacherCypter)) :
            #Pour chaque élément de la matrice
            for i in range(4) :
                for j in range(4) :   
                    #Conversion de l'élément courant de la matrice et la cle en binaire
                    binaryDataMessage = format(self.messageHacherCypter[messageParts][i][j], 'b') 
                    binaryDataCle = format(roundKey[i][j], 'b')  
                    listBinaryMessage = []
                    listBinaryCle = []
                        
                    #Remplissage de la liste message de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataMessage)) :
                        listBinaryMessage.append(binaryDataMessage[b])
                    while (len(listBinaryMessage) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryMessage.insert(0, '0') 
                        
                    #Remplissage de la liste clé de chiffre binaire jusqu'à une longueur de 8
                    for b in range(len(binaryDataCle)) :
                        listBinaryCle.append(binaryDataCle[b])
                    while (len(listBinaryCle) != 8) :
                        #Insertion de 0 à l'avant de la liste tant qu'elle de fait pas 8 de longueur
                        listBinaryCle.insert(0, '0')
                        
                    resultat = []
                    #Pour chaque bit
                    for b in range(8) :
                        #Si le bit du message est égal à 1 alors le résultat est identique au bit de la clé
                        if (listBinaryMessage[b] == '0') :
                            if (listBinaryCle[b] == '1') :
                                resultat.append(1)
                            else :
                                resultat.append(0)
                        #sinon le résultat est différent du bit de la clé
                        else :
                            if (listBinaryCle[b] == '1') :
                                resultat.append(0)
                            else :
                                resultat.append(1)
                    
                    #Conversion du chiffre binaire final en int
                    finalBinary = '0b'
                    for b in range(len(resultat)) :
                        resultat[b] = str(resultat[b])
                        finalBinary += resultat[b]                        
                    finalNumber = int(finalBinary, 2)
                    #Remplacement de l'ancienne valeur par la nouvelle
                    self.messageHacherCypter[messageParts][i, j] = finalNumber
                           


'''
||==============================================||
||                 Zone de test                 ||
||==============================================||
'''
'''
mdp = "Cdfp56qpr8Z4G73c"
cle = CleAES(mdp)
print(cle.originalCle)

cle.keySchedule()
  
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

messageHacher = MessageAES(message)

messageHacher.subBytes()

messageHacher.shiftRows()

messageHacher.mixColumn()

messageHacher.addRoundKey(cle.currentKey)

messageHacher.turnIntoChar()
'''