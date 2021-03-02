
import math
import keyword
import random
import numpy as np
from types import *

# Author: Ajinkya Mukherjee
# Class: Operation System Security
# School: New York Institute of Technology


# The following Python program is used to construct two CryptoSystems
# CryptoSystem 1: Affine Cipher
# CryptoSystem 2: Vigenere Cipher




##     0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24   25
# A = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
# B = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"]
# C = ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"]
# D = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"]
# E = ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"]
# F = ["F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E"]
# G = ["G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F"]
# H = ["H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"]
# I = ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"]
# J = ["J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
# K = ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
# L = ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
# M = ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
# N = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
# O = ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
# P = ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
# Q = ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
# R = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
# S = ["S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]
# T = ["T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"]
# U = ["U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
# V = ["V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"]
# W = ["W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]
# X = ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]
# Y = ["Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]
# Z = ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]


# Dictionary consisting of Alphabets and their corresponding numeric values
dictionaryAlphaToNum ={
    "A" : 0,
    "B" : 1,
    "C" : 2,
    "D" : 3,
    "E" : 4,
    "F" : 5,
    "G" : 6,
    "H" : 7,
    "I" : 8,
    "J" : 9,
    "K" : 10,
    "L" : 11,
    "M" : 12,
    "N" : 13,
    "O" : 14,
    "P" : 15,
    "Q" : 16,
    "R" : 17,
    "S" : 18,
    "T" : 19,
    "U" : 20,
    "V" : 21,
    "W" : 22,
    "X" : 23,
    "Y" : 24,
    "Z" : 25
}
# Dictionary consisting of Numbers and their corresponding Alphabetic values
dictionaryNumtoAlpha = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "J",
    10: "K",
    11: "L",
    12: "M",
    13: "N",
    14: "O",
    15: "P",
    16: "Q",
    17: "R",
    18: "S",
    19: "T",
    20: "U",
    21: "V",
    22: "W",
    23: "X",
    24: "Y",
    25: "Z",

}
#Function that acts as the Vigenere Table

