# Program that that uses sockets to read the file "romeo-full.txt" from the 
# server data.pr4e.org and saves it on the computer.
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

file = open("romeo-full.txt", "w")
file.write(text)
file.close()