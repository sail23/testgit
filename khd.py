import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(('127.0.0.1',8712))
print(s.recv(1024).decode(encoding="utf8"))
s.send("连接了".encode("utf8"))
print(s.recv(1024).decode(encoding="utf8"))
input("")