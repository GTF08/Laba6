from enum import Enum

class Mode(Enum):
    Cipher = "C"
    Decipher = "DC"

def Vigenere(keyword, Mode, filepath = "text.txt", writepath = "result.txt"):
    file = open(filepath, 'r')
    writefile = open(writepath, 'w')
    for line in file:
        if(Mode.name == "Cipher"):
            i = 0
            encryptedStr = ""
            for char in line:
                if(Alphabeth.find(char.upper()) != -1):
                    charID = Alphabeth.index(char.upper())
                    offset = Alphabeth.index(keyword[i%len(keyword)].upper())
                    if(char.isupper()):
                        encryptedStr += Alphabeth[(charID+offset)%ALen]
                    else:
                        encryptedStr += Alphabeth[(charID+offset)%ALen].lower()
                    i+=1
                else:
                    encryptedStr += char

            writefile.write(encryptedStr)
        else:
            i = 0
            encryptedStr = ""
            for char in line:
                if(Alphabeth.find(char.upper()) != -1):
                    charID = Alphabeth.index(char.upper())
                    offset = Alphabeth.index(keyword[i%len(keyword)].upper())
                    if(char.isupper()):
                        encryptedStr += Alphabeth[(charID-offset)%ALen]
                    else:
                        encryptedStr += Alphabeth[(charID-offset)%ALen].lower()
                    i+=1
                else:
                    encryptedStr += char

            writefile.write(encryptedStr)

    file.close()
    writefile.close()

Alphabeth = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ALen = len(Alphabeth)
mode = Mode.Cipher
filepath = "text.txt"
writepath = "result.txt"

Vigenere("Savior",Mode.Cipher, filepath, writepath)
Vigenere("Savior",Mode.Decipher, writepath, "deciphered.txt")
