# Program that that uses the urllib module to read the file "romeo-full.txt" from the 
# server data.pr4e.org and print the 10 most frequent words.
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

import urllib.request

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo-full.txt")

# Delimiter string
delimiter = "[],.;-?!:"
# Create an empty dictionary
dict = {}

for line in fhand:
   # Convert bytes to UTF-8
   text = line.decode()

   # Clean text by replacing hyphens and apostrophe-s with spaces.
   cleanText = text.replace("-"," ")
   text = cleanText

   cleanText = text.replace("\'s "," ")
   text = cleanText

   for word in text.lower().split():
      cleanWord = ""
      for c in word:
         # If current character is not in a delimiter add it to the text
         if c not in delimiter:
            cleanWord += c

      # If the word is already in the dictionary increment its count. Otherwise initialize it to 1.
      if cleanWord in dict:
         dict[cleanWord] += 1
      else:
         dict[cleanWord] = 1

 # Create a list of value, key pairs to simplify sorting.
t = list()
for k, v in list(dict.items()):
  t.append((v,k))

# Sort the list in reverse order
t.sort(reverse=True)
# Print the words with the 10 highest frequency counts.
for i in range(10):
   print(f"{t[i][1]} {t[i][0]}")