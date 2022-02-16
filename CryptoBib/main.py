import AES 

mdp = "Cdfp56qpr8Z4G73c"
print('')
print("mot de passe : ", mdp)

cle = AES.CleAES(mdp)

cle.keySchedule()
print('')
print("liste des des sous-clés : ")
for subCle in range(len(cle.subCleList)) :
    print('')
    print(cle.subCleList[subCle])
  
message = "Les chaussettes de l'archiduchesse sont-elle sèches, archisèches ?"
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