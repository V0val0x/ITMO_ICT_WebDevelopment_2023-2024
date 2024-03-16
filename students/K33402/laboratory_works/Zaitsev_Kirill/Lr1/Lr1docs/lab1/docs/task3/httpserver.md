```python
import socket
import threading
import os

# Путь к файлу index.html
html_file_path = "index.html"

# Создаем TCP сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 8080)
server_socket.bind(server_address)

# Слушаем подключения
server_socket.listen(1)
print("Server is listening on port 8080...")


def handle_client(client_socket):
    # Принимаем данные от клиента
    data = client_socket.recv(1024).decode('utf-8')

    if "GET / HTTP/1.1" in data:
        # Отправляем содержимое файла index.html
        if os.path.exists(html_file_path):
            with open(html_file_path, 'r') as file:
                content = file.read()
                response = f"HTTP/1.1 200 OK\r\nContent-Type: text/html\r\n\r\n{content}"
        else:
            response = "HTTP/1.1 404 Not Found\r\n\r\nFile not found"
    else:
        # Если запрос не соответствует ожидаемому, отправляем ошибку
        response = "HTTP/1.1 400 Bad Request\r\n\r\nBad Request"

    # Отправляем ответ клиенту
    client_socket.send(response.encode('utf-8'))
    client_socket.close()


while True:
    # Принимаем клиентское соединение
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Создаем отдельный поток для каждого клиента
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()

```