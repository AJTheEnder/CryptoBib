import AES 
import os

clear = lambda : os.system('clear')

def chiffrementAES() :
    print(' ||=====================================================||\n',
          '||                      CryptoBib                      ||\n',
          '||=====================================================||\n') 
    
    message = input('\nChoisissez un message à chiffrer via la méthode AES :')
    messageAES = AES.MessageAES(message)
    lastBlock = 1
    if(len(message) % 16 != 0) :
        lastBlock = 1
    else :
        lastBlock = 0
    print('le message est d une longueur de ', len(message), 
          'caractères, il possède ', len(message) // 16, 
          'blocks de 16 caractères et possède ', lastBlock, 
          'block incomplet de ', len(message) % 16, 'caractères\n')
    
    key = input('\nChoisissez une clé de cyptage de 16 caractères :')
    while (len(key) != 16) :
        key = input('\nLongueur de clé incorrect, choisissez en une autre :')
    keyAES = AES.CleAES(key)
    keyAES.keySchedule()
    
    print('\nChiffrement en cours...\n')
    
    messageAES.addRoundKey(keyAES.originalCle)
    for rounds in range(9) :
        messageAES.subBytes()
        messageAES.shiftRows()
        messageAES.mixColumn()
        keyAES.currentKey = keyAES.subCleList[rounds]
        messageAES.addRoundKey(keyAES.currentKey)
    messageAES.subBytes()
    messageAES.shiftRows()
    messageAES.addRoundKey(keyAES.subCleList[9])
    
    print('\n')
    messageAES.turnIntoChar()
    
    saveMessageData = input('\nVoulez-vous sauvegarder les données du message crypter ? (y/n)\n') 
    if (saveMessageData == 'y') :
        return messageAES.messageHacher
    elif (saveMessageData == 'n') :
        return None
    else :
        return None
    
def dechiffrementAES(savedData) :
    print(' ||=====================================================||\n',
          '||                      CryptoBib                      ||\n',
          '||=====================================================||\n') 
    
    print('\nChoisissez un message à déchiffrer via la méthode AES\n')
    choice = input('\nVoulez-vous écrire le message (1) ou charger les données sauvegarder (2) :')
    if (choice == '1') :
        message = input('\nEcrivez un message à décrypter :')
    elif (choice == '2') :
        if (savedData == None) :
            print('\nAucune donnée sauvegardé')
            message = input('\nEcrivez un message à décrypter :')
        else :
            message = savedData
    else :
        message = input('\nEcrivez un message à décrypter :')
    messageAES = AES.DecryptMessageAES(message)
    
    key = input('\nChoisissez une clé de décyptage de 16 caractères :')
    while (len(key) != 16) :
        key = input('\nLongueur de clé incorrect, choisissez en une autre :')
    keyAES = AES.CleAES(key)
    keyAES.keySchedule()
    
    print('\nDechiffrement en cours...\n')
    
    messageAES.reverseAddRoundKey(keyAES.subCleList[9])
    messageAES.reverseShiftRows()
    messageAES.reverseSubBytes()
    for rounds in range(9) :
        keyAES.currentKey = keyAES.subCleList[8 - rounds]
        messageAES.reverseAddRoundKey(keyAES.currentKey)
        messageAES.reverseMixColumn()
        messageAES.reverseShiftRows()
        messageAES.reverseSubBytes()
    messageAES.reverseAddRoundKey(keyAES.originalCle)
    
    print('\n')
    messageAES.turnIntoChar()
    
    input('Rentrer n importe quoi pour revenir au menu princpal :')
    
savedData = None
loop = True
while (loop == True) :
    clear()
    print('\n ||=====================================================||\n',
            '||                      CryptoBib                      ||\n',
            '||=====================================================||\n')
    print('\n',
          '___________________1  Chiffrer AES  1___________________\n',
          '___________________2 Déchiffrer AES 2___________________\n',
          '___________________3  Chiffrer RSA  3___________________\n',
          '___________________4 Déchiffrer RSA 4___________________\n',
          '___________________5    Quitter     5___________________\n')
    inputLoop = True
    while (inputLoop == True) :
        choice = input('Choisissez une action à réaliser :')
        if (choice == '1') :
            clear()
            savedData = chiffrementAES()
            inputLoop = False
        elif (choice == '2') :
            clear()
            dechiffrementAES(savedData)
            inputLoop = False
        elif (choice == '3') :
            print('Chiffrement RSA non disponible\n')
        elif (choice == '4') :
            print('Déchiffrement RSA non disponible\n')
        elif (choice == '5') :
            print('Arret de CryptoBib\n')
            inputLoop = False
            loop = False
        else :
            print('Choix invalide\n')     