import socket
host='127.0.0.1'
port=56789
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
clientSocket,clientAddr =s.accept()
print('client connected')
clientSocket.sendall(b'welcome to python world')
clientSocket.close()
input('send successfully')
