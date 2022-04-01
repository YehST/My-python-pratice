from machine import Pin, Timer
import urequests as req
import dht
import time

d = dht.DHT11(Pin(2))
running = True

apiURL = '{url}?key={key}'.format(
    url='http://api.thingspeak.com/update',
    key='5NBHZGH5AS4NBY9M'
)


def sendDHT(t):
    global apiURL, running

    try:
        d.measure()
    except OSError as e:
        print(e)
        return
    apiURL += '&field1={temp}&field={humid}'.format(
        temp=d.temperature(),
        humid=d.humidity()
    )

    r = req.get(apiURL)

    if r.status_code != 200:
        t.deinit()
        print('Bad request error')
        running = False
    else:
        print('Data saved , id:', r.text)


tim = Timer(-1)
tim.init(period=20000, mode=Timer.PERIODIC, callback=sendDHT)

try:
    while running:
        pass
except:
    tim.deinit()
    print('stoppp')
