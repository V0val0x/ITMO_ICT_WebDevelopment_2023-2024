import socket

# Создаем TCP сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера, к которому хотим подключиться
server_address = ('localhost', 8080)

try:
    # Подключаемся к серверу
    client_socket.connect(server_address)

    # Формируем HTTP-запрос
    request = "GET / HTTP/1.1\r\nHost: localhost\r\n\r\n"

    # Отправляем запрос серверу
    client_socket.sendall(request.encode('utf-8'))

    # Получаем ответ от сервера и выводим его
    response = client_socket.recv(1024).decode('utf-8')
    print(response)

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Закрываем соединение с сервером
    client_socket.close()
