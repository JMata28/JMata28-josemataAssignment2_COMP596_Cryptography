#This is the answer for Question #4 of Assignment 2 of the class COMP 596 - Cryptography

"""
The explanation for RC4 and process implemented was obtained from the following sources: 
https://www.youtube.com/watch?v=1UP56WM4ook
https://www.youtube.com/watch?v=lRyzKIvxNdM 
"""

print("Welcome to José Mata's RC4 Implementer")
S = [] #Create a python list (basically an array) that is empty
i = 0 #i is used as a counter in the while loop below
while i <= 255: #This loop fills up the list with the digits from 0 to 255
    S.append(i)
    i = i +1
key = "thisiskey"  #this is the key that will be used 
keyinascii = []
for letter in key: #this loops through each character in the string named "key", converts it to ascii, and appends each as a spearate item to the list "keyinascii". Code derived from code on this page: https://www.geeksforgeeks.org/python-convert-string-list-to-ascii-values/
    keyinascii.append(ord(letter))

K = [] #list k will have the key in ascii repeated until there are 256 items in the list
p = 0  #will be used as counter
x = 0  #will be used as counter
while p <= 255:  #this loop fills up the list k with the values of "keyinascii" until there are 256 items in the list
    K.append(keyinascii[x])
    if x == (len(keyinascii)-1):
        x = 0
    else:
        x = x+1 
    p = p +1


""" The section of code blow implements the "key scheduling". The pseudocode for this section was obtained from https://www.youtube.com/watch?v=1UP56WM4ook
In summary, what this section does is that it rearranges the elements in list S. It uses tha value of the elements themselves and the values in the K list
to determine which items will be swapped.  """
j = 0
l = 0
while l <= 255:
    j = (j + S[l] + K[j])%256
    S[l], S[j] = S[j], S[l] #This line of code was derived from the code found here: https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
    l = l+1

''' The section of the code below implements the pseudo-random generation algorithm. The pseudocode for this section was obtained from https://www.youtube.com/watch?v=1UP56WM4ook
    In summary, this section is meant to produce the keystream. First, this section rearranges the elements in list S (but only up until the lenght of the plaintext). 
    It uses tha value of the elements themselves to determine which items will be swapped. 
    Then the value t is produced based on the values swapped in list S and value t is added to the keystream. 
'''
j = 0
l = 1
keystream = []
plaintext = "success"
print("The plaintext BEFORE ENCRYPTION is: ", plaintext)
while l <= len(plaintext):
    j = (j + S[l])%256
    S[l], S[j] = S[j], S[l] #This line of code was derived from the code found here: https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
    t = (S[l] + S[j])%256
    keystream.append(S[t])
    l = l+1
print("The keystream produced in decimal notation is: ", keystream)

#The section of code below produces the cyphertext by XOR'ing the plaintext and the keystream
plaintextinascii = []
for letter in plaintext: #this loops through each character in the string named "plaintext", converts it to ascii, and appends each as a spearate item to the list "plaintextinascii". Code derived from code on this page: https://www.geeksforgeeks.org/python-convert-string-list-to-ascii-values/
    plaintextinascii.append(ord(letter))
print("The original plaintext in decimal notation BEFORE ENCRYPTION is: ", plaintextinascii)
cyphertext = []
y = 0 
while y < len(plaintextinascii):
    cyphertext.append(plaintextinascii[y] ^ keystream[y])
    y = y + 1
print("The cypher text in decimal notation is: ", cyphertext)

#The section of code below produces the plaintext by XOR'ing the cyphertext and the keystream
decryptedplaintext = []
y = 0 
while y < len(cyphertext):
    decryptedplaintext.append(cyphertext[y] ^ keystream[y])
    y = y + 1
print("The plaintext in decimal notation AFTER DECRYPTION is: ", decryptedplaintext)
finalplaintext = "" 
for val in decryptedplaintext:  #This loops through each item of the list "decryptedplaintext", turns it into a character, and appends it to the string naned "finalplaintext". This code was derived from doe found here: https://www.geeksforgeeks.org/python-ways-to-convert-list-of-ascii-value-to-string/
    finalplaintext = finalplaintext + chr(val)  
print("The final plaintext AFTER DECRYPTION is: ", finalplaintext)