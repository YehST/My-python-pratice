from machine import Pin
import time
#import socket
print("start..")
'''____________________________Web Connect________________________________'''
'''
host = '172.20.10.12'
path = 'esp8266'

addr = socket.getaddrinfo(host, 1880)[0][-1]
s = socket.socket()
s.connect(addr)

httpHeader = b''\
GET/{path} HTTP/1.0\r
Host:{host}\r
User-Agent:MicroPython\r
\r
''

s.send(httpHeader.format(path=path, host=host))
'''
'''____________________________Motor Control________________________________'''
Ain1 = Pin(4, Pin.OUT)
Ain2 = Pin(5, Pin.OUT)
Bin1 = Pin(0, Pin.OUT)
Bin2 = Pin(2, Pin.OUT)
Ain1.off()
Ain2.off()
Bin1.off()
Bin2.off()


def Forward():
    Ain2.on()
    Bin2.on()
    Ain1.off()
    Bin1.off()
    time.sleep(1)
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()


def L_Turn():
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.on()
    time.sleep(1)
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()


def R_Turn():
    Ain1.off()
    Ain2.on()
    Bin1.off()
    Bin2.off()
    time.sleep(1)
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()


def Backward():
    Bin1.on()
    Bin2.off()
    Ain1.on()
    Ain2.off()
    time.sleep(1)
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()


def Forward_Con():
    Ain2.on()
    Bin2.on()
    Ain1.off()
    Bin1.off()


def L_Turn_Con():
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.on()


def R_Turn_Con():
    Ain1.off()
    Ain2.on()
    Bin1.off()
    Bin2.off()


def Backward_Con():
    Bin1.on()
    Bin2.off()
    Ain1.on()
    Ain2.off()


def Command():
    pass


def Stop():
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()
print("start...")

'''____________________________Major Program________________________________'''
while True:
    data = input("input:")
    if data == 'F':
        Forward()
    elif data == 'L':
        L_Turn()
    elif data == 'R':
        R_Turn()
    elif data == 'B':
        Backward()
    elif data == 'A':
        Forward_Con()
    elif data == 'S':
        L_Turn_Con()
    elif data == 'D':
        R_Turn_Con()
    elif data == 'F':
        Backward_Con()
    else:
        Stop()


#s.close()
