import socket
from machine import Pin
led = Pin(2, Pin.OUT)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('172.20.10.5', 80))
print("已開通")

while True:
    req = s.recv(1024)
    print(str(req))
    led_on = req.find('/?led=on')
    led_off = req.find('/?led=off')
    if led_on == 6:
        print('LED OFF')
        led.value(0)
    else:
        print('LED ON')
        led.value(1)
