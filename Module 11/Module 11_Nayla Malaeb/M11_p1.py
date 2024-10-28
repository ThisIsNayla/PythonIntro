# The file romeo-full.txt contains Act 2, Scene 2 from William Shakespeare's Romeo and Juliet. 
# Write a program M11_p1.py that uses sockets to read romeo-full.txt from the server data.pr4e.org 
# and saves it on your computer. Be sure to only save the contents of the file after removing the 
# HTTP header. Use the Module 11 slides as a reference and remember that data is transferred across 
# a network as bytes. Hint: You will need to use the decode() string method.

# USING URLLIB
# import urllib.request
# fhand = urllib.request.urlopen ('http://data.pr4e.org/romeo-full.txt')

# with open("romeo-full.txt", "w") as file:
#     for line in fhand:
#         file.write(line.decode().strip() + "\n")

# file.close()


# USING SOCKET
import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo-full.txt HTTP/1.0\r\n\r\n'.encode()
mysocket.send(cmd)

data = b''

while True:
    chunk = mysocket.recv(512)
    if len(chunk) < 1:
        break
    data += chunk

pos = data.find(b"\r\n\r\n")
print(data[pos+4:].decode())

mysocket.close()