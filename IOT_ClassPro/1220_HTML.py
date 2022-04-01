import socket

url = 'http://swf.com.tw/openData/test.html'
_,_,host,path = url.spilt('/',3)

addr = socket.getaddrinfo(host,80)[0][-1]
s = socket.socket()
s.connect(addr)

httpHeader = b'''\
GET/{Path}HTTP/1.0\r
Host:{host}\r
User-Agent:MicroPython\r
\r
'''

s.send(httpHeader.format(path=path))