import socket
url = 'http://swf.com.tw/openData/test.html'
_, _, host, path = url.split('/', 3)

addr = socket.getaddrinfo(host, 80)[0][-1]
s = socket.socket()
s.connect(addr)

httpHeader = b'''\
GET/{path} HTTP/1.0\r
Host:{host}\r
User-Agent:MicroPython\r
\r
'''

s.send(httpHeader.format(path=path, host=host))

while True:
    data = s.recv(128)
    if data:
        print(str(data, 'utf8'), end='')
    else:
        break

s.close()
