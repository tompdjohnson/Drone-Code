# Drone-Code
This is a repository that holds some of the code I will be developing for use in a experimetnal police drone project.  

The Drone consists of two Raspberry PI's which control a number of onboard systems.

Raspberry Pi Number 1 will control motion, hardware devices such as onboard jammer, high powered IR Illuminator, Siren & Strobes and a 200mw green laser jamming system. 

Raspberry Pi Number 2 will control an ALFA High powered WiFi adapter with a long range Yagi Uda Antenna. It will also have a full version of Kali Arm installed and configured with a second WiFi adapter to enable two way communication with the ciommand and control station via WPA2.

I will be developing a simple RSA communication system using Python which will serve as a second layer of protection if the WPA2 key is extracted and cracked.  This is unlikely as the drone will only be used for 60 minutes at a time.   

My aim is to create a lightweight RSA system without using publically available Python cryptographic modules which regulaly roles keys and salts.

Feel free to use any of my code to build your own for non profit device. 


PWM-GPIO-Testing.py
This is a program to test pulse width modulation of motors installed within the drone. 

