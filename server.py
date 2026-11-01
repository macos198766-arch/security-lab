import threading
import socket



def handle_client(client_socket, address):
    print(f"client {address} connected")
    try:
        while True:
            data = client_socket.recv(1024)
        
            if not data:
                break

            text = data.decode('utf-8')
            print(text)

            client_socket.sendall(data)

    except ConnectionResetError:
        print('off')
    finally:
        client_socket.close()

        
def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:   
        server_address = (host, port)
        server_socket.bind(server_address)
        server_socket.listen(5)
        print('ok')
    except OSError:
        print('not ok')
        return
    try:

        while True:
            client_socket, address = server_socket.accept()
            t = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
             daemon=True
            )
            t.start()
    except KeyboardInterrupt:
        print('-')
    finally:
        server_socket.close()


if __name__ == "__main__":
    start_server("localhost", 8000)
