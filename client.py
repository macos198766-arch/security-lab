import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 8000))

while True:
    msg = input("Сообщение: ")

    client.sendall(msg.encode('utf-8'))

    response = client.recv(1024)
    print(response.decode('utf-8'))

client.close()