helloworld = "Hello world"
helloworldASCII = []
helloworldASCIItoChar = []
intLetter = 0
charLetter = ""
hexLetter = ""
for letter in range(len(helloworld)) :
    intLetter = format(ord(helloworld[letter]), "x")
    print(intLetter)
    helloworldASCII.append(intLetter)
    
print(" ")
for x in range((len(helloworld))) :
    print(x)
    