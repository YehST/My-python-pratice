import pyfirmata
from time import sleep

LED = 13
PORT = "COM3"
board = pyfirmata.Arduino(PORT)
i = 0
i = input("input")
while True:
    board.digital[LED].write(1)
    sleep(1)
    board.digital[LED].write(0)
    sleep(1)
