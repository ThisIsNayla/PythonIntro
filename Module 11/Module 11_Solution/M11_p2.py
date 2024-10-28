# Program that that uses sockets to read the file "romeo-full.txt" from the 
# server data.pr4e.org and prints the 10 most frequent words in the text. 
#
# Copyright (c) 2022 Mazen A. R. Saghir
# Department of Electrical and Computer Engineering
# American University of Beirut

import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(("data.pr4e.org",80))
cmd = "GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n".encode()
mysock.send(cmd)
text = b""
while True:
    data = mysock.recv(512)
    if len(data) < 1:
       break
    text = text + data
mysock.close()

pos = text.find(b"\r\n\r\n")
text = text[pos+4:].decode()

delimiter = "[],.;-?!:"
dict = {}

cleanText = text.replace("-"," ")
text = cleanText

cleanText = text.replace("\'s "," ")
text = cleanText

for word in text.lower().split():
   cleanWord = ""
   for c in word:
      if c not in delimiter:
         cleanWord += c

   if cleanWord in dict:
      dict[cleanWord] += 1
   else:
      dict[cleanWord] = 1

t = list()
for k, v in list(dict.items()):
  t.append((v,k))

t.sort(reverse=True)
for i in range(10):
   print(f"{t[i][1]} {t[i][0]}")