# Repeat question 2 using urllib. 
# Use the Module 11 slides as reference and save your program as M11_p3.py.

# Write a program M11_p2.py that uses sockets to read romeo-full.txt from data.pr4e.org and prints 
# the 10 most frequent words in the text. You can use techniques you learned in earlier modules, 
# but you must not save the file on your computer. You must also clean the text before counting 
# its words by replacing hyphens with spaces, and the character sequence apostrophe-s-space with 
# a single space (i.e. replace "Romeo's " with "Romeo "). Use the Module 11 slides as a reference 
# and remember that data is transferred across a network as bytes. Hint: To access a tuple element 
# in a list of tuples (L) use the tuple index, t, and the tuple element index, e: L[t][e]. 

# Example: if L = [('a',1), ('b',2), ('c',3)], L[2][1] returns 3 and L[1][0] returns 'b'.

import urllib.request
import string

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo-full.txt")
dict = {}
for line in fhand:
    text = line.decode()
    cleaned_text = text.replace("-", " ").replace("'s"," ")
    cleaned_text = cleaned_text.translate(str.maketrans('', '', string.punctuation))
    for word in cleaned_text.lower().split():
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    sorted_dict = sorted(dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

for word, freq in sorted_dict[:10]:
    print(f"{word} {freq}")