import socket
import psutil

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host,port))
s.send('mem')

print s.recv(1024)
s.close()
