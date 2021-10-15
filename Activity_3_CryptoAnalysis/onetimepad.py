""" 
Marcela Fuentes, A01748161
Katia Bellido, A01023638
Carla Pérez Gavilán, A01023033
16/03/2021

One Time Pad:  generates key automatically and returns ciphertext & key
"""

import string
import random
import sys

def generateKey(plainText):
    alphabet="abcdefghijklmnopqrstuvwxyz "
    size=len(plainText)
    key=''.join(random.choice(alphabet) for i in range(size))
    return key

def encryptChar(plainText, key):
    cipherNum=(charToNum(plainText) + charToNum(key)) % 27
    cipherText=numToChar(cipherNum)
    return cipherText

def charToNum(char):
    alphabet="abcdefghijklmnopqrstuvwxyz "
    num=1
    for letter in alphabet:
        if letter==char:
            break
        else:
            num+=1
    return num

def numToChar(num):
    alphabet="abcdefghijklmnopqrstuvwxyz "
    return alphabet[num+1]

def encrypt(plainText, key):
    cipherText=""
    for i in range(0, len(plainText)):
        cipherText += encryptChar(plainText[i], key[i])
    
    return cipherText

if __name__ == "__main__":
    
    cont=True
    choice=""
    plainText=""

    print("Welcome to One Time Pad! I can help you encrypt a message by generating a random key.  Remember that your plaintext can contain spaces but not numbers!")
    print("\n Pick an option: \n 1: Encrypt \n 2: Quit \n")
    
    while cont==True:
        choice=input(">>> ")
        if choice=="1":
            print("Please enter your plaintext: ")
            plainText=input(">>> ")
            print("The generated key is " + generateKey(plainText) + " & your ciphertext is " + encrypt(plainText, generateKey(plainText)))

        elif choice=="2":
            cont=False

        else:
            print("Please choose 1 or 2")