def vTable(listChoice):
    if listChoice == 'A':
        listChosen =  ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    elif listChoice == 'B':
        listChosen = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A"]
    elif listChoice == 'C':
        listChosen = ["C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B"]
    elif listChoice == 'D':
        listChosen = ["D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C"]
    elif listChoice == 'E':
        listChosen = ["E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D"]
    elif listChoice == 'F':
        listChosen = ["F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E"]
    elif listChoice == 'G':
        listChosen = ["G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F"]
    elif listChoice == 'H':
        listChosen = ["H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G"]
    elif listChoice == 'I':
        listChosen = ["I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H"]
    elif listChoice == 'J':
        listChosen = ["J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I"]
    elif listChoice == 'K':
        listChosen = ["K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    elif listChoice == 'L':
        listChosen = ["L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
    elif listChoice == 'M':
        listChosen = ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    elif listChoice == 'N':
        listChosen = ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"]
    elif listChoice == 'O':
        listChosen = ["O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N"]
    elif listChoice == 'P':
        listChosen = ["P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O"]
    elif listChoice == 'Q':
        listChosen = ["Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P"]
    elif listChoice == 'R':
        listChosen = ["R", "S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q"]
    elif listChoice == 'S':
        listChosen = ["S", "T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R"]
    elif listChoice == 'T':
        listChosen = ["T", "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S"]
    elif listChoice == 'U':
        listChosen = ["U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T"]
    elif listChoice == 'V':
        listChosen = ["V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U"]
    elif listChoice == 'W':
        listChosen = ["W", "X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V"]
    elif listChoice == 'X':
        listChosen = ["X", "Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W"]
    elif listChoice == 'Y':
        listChosen = ["Y", "Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X"]
    elif listChoice == 'Z':
        listChosen = ["Z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y"]

    return listChosen



# Encryption Function: Vigenere Cipher
def encryptVigenere(messageList,key):
    messLen = len(messageList)
    #print(messageList)
    key = messLen*key
    encryptedMessageList= []
    encryptedMessage = ''
    for i in range(0, messLen):
        listChoiceM = messageList[i] # Chose the Letter from Plain Text
        listChosenM = vTable(listChoiceM) # Give us the list of Alphabets with Corresponding PlainText Character
        chosenChar = key[i] # chose letter from Key
        chosenValue = dictionaryAlphaToNum.get(chosenChar) # Convert Alphabet to Number
        encryptedChar = listChosenM[chosenValue] # chose the position.
        encryptedMessageList.append(encryptedChar)
        #print(encryptedMessage)

    encryptedMessageLen = len(encryptedMessageList)
    for x in range(0, encryptedMessageLen):
        encryptedMessage += encryptedMessageList[x]
        #print(encryptedMessage)
    return encryptedMessage

# Decryption Function: Vigenere Cipher
def decryptVigenere(cipherList, key):
    cipherLen = len(cipherList)
    decipherMessage = ''
    key = cipherLen*key
    #print("Key is: \t")
    #print(key)
    #chosenCharNum = 0
    decipherMessageList = []

    for i in range(0, cipherLen):
        listChoiceC = cipherList[i]
        listChosenC = vTable(listChoiceC)
        keytoNum = dictionaryAlphaToNum.get(key[i])
        #print("Key is: \t" + str(key[i]))
        #decipherMessageList.append(listChosenC[keytoNum])
        cipherToNum = dictionaryAlphaToNum.get(listChoiceC)
        if cipherToNum >= keytoNum:
            val = abs(cipherToNum - keytoNum)
        else:
            val = 26 - abs(cipherToNum - keytoNum)
        #print(" value is \t" + str(val))
        #print("Plain Text Alpha is " + str(dictionaryNumtoAlpha.get(val)))
        decipherMessageList.append(dictionaryNumtoAlpha.get(val))
    for x in range(0, cipherLen):
        decipherMessage += decipherMessageList[x]

    return decipherMessage


# Encryption Function for Affine Cipher
# Formula used ax+b mod 26
def encryptAffine(plainText, a , b):
    plainTextlen = len(plainText)
    cipherMessage = ""
    cipherMessageList = []
    for x in range(0, plainTextlen):
        alphatoNum = dictionaryAlphaToNum.get(plainText[x])
        alphatoNum = int(alphatoNum)
        lhs1 = a * alphatoNum
        lhs = lhs1 + b
        cipherTextNum = lhs % 26 #Encryption Formula
        cipherTextChar = dictionaryNumtoAlpha.get(cipherTextNum)
        cipherMessageList.append(cipherTextChar)
    for i in range(0, plainTextlen):
        cipherMessage += cipherMessageList[i]

    return cipherMessage


# Function to generate Multiplicative Modulo inverse of a number
# num1 * itr = 1 mod num2
# Return Itr which is multiplicative Inverse of num1 while dividing with num2 resulting in 1 as reminader
def multInverse(num1,num2):
    for itr in range(1,num2):
        if((num1*itr)%num2) == 1:
            return itr
        else:
            continue

# Decryption Function to
# Formula used is c(x-b) mod 26
def decryptAffine(cipher, a, b):
    cipherTextLen = len(cipher)
    originalMessage = ""
    originalMessageList = []
    inv = multInverse(a,26)
    for y in range(0, cipherTextLen):
        alphatoNum = dictionaryAlphaToNum.get(cipher[y])
        originalMessageNum = (inv * (alphatoNum - b)) % 26
        originalMessageChar = dictionaryNumtoAlpha.get(originalMessageNum)
        originalMessageList.append(originalMessageChar)

    for i in range(0,cipherTextLen):
        originalMessage += originalMessageList[i]

    return originalMessage





def main():
    print("******************* Welcome to my Crypto System ******************")
    print("In this Program you can chose to encrypt or decrypt using either Affine Cipher or Vigenere Cipher")
    option = int(input("Enter 1 for Vigenere Cipher and 2 for Affine Cipher\n"))
    if option == 1:
        print("Welcome to Vigenere Crypto System\n")
        message = input("Please Enter the Message to Encrypt\n")
        message = message.upper()
        charMessage =[c for c in message]
        key = input("Please enter the Key\n")
        key = key.upper()
        charKey = [k for k in key]
        print("Encrypting The PlainText")
        CipherText = encryptVigenere(charMessage, charKey)
        print("Message After Encrypting is\n")
        print(CipherText.lower())
        print("Decrypting the Cipher Text")
        charCipher = [y for y in CipherText]
        plainText = decryptVigenere(charCipher, charKey)
        print("Message After Decrypting  is\n")
        print(plainText.lower())


    elif option == 2:
        print("Welcome to Affine Crypto System")
        message = input("Please Enter the Message you want to encrypt\t")
        message = message.upper()
        charMessage = [c for c in message]
        keyA = int(input("Please enter the Coefficient for A (number only)\t"))
        keyB = int(input("Please enter the Coefficient for B (number only)\t"))
        print("Message After Encrypting is\n")
        cipher = encryptAffine(charMessage, keyA, keyB)
        print(cipher.lower())
        cipherText = [z for z in cipher]
        print("Message After Decryption is\n")
        orgMessage = decryptAffine(cipherText, keyA, keyB)
        print(orgMessage.lower())
    else:
        print("Erroneous Entry please restart the program")

       
if __name__ == '__main__':
    main()
