# Write a program M11_p2.py that uses sockets to read romeo-full.txt from data.pr4e.org and prints 
# the 10 most frequent words in the text. You can use techniques you learned in earlier modules, 
# but you must not save the file on your computer. You must also clean the text before counting 
# its words by replacing hyphens with spaces, and the character sequence apostrophe-s-space with 
# a single space (i.e. replace "Romeo's " with "Romeo "). Use the Module 11 slides as a reference 
# and remember that data is transferred across a network as bytes. Hint: To access a tuple element 
# in a list of tuples (L) use the tuple index, t, and the tuple element index, e: L[t][e]. 

# Example: if L = [('a',1), ('b',2), ('c',3)], L[2][1] returns 3 and L[1][0] returns 'b'.

import socket
import string

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))

cmd = 'GET /romeo-full.txt HTTP/1.0\r\nHost: data.pr4e.org\r\n\r\n'.encode()
mysocket.send(cmd)

text = b''
while True:
    chunk = mysocket.recv(512)
    if len(chunk) < 1:
        break
    text += chunk

mysocket.close()

text = text.decode()
cleaned_text = text.replace("-", " ").replace("'s", " ")
cleaned_text = cleaned_text.translate(str.maketrans('', '', string.punctuation))

word_dict = {}
for word in cleaned_text.lower().split():
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

sorted_dict = sorted(word_dict.items(), key=lambda x: (x[1], x[0]), reverse=True)

for word, freq in sorted_dict[:10]:
    print(f"{word} {freq}")