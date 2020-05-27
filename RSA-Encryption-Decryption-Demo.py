# RSA Encryption/Decryption Demo writen by Tom Johnson
# Use this code in whatever you want, whenever you want.

#import socket
import time
import string
import os
import re

import random
global colour1
global colour2
global colour3
global colour4
global colour5
global colour6
global colour7
global colour8
colour1 = "\033[1;31;40m" # red
colour2 = "\033[1;32;40m" # green
colour3 = "\033[1;33;40m" # yellow
colour4 = "\033[1;34;40m" # blue
colour5 = "\033[1;35;40m" # magenta
colour6 = "\033[1;36;40m" # cyan
colour7 = "\033[1;37;40m" # white
colour8 = "\033[1;30;40m" # dark grey


randomcolours=["\033[1;31;40m", "\033[1;33;40m", "\033[1;34;40m", "\033[1;36;40m", "\033[1;32;40m", "\033[1;35;40m"]

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return


cls();


publickey=871
modulus=979
privatekey=391

print(colour7)

title="SINGLE KEY - RSA Encryption/Decryption Demonstration by Acon1tum 2020"

for i in title:
    print(random.choice(randomcolours)+i,end=" ")

print(colour7)
print("")


# taking users input
usrMessage = input("Enter Text >  ")


# Puts whole input into lowercase
usrMessage = usrMessage.lower()

# stripping non-alpha characters
usrMessage=''.join(c for c in usrMessage if c.isalpha())
print("Removing non-alpha Characters...")
print("Message without Special Characters -->", usrMessage)



print("")
print("")
print("***************  ENCRYPTING  ***************")
print("")
print("Plain Text Message -->", colour4, usrMessage, colour7)
print("")

# removes spaces to avoid an error
usrMessage = usrMessage.replace(' ', '')
msgNumberCombined=[]
msgEncrypted=[]
msgDecrypted=[]
for i in range(0, len(msgNumberCombined)):
    msgNumberCombined[i] = int(msgNumberCombined[i])

for i in usrMessage:
    msgNumber = string.ascii_lowercase.index(i)
    msgNumberCombined.append(msgNumber+1)

for i in range(0, len(msgNumberCombined)):
    msgEncrypted.append(msgNumberCombined[i] ** publickey % modulus)

print("Plain Text Numerical Representation: ", colour2, msgNumberCombined, colour7)
print("")
print("RSA Public Key Applied:              ", colour2, msgEncrypted, colour7 )
print("")



# number modulus 26 to find cypher text letter
textEncrypted=[]
for i in range(0, len(msgEncrypted)):
    textEncrypted.append(msgEncrypted[i] % 26)
print("RSA Alphabetical Position:           ", colour2, textEncrypted, colour7)
print("")

cypherText=[]
cypherText = [chr(number +96) for number in textEncrypted]
print("Encrypted Message -->",colour1, "".join(cypherText), colour7)

for i in range(0, len(msgEncrypted)):
    msgDecrypted.append(msgEncrypted[i] ** privatekey % modulus)
print("")
print("")
print("************** DECRYPTING **************")
print("")
print("Encrypted Message -->", colour1, "".join(cypherText), colour7)
print("")
print("Cypher Text Numerical Representation:", colour2, textEncrypted, colour7)
print("")
print("RSA Private Key Applied:             ", colour2, msgEncrypted, colour7)
print("")
print("Decrypted Message:                   ",colour2, msgDecrypted, colour7)
print("")

msgPlain=[]
msgPlain = [chr(number +96) for number in msgDecrypted]
print("Decrypted Message -->",colour4, "".join(msgPlain), colour7)
