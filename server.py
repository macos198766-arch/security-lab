import threading
import socket
import logging
import sys

#создание и настойка логгера
file_handler = logging.FileHandler("app.log", encoding="utf-8")
console_handler = logging.StreamHandler(sys.stdout)

logging.basicConfig(
level=logging.INFO,
format='%(asctime)s – %(name)s – %(levelname)s – %(message)s'
)

logging.info('Сервер запущен успешно')



def handle_client(client_socket, address): #функция, которая выполняется в потоке
    logging.info(f"client {address[0]}:{address[1]} connected")

    try:
        while True:
            data = client_socket.recv(1024) #получение данных от пользователя
        
            if data: 
                text = data.decode('utf-8', errors='ignore') #декодировать данные в читаемую кодировку
                logging.info(text) #записать данные от клиента в лог файл


    except ConnectionResetError as e: 
        logging.warning(f"{e}: Соединение разорвано принудительно клиентом")
    finally:
        client_socket.close() #закрыть сокет клиента

        
def start_server(host, port): #создание TCP/IPv4 сервера; создание потока
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:   
        server_address = (host, port)
        server_socket.bind(server_address)
        server_socket.listen(5)
        logging.info(f"Сервер создан успешно на {host}:{port}")
    except OSError as e:
        logging.warning(f"{e}: Данный порт занят")
        return
    try:
        while True:
            client_socket, address = server_socket.accept() #получение айпи и порта клиента
            t = threading.Thread( #создание потока
                target=handle_client,
                args=(client_socket, address),
             daemon=True
            )
            t.start() #запуск потока
    except KeyboardInterrupt as e:
        logging.warning(f"{e}: Сервер выключен")
    finally:
        server_socket.close()


if __name__ == "__main__": #запуск программы
    start_server("0.0.0.0", 2222) 