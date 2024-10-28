# Program that prints and counts all words that have a specific length in a file.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

try:
   filename = input("Enter file name: ")
   file = open(filename)

   wordlen = int(input("Enter word length: "))
   if wordlen <= 0:
      print("Invalid input.")
   else:
      count = 0
      for line in file:
         cleanline = ""
         for char in line:
            if not char in ",;.:?":
               cleanline = cleanline + char
         for word in cleanline.split():
            if len(word) == wordlen:
               print(word)
               count = count + 1
      print(f"Total words of length {wordlen}: {count}")
except:
   print(f"File \'{filename}\' not found.")