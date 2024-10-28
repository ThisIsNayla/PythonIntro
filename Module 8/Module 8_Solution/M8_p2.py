# Program that prints all permutations of a word in capital letters 
# and the number of possible permutations.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

import itertools
word = input("Please enter word: ")

perms = itertools.permutations(word.upper())
count = 0
for p in perms:
   w = ""
   for i in p:
      w += i
   count += 1
   print(w)
print("Total permutations =",count)