# Program that generates a Ceasar ciphertext from a plaintext and rotation value.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

def rotateString(instr, rot):
  retstr = ""
  NUM_LETTERS = 26
  for c in instr:
     if c >= 'a' and c <= 'z':
        d = chr((ord(c) - ord('a') + rot)%NUM_LETTERS + ord('a'))
     elif c >= 'A' and c <= 'Z':
        d = chr((ord(c) - ord('A') + rot)%NUM_LETTERS + ord('A'))
     else:
        d = c
     retstr += d
  return retstr
   
instr = input("Enter plaintext: ")
rotval = int(input("Enter rotation value: "))
print("Ciphertext:", rotateString(instr, rotval))