import socket
##TCP_IP = '127.0.0.1'
##TCP_PORT = 25
TCP_IP = '10.0.0.16'
TCP_PORT = 1973
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

b = bytes(MESSAGE, 'utf-8')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(b)
##print("hi")
##data = s.recv(BUFFER_SIZE)
s.close()
##
##print ("received data:", data)
