# This file is executed on every boot (including wake-boot from deepsleep)
import esp
import uos
import machine
# uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
import socket
from machine import Pin, Timer
import time

# === Init === #
Ain1 = Pin(4, Pin.OUT)  # Motor A 訊號1
Ain2 = Pin(5, Pin.OUT)  # Motor A 訊號2
Bin1 = Pin(0, Pin.OUT)  # Motor B 訊號1
Bin2 = Pin(2, Pin.OUT)  # Motor B 訊號2
trig = Pin(13, Pin.OUT)  # 超音波感測器 訊號發送
echo = Pin(15, Pin.IN)  # 超音波感測器 訊號接收
Ain1.off()
Ain2.off()
Bin1.off()
Bin2.off()
# === End Line === #

# === Global Variable === #
run_flag = True
distance = 0
# === End Line ========== #

# === (Move) Function Section === #


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


def Forward_Con():
    Ain2.on()
    Bin2.on()
    Ain1.off()
    Bin1.off()


def R_Turn_Con():
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.on()


def L_Turn_Con():
    Ain1.off()
    Ain2.on()
    Bin1.off()
    Bin2.off()


def Backward_Con():
    Bin1.on()
    Bin2.off()
    Ain1.on()
    Ain2.off()


def Stop():
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()
# === End Line === #

# === Wifi Section === #


def connectAP(ssid, pwd):
    import network

    wlan = network.WLAN(network.STA_IF)

    if not wlan.isconnected():
        wlan.active(True)
        wlan.connect(ssid, pwd)

        while not wlan.isconnected():
            pass
    print('network config :\n', wlan.ifconfig())


esp.osdebug(None)
webrepl.start()
gc.collect()
#connectAP('yiyi_890313', '0902313888')
connectAP('Zozoo', 'kinfe777')
# === End Line === #

# === WebSocket(Server) === #
server_s = socket.socket()
server_host = '172.20.10.12'
server_port = 80
server_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_s.bind((server_host, server_port))
server_s.listen(5)
print('===== Server Open =====')
# === End Line === #

# === Send Distance === #


def send_dist_to_web(x):
    global distance
    client_s = socket.socket()
    client_s.connect(('172.20.10.2', 7788))
    client_s.send(str(distance).encode('utf-8'))
    client_s.close()
# === End Line ======== #

# === Sensor Distance === #


def ping(x):
    global run_flag
    global distance
    dist = 0
    trig.value(1)
    time.sleep_us(10)
    trig.value(0)
    count = 0
    timeout = False
    start = time.ticks_us()
    while not echo.value():  # wait for HIGH
        time.sleep_us(10)
        count += 1
        if count > 100000:  # over 1s timeout
            timeout = True
            break
    if timeout:
        duration = 0  # timeout return 0
    else:  # got HIGH pulse:calculate duration
        count = 0
        start = time.ticks_us()
        while echo.value():  # wait for LOW
            time.sleep_us(10)
            count += 1
            if count > 2320:
                break  # over 400cm range:
        duration = time.ticks_diff(time.ticks_us(), start)
        dist = round(duration/58)  # 距離
    print(dist)
    if dist <= 50:
        run_flag = False
    else:
        run_flag = True
    distance = dist


timer1 = Timer(1)
timer1.init(period=200, mode=Timer.PERIODIC, callback=ping)
timer2 = Timer(1)
timer2.init(period=500, mode=Timer.PERIODIC, callback=send_dist_to_web)
# === End Line === #

# === Main Section === #
while True:
    client, addr = server_s.accept()
    print("Client Address:", addr)

    req = client.recv(1024).decode('utf-8')
    data = req[len(req)-1]
    print(data)
    if data and run_flag:
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
    client.close()
# === End Line === #
