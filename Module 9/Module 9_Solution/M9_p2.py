# Program that that reads a user-specified text file and uses a dictionary 
# to print all duplicate words in the file and their corresponding counts.
# 
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

try:
   delimiter = ",.;?!:"
   d = {}
   
   filename = input("Enter file name: ")

   file = open(filename)
   for line in file:
      cleanLine = ""
      for c in line:
         if c in delimiter:
            c = ""
         cleanLine += c
      
      for word in cleanLine.lower().split():
         if word not in d.keys():
            d[word] = 1
         else:
            d[word] += 1
   
   print("Duplicate words:")
   sortedKeys = sorted(d)
   for k in sortedKeys:
      v = d[k]
      if v > 1:
         print(k, v)
         
   file.close()

except:
   print("File not found.")
   exit()