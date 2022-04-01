import time
from machine import Pin,Timer

Ain1 = Pin(4, Pin.OUT)
Ain2 = Pin(5, Pin.OUT)
Bin1 = Pin(0, Pin.OUT)
Bin2 = Pin(2, Pin.OUT)
Ain1.off()
Ain2.off()
Bin1.off()
Bin2.off()
trig=Pin(13, Pin.OUT)
echo=Pin(15, Pin.IN)


def Forward():
    Ain2.on()
    Bin2.on()
    Ain1.off()
    Bin1.off()
def R_Turn():
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.on()
    time.sleep(1)
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()
def L_Turn():
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

def ping(x):
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count=0
    timeout=False
    start=time.ticks_us()
    while not echo.value(): #wait for HIGH
        time.sleep_us(10)
        count += 1
        if count > 100000: #over 1s timeout
            timeout=True
            break
    if timeout: #timeout return 0
        duration=0
    else: #got HIGH pulse:calculate duration
        count=0
        start=time.ticks_us()
        while echo.value(): #wait for LOW
            time.sleep_us(10)
            count += 1
            if count > 2320: #over 400cm range:quit
                break
        duration=time.ticks_diff(time.ticks_us(), start)
        duration=round(duration/58)
        print('%scm' % duration)
timer1=Timer(1)
timer1.init(period=500, mode=Timer.PERIODIC, callback=ping)
#while True:
    #distance=round(ping(trigPin=13,echoPin=15)/58)
    #print('%scm' % distance)
while True:
    #client, addr = get_s.accept()
    #print("Client Address:", addr)
    #req = client.recv(1024).decode('utf-8')
    #data = req[len(req)-1]
    #distance=round(ping(trigPin=13,echoPin=15)/58)
    data = input('command:')
    print("Request:\n", data)
    if data:
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
        elif data == 'Q':
            Backward_Con()
        elif data == 'O':
            Stop()
    else:
        Stop()
        timer1.deinit()