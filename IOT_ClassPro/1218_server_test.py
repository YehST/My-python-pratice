import socket
addr = socket.getaddrinfo('172.20.10.5', 80)[0][-1]

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  # 設定 socket 位址可重複使用
s.bind(addr)  # Server socket 綁定本身 AP 的網址與 80 埠
s.listen(5)  # 設定連線等候佇列最大連線數目為 5
print('listening on', addr)
html = """<html><head> <title>ESP Web Server</title> <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="icon" href="data:,"> <style>html{font-family: Helvetica; display:inline-block; margin: 0px auto; text-align: center;}
  h1{color: #0F3376; padding: 2vh;}p{font-size: 1.5rem;}.button{display: inline-block; background-color: #e7bd3b; border: none;
  border-radius: 4px; color: white; padding: 16px 40px; text-decoration: none; font-size: 30px; margin: 2px; cursor: pointer;}
  .button2{background-color: #4286f4;}</style></head><body> <h1>ESP Web Server</h1>
  <p>GPIO state: <strong></strong></p><p><a href="/?led=on"><button class="button">ON</button></a></p>
  <p><a href="/?led=off"><button class="button button2">OFF</button></a></p></body></html>"""
while True:
    cs, addr = s.accept()  # 等候連線進來, 接受後傳回與該連線通訊之新 socket 與遠端位址
    print('client connected from', addr)  # 輸出遠端網址
    cs.send(html)  # 以網頁回應遠端客戶
    cs.close()  # 關閉新 socket

s.close()  # 關閉 Server socket
