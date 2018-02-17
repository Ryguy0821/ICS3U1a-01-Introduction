
# Allows random integers to be created
# Original code created by ArcKnight18 on 2/16/2018
# Code cleaned up by Symb1ote on 2/17/2018
# Last modified on: 2/17/2018, 2:34 PM

import random

# Variables for creating random letters
numZeroes = 0
numOnes = 0
randLettZero = 0
randLettOne = 0

# Input
sentence = input("Message:")

# Reads each letter in the sentence
for i in range(0,len(sentence)):
  asciiNum= (ord(sentence[i])) # Converts each letter to ascii numbers
  # Turns ascii numbers into into binary, binary is then each 0,1 becomes a string
  text=str(bin(asciiNum)[2:])  
  
  # Reads each 0,1 string
  for tex in range(0,len(text)):
    asciiB= (ord(text[tex])) # Creates the ascii value for 0 and 1
    
    # Creats a random int after each 0 and 1 ascii is created
    # ints are created by a range on the ascii chart to create multiple
    # uppercases and lowercases at random
    numZeroes= random.randint(97,122)
    numOnes= random.randint(65,90)
    
    # if a 0 
    if asciiB == 48:
      RandLettZero= chr(numZeroes) # Convert random int to letter
      print(randLettZero) # Outputs random lowercase letter
    
    # if a 1
    elif asciiB == 49:
      RandLettOne= chr(numOnes) # Convert random int to letter
      print(RandLettOne) #Outputs random Uppercase letter
