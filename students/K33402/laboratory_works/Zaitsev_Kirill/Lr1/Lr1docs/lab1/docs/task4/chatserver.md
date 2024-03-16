```python
import socket
import threading

# Создаем TCP сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Слушаем подключения
server_socket.listen(5)
print("Server is listening for incoming connections...")

# Словарь для хранения имен клиентов и их соответствующих соксетов
clients = {}


def handle_client(client_socket):
    # Запрос имени у клиента
    client_socket.send("Enter your name: ".encode('utf-8'))
    name = client_socket.recv(1024).decode('utf-8')

    # Проверка уникальности имени
    while name in clients:
        client_socket.send("Name already in use. Enter another name: ".encode('utf-8'))
        name = client_socket.recv(1024).decode('utf-8')

    clients[name] = client_socket

    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = data.decode('utf-8')
            print(f"{name}: {message}")

            # Отправляем сообщение всем другим клиентам
            for other_name, other_client in clients.items():
                if other_name != name:
                    other_client.send(f"{name}: {message}".encode('utf-8'))
        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Удаляем клиента из списка после отключения
    del clients[name]
    client_socket.close()


while True:
    # Принимаем клиентское соединение
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Создаем отдельный поток для каждого клиента
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

```