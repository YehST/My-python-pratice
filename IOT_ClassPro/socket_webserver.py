import socket

s = socket.socket()
HOST = '0.0.0.0'
PORT = 80
httpHeader = b'''\
HTTP/1.0 200 OK
    
    
Welcome to MicroPython
'''

s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))
s.listen(5)
print('on port:', PORT)

while True:
    client, addr = s.accept()
    print('client add', addr)
    req = client.recv(1024)
    client.send(httpHeader)
    client.close()
    print("----------------")
