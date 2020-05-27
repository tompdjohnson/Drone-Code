# Dual Prime Number Generator by Tom Johnson 2020
# Use this code in any project you want.


# Importing libraries
import math
import random

# Rand Number - Function 1 - allows set range below
def isPrime(n):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False;
    return n>1;

# Rand Number - Function 2 - allows set range below
def isPrime2(m):
    for i in range(2, int(math.sqrt(m)+1)):
        if m % i == 0:
            return False;
    return m>1;



print("")
print("")

# Range for function 1 prime number
numberRand = (random.randint(1000, 2000))
# Range for function 2 prime number
numberRand2 = (random.randint(500, 999))


# Loop to generate a single random Prime Number based on function 1
randprime1=[]
for n in range(numberRand, numberRand+60):
    if isPrime(n):
        randprime1=n
        print(n)
        break


print("")

# Loop to generate a single random Prime Number based on function 2
randprime2=[]
for m in range(numberRand2, numberRand2+60):
    if isPrime2(m):
        randomprime2=m
        print(m)
        break
