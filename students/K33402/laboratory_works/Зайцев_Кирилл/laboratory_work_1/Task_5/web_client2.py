import socket

# Адрес и порт сервера
server_address = ('localhost', 8080)


def send_get_request(path):
    # Создаем TCP сокет и подключаемся к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    # Отправляем GET-запрос на указанный путь
    request = f"GET {path} HTTP/1.1\r\nHost: {server_address[0]}\r\n\r\n"
    client_socket.send(request.encode('utf-8'))

    # Получаем и выводим ответ от сервера
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    # Закрываем сокет
    client_socket.close()


def send_post_request(data):
    # Создаем TCP сокет и подключаемся к серверу
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)

    # Отправляем POST-запрос с данными
    request = f"POST / HTTP/1.1\r\nHost: {server_address[0]}\r\nContent-Length: {len(data)}\r\n\r\n{data}"
    client_socket.send(request.encode('utf-8'))

    # Получаем и выводим ответ от сервера
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

    # Закрываем сокет
    client_socket.close()


# Примеры запросов:

# Отправляем GET-запрос для получения оценок
send_get_request('/')

# Отправляем POST-запрос для добавления оценки
send_post_request('Английский,2')

# Отправляем GET-запрос для проверки, что оценка добавлена
send_get_request('/')
