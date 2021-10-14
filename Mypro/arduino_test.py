from pyfirmata import Arduino, SERVO
from time import sleep

port = 'COM3'
board = Arduino(port)
sleep(5)

pin = 9
board.digital[pin].mode = SERVO


def setServo(pin, angle):
    board.digital[pin].write(angle)
    sleep(0.015)


i = input("push y to continue")
if i == "1":
    setServo(pin, 70)
    print('servo go ')
    pass
else:
    board.exit()
