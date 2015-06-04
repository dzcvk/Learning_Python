import socket
host='127.0.0.1'
port=56789
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
buf=s.recv(2048)
print(buf.decode('utf-8'))
input('receive successfully')
