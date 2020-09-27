#!/bin/usr/bin/python

# Secure Password Hash Checking Demo - Acon1tum 2020

# This demo is to help students understand how to store
# an SHA512 secure password hash and then take a user
# input, encode it using UTF-8 and hashing it with then
# same hashing algorithm.  The program then compares them
# if they match it prints "Correct" otherwise it prints "Incorrect"

# -----------------------------------------------
# IMPORTING LIBRARIES
# -----------------------------------------------
import hashlib, os


# -----------------------------------------------
# DEFINING STORED PASSWORD  "HELLOWORLD"
# -----------------------------------------------
storedPassword = "1594244d52f2d8c12b142bb61f47bc2eaf503d6d9ca8480cae9fcf112f66e4967dc5e8fa98285e36db8af1b8ffa8b84cb15e0fbcf836c3deb803c13f37659a60"


# -----------------------------------------------
# REQUESTING USER TO ENTER PASSWORD
# -----------------------------------------------
password = input ("Please Enter The Password >  ")



# -----------------------------------------------
# GENERATING HASH AND DESIGNATING UTF-8 ENCODING
# -----------------------------------------------
hash = hashlib.sha512()
hash.update(password.encode('utf-8'))
password_hash = hash.hexdigest()


# -----------------------------------------------
# PRINTING HASH TO CHECK IF ITS WORKING
# -----------------------------------------------
# comment out when running real program for debugging
# print ("Password is:  "+ password_hash)


# -----------------------------------------------
# TAKING USERS INPUT AND CHECKING IT AGAINST HASH
# -----------------------------------------------

if password_hash == storedPassword:
    print ("Password Correct! - Access Granted")

else:
    print ("Incorrect Password - Permission Denied")
