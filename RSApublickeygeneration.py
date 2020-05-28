# Dual Prime Number Generator by Tom Johnson 2020
# Use this code in any project you want.


# Importing libraries
import math
import random
import os
import time
from functools import reduce
# setting up colours
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
null=0

# Setting text to white.
print(colour7)

# clear screen function
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    return


# Rand Number - Function 1 - allows set range below
def isPrime(p):
    for i in range(2, int(math.sqrt(p)+1)):
        if p % i == 0:
            return False;
    return p>1;

# Rand Number - Function 2 - allows set range below
def isPrime2(q):
    for i in range(2, int(math.sqrt(q)+1)):
        if q % i == 0:
            return False;
    return q>1;


cls()
#'''
# Printing random colour mixed title
title="RSA Public/Private Keygenerator by Acon1tum 2020"
for i in title:
    print(random.choice(randomcolours)+i,end=" ")

print(colour7)
print("")
print("")

# Range for function 1 prime number
numberRand = (random.randint(3, 10))
# Range for function 2 prime number
numberRand2 = (random.randint(3, 50))

print("Generating Prime Numbers")
print("")
# Loop to generate a single random Prime Number based on function 1
randprime1=[]
for p in range(numberRand, numberRand+60):
    if isPrime(p):
        randprime1=p
        print("Prime number 'p' =", colour4, p, colour7)
        break


print("")

# Loop to generate a single random Prime Number based on function 2
randprime2=[]
for q in range(numberRand2, numberRand2+60):
    if isPrime2(q):
        randomprime2=q
        print("Prime number 'q' =", colour4, q, colour7)
        break
print("")
print("")
print("Factorising Prime Numbers to Public/Private Key Modulus")

#'''

#################################
# REMOVE TO RESTORE RANDOM PRIMES
#p=3
#q=11
#################################

print ("p=",p)
print ("q=",q)

n=p*q
print (colour4)
print("p",colour7 ,"*", colour4, "q", colour7, "=",colour1,"n", colour7, "-->",colour1, n, colour7)
print("")
modulus=n
print("Modulus =",colour6,modulus, colour7)
# Math shortcut to work out coprimes.
coprimes = 0
coprimes = ((p-1)*(q-1))
print("")
print("Generating Coprimes")
print("")
print("Number of Coprimes=", colour5, coprimes, colour7)
print("")
print("Modulus=", modulus)

noEven=[]
for i in range(2, modulus+1):
    if i % 2 == 0:
        null=0
    else:
        noEven.append([i])
print("")
flattenedNoEven=reduce(lambda x,y: x+y, noEven)


phiNumbers=[]
print("Calculating 'e' range...")
for i in range(1, coprimes):
    if n % i == 0 or coprimes % i == 0:
        null=0
    else:
        phiNumbers.append([i])
flattenedPhiNumbers=reduce(lambda x,y: x+y, phiNumbers)


multiE=[]
for i in flattenedPhiNumbers:
    if i % 2 ==0:
        null=0
    else:
        multiE.append([i])
elist=reduce(lambda x,y: x+y, multiE)
print ("elist = ", elist)
