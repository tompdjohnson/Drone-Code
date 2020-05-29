# Prime Number Tester by Tom Johnson 2020
# This program will test numbers to see if they are Prime numbers.
# Use this code for whatever you want, when you want.

#Number To Test
number=7

# Function Created to test a number to see if its a PRIME Number.
def isPrime(number):
    # for loop including math which checks the number
    for i in range(2,int(number**0.5)+1):
        # if it does not have a remainder is not a prime.
        if n%i==0:
            print (number, "Is NOT Prime")
            return

    else:
        # If the number has a remainder after modulus, it is a Prime.
        print(number, "Is Prime")

# Runs Function and feeds in number variable.
isPrime(number)
