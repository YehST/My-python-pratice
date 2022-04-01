from machine import Pin
import time

Ain1 = Pin(4, Pin.OUT)
Ain2 = Pin(5, Pin.OUT)
Bin1 = Pin(0, Pin.OUT)
Bin2 = Pin(2, Pin.OUT)
  # B Motor Speed Adjust
Ain1.off()
Ain2.off()
Bin1.off()
Bin2.off()
try:
    while True:
        Ain2.on()
        Bin2.on()
        print(1)
        time.sleep(2)
        Ain1.off()
        Ain2.off()
        Bin1.off()
        Bin2.off()
        print(0)
        time.sleep(2)
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
    Ain1.off()
    Ain2.off()
    Bin1.off()
    Bin2.off()
        
