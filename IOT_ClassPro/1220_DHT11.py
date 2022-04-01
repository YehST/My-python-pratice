from machine import Pin
import dht
import socket
d = dht.DHT11(Pin(2))

s = socket.socket()
HOST = '0.0.0.0'
POST = 80
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, POST))
s.listen(5)
print('Web server is running')
httpHeader = b'''\
    HTTP/1.0 200 OK
    <!doctype html>
    <html>
    <head>
        <meta charset = "utf-8">
        <title>ESP8266 Webserver</title>
    </head>
    <body>
        Temp:{temp}<br>
        Humid:{humid}
    </body>
    </html>
'''


def readDHT():
    d.measure()
    t = '{:02}\u00b0C'.format(d.temperature())
    h = '{:02}%'.format(d.humidity())
    return(t, h)


try:
    while True:
        client, _ = s.accept()
        temp, humid = readDHT()
        client.send(httpHeader.format(temp=temp, humid=humid))
        client.close()
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
    client.close()
