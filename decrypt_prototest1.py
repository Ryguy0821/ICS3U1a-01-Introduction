# Encryption/Decryption test by Symb1ote and ArcKnight18
# Last Modified on: 2/17/2018, 9:51 PM

# Encrypt Test

import random
import binascii

numZeroes = 0
numOnes = 0
randLettZero = 0
randLettZero = 0
letterHoriz= ""

sentence = input("Message:")

for i in range(0,len(sentence)):
  asciiNum = (ord(sentence[i])) 
  text = str(bin(asciiNum)[2:])  
  for tex in range(0,len(text)):
    asciiB= (ord(text[tex])) 
    numZeroes= random.randint(97,122)
    numOnes= random.randint(65,90)
    if asciiB == 48:
      randLettZero= chr(numZeroes)
      letterHoriz += randLettZero
    elif asciiB == 49:
      randLettOne = chr(numOnes) 
      letterHoriz += randLettOne
print (letterHoriz)

# Decrypt Test

countSort = 0
groupBin = ""
realBin = ""
countRep = 7

for D in range(0,len(letterHoriz)):
  asciiValue = (ord(letterHoriz[D]))
  if 122 >= asciiValue >= 97:
    countSort += 1
    groupBin += "0"
  elif 90 >= asciiValue >= 65:
    countSort += 1
    groupBin += "1"
  if countSort in (7, countRep):
    realBin = ('0' + groupBin)
    print (chr(int(realBin, 2)))
    groupBin = ""
    realBin = ""
    countRep += 7
