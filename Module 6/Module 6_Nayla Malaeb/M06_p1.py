# In cryptography, the Caesar cipher is a simple and widely used encryption technique. 
# It is a type of substitution cipher in which each letter of an input plaintext is replaced by a 
# letter that is at a fixed number of positions up or down the alphabet. For example, with a left shift 
# of 3, the letter 'D' would be replaced by an 'A'; the letter 'E' would become a 'B', and so on. 
	
# The transformation can be represented by aligning two alphabets; the plain alphabet and the cipher 
# alphabet, which is the plain alphabet rotated left or right by some number of positions. For example, 
# here is a Caesar cipher using a left rotation of three characters, which is equivalent to a right shift 
# of 23 characters:  
	
# Using this cipher, the plaintext: THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG becomes the ciphertext: 
# QEB NRFZH YOLTK CLU GRJMP LSBO QEB IXWV ALD. 
	
# Caesar cipher encryption can be represented using modular arithmetic by first transforming letters 
# into numbers according to the scheme: A = 0, B = 1, ... Z = 25. Encrypting a letter x rotated by n 
# characters can be described mathematically as: En(x) = (x + n) % 26. 
	
# In Python, a character can be converted to its UTF-8 code using the ord() function. Conversely, 
# the character for a given UTF-8 code can be generated using the chr() function. For example, 
# ord('a') = 97 and chr(97) = 'a'. Moreover, expressions like ord('d') - ord('a') return the difference 
# in the number of characters between 'a' and 'd'. 
	
# Write a program M06_p1.py that asks the user to enter a plaintext and a rotation value, and that 
# returns the corresponding Caesar cipher ciphertext. The rotation value can be any positive or 
# negative integer, and the plaintext may include lowercase, uppercase, or nonalphabetic characters 
# (e.g. punctuation marks, white space, and digits). A negative rotation value corresponds to a left 
# rotation, and a positive rotation value corresponds to a right rotation. 
	
# Your program should use a function rotateString that takes two parameters: instr and rot, which 
# correspond to the input plaintext and rotation value, respectively. The function should return 
# the ciphertext string. 

# Example:  
# Enter plaintext: Hello, world! 
# Enter rotation value: -2 
# Ciphertext: Fcjjm, umpjb! 

def rotateString(instr, rot):
    ciphertext = ""
    for char in instr:
        if char.isalpha():
            if char.isupper():
                base = ord('A')
                difference = ord(char) - base
            else: 
                base = ord('a')
                difference = ord(char) - base
            ciphertext += (chr((difference + rot) % 26 + base))
        else:
            ciphertext += char
    return ciphertext

plaintext = str(input("Enter plaintext: "))
rotation = int(input("Enter rotation value: "))

ciphertext = rotateString(plaintext, rotation)
print(f"Ciphertext: {ciphertext}")