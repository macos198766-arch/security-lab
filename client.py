#клиентская часть

import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #создание TCP/IP сокета для клиента
client.connect(("0.0.0.0", 2222))

while True:
    msg = input() #запрос сообщения от пользователя

    client.sendall(msg.encode('utf-8')) #отправка сообщения клиента на сервер


client.close()