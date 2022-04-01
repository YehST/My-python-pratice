import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

print('已開通')
client, addr = s.accept()
print('用戶端位址:{},槴號:{}'.format(addr[0], addr[1]))


def web_page():
    if led_value == 1:
        gpio_state = 'OFF'
    else:
        gpio_state = 'ON'
    # html code ...
    html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
  <p>GPIO state: <strong>""" + gpio_state + """</strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
    return html


try:
    while True:
        client, addr = s.accept()
        print('Connection: %s' % str(addr))
        req = client.recv(1024)
        print('Connect = %s' % str(req), end='\n')
        req = str(req)
        led_on = req.find('/?led=on')
        led_off = req.find('/?led=off')
        if led_on == 6:
            print('LED OFF')
            led_value = 0
        else:
            print('LED ON')
            led_value = 1

        response = web_page()
        client.send(b'HTTP/1.1 200 OK\n')
        client.send(b'Content-Type: text/html\n')
        client.send(b'Connection: close\n\n')
        client.sendall(response.encode())
        client.close()
except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")
    client.close()
