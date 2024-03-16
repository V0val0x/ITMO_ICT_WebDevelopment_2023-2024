```python
import socket
import threading

# Создаем TCP сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 12345)

# Подключаемся к серверу
client_socket.connect(server_address)

# Запрашиваем имя у пользователя
name = input("Enter your name: ")
client_socket.send(name.encode('utf-8'))


def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024)
            message = data.decode('utf-8')
            print(message)
        except Exception as e:
            print(f"An error occurred: {e}")
            break


# Создаем поток для приема сообщений от сервера
receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

while True:
    message = input()
    client_socket.send(message.encode('utf-8'))

```