""" 
Marcela Fuentes, A01748161
Katia Bellido, A01023638
Carla Pérez Gavilán, A01023033
16/03/2021

Ceaser: uses a single character as a key to shift the entire alphabet 
"""

def decipher (alphabet, key, mesToDencrypt):
   translated = ""
   for letter in mesToDencrypt:
      if letter in alphabet:
         num = alphabet.find(letter)
         num = num - key
         if num < 0:
            num = num + len(alphabet)
         translated = translated + alphabet[num]
      else:
         translated = translated + letter
   print('Hacking key #%s: %s \n' % (key, translated))
   return translated  

def cipher (alphabet, key, mesToCipher):
   num = 0
   ciphering = ""
   for letter in  mesToCipher:
      if letter in alphabet:
         num = alphabet.find(letter)
         num = num + key
         if num > len(alphabet)-1:
            num = num - len(alphabet)
         ciphering = ciphering + alphabet[num]
      else:
         ciphering = ciphering + letter
   print('Hacking key #%s: %s \n' % (key, ciphering))  
   return ciphering

def statistics (mensaje, alphabet):
   statistic = dict()
   mejorLetra = ''
   contador = 0
   for letters in mensaje:
      if letters in alphabet:
         statistic[letters] = statistic.get(letters,0)+1
   for key, value in statistic.items():
      if value > contador:
         contador = value
         mejorLetra = key
   return mejorLetra

def findNumberKey(letra, alphabet):
   print(letra)
   if letra in alphabet:
      key = LETTERS.find(mejorLetra) +1
   return key

#f = open("RESPUESTACIFRADO.txt", "w+")
message = open('cipher1.txt')
LETTERS = 'abcdefghijklmnopqrstuvwxyz '
count = 0
message2 = message.read()
mejorLetra = statistics(message2, LETTERS)
key = findNumberKey(mejorLetra, LETTERS)
message3 = decipher(LETTERS, key,  message2)
#f.write("KEY: %s\n" %mejorLetra)
#f.write("MESSAGE:\n %s\n" %message3)
cipher(LETTERS,key, message3)
