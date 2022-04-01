from machine import Pin,PWM
import time

C0=18
CS0=17
D0=18
DS0=19
E0=21
F0=22
FS0=23
G0=25
GS0=26
A0=28
AS0=29
B0=31
C1=33
CS1=35
D1=37
DS1=39
B0=31
C1=33
CS1=35
D1=37
DS1=39
E1=41
F1=44
FS1=46
G1=49
GS1=52
A1=55
AS1=58
B1=62
C2=65
CS2=69
D2=73
DS2=78
E2=82
F2=87
FS2=93
G2=98
GS2=104
A2=110
AS2=117
B2=123
C3=131
CS3=139
D3=147
DS3=156
E3=165
F3=175
FS3=185
G3=196
GS3=208
A3=220
AS3=233
B3=247
C4=262
CS4=277
D4=294
DS4=311
E4=330
F4=349
FS4=370
G4=392
GS4=415
A4=440
AS4=466
B4=494
C5=523
CS5=554
D5=587
DS5=622
E5=659
F5=698
FS5=740
G5=784
GS5=831
A5=880
AS5=932
B5=988

note=(G5, E5, E5, 0, F5, D5, D5, 0, C5, D5, E5, F5, G5, G5, G5, 0,
      G5, E5, E5, 0, F5, D5, D5, 0, C5, E5, G5, G5, E5, 0, 0, 0,
      D5, D5, D5, D5, D5, E5, F5, 0, E5, E5, E5, E5, E5, F5, G5, 0,
      G5, E5, E5, 0, F5, D5, D5, 0, C5, E5, G5, G5, C5, 0, 0, 0)
duration=(4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
          4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
          4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4,
          4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4)

def tone(pwm,note,duration):
    pwm.freq(note)          
    pwm.duty(512)
    time.sleep_ms(duration)
    pwm.deinit()

def littleBee(pwm):
    for i in range(0,len(note)):
        d=int(1000/duration[i])
        tone(pwm, note[i], d)
        p=int(d*0.9)
        time.sleep_ms(p)
    time.sleep(2)

pwm=PWM(Pin(4))

while True:
    littleBee(pwm)