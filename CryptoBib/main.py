import AES 

mdp = "abcdefghijklmnop"
print('')
print("mot de passe : ", mdp)

cle = AES.CleAES(mdp)
print('')
print("cle originel : ")
print('')
print(cle.originalCle)

cle.keySchedule()
print('')
print("liste des des sous-clés : ")
for subCle in range(len(cle.subCleList)) :
    print('')
    print(cle.subCleList[subCle])
  
message = "les chaussettes de l'archiduchesse sont-elles sèches, archisèches ?"
print('')
print("message : ", message)

lastBlock = 1
if(len(message) % 16 != 0) :
    lastBlock = 1
else :
    lastBlock = 0

print('')
print("le message est d'une longueur de ", len(message), 
      " caractères, il possède ", len(message) // 16, 
      " blocks de 16 caractères et possède ", lastBlock, 
      " block incomplet de ", len(message) % 16, "caractères")

messageHacher = AES.MessageAES(message)

messageHacher.addRoundKey(cle.originalCle)

for rounds in range(9) :
    messageHacher.subBytes()
    messageHacher.shiftRows()
    messageHacher.mixColumn()
    cle.currentKey = cle.subCleList[rounds]
    messageHacher.addRoundKey(cle.currentKey)

messageHacher.subBytes()
messageHacher.shiftRows()
messageHacher.addRoundKey(cle.subCleList[9])

print('')
messageHacher.turnIntoChar()

print('')
print("La matrice du message crypté est : ")
print(messageHacher.messageHacher)

messageCrypter = AES.DecryptMessageAES(messageHacher.messageHacher)

messageCrypter.reverseAddRoundKey(cle.subCleList[9])
messageCrypter.reverseShiftRows()
messageCrypter.reverseSubBytes()

for rounds in range(9) :
    cle.currentKey = cle.subCleList[8 - rounds]
    messageCrypter.reverseAddRoundKey(cle.currentKey)
    messageCrypter.reverseMixColumn()
    messageCrypter.reverseShiftRows()
    messageCrypter.reverseSubBytes()
    
messageCrypter.reverseAddRoundKey(cle.originalCle)

print('')
messageCrypter.turnIntoChar()

print('')
print("La matrice du message décrypté est : ")
print(messageCrypter.messageHacherCypter)