# Program that checks if a word is a palindrome.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

word = input("Enter a word: ")
isPal = True

wordLen = len(word)
for i in range(wordLen//2):
   if (word[i] != word[wordLen-i-1]):
      isPal = False
      break
      
if isPal:
   print(f"{word} is a palindrome.")
else:
   print(f"{word} is not a palindrome.")