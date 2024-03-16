```python
import socket

# Создаем TCP сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт для сервера
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Слушаем подключения
server_socket.listen(5)
print("Waiting for a connection...")

while True:
    # Принимаем клиентское соединение
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address}")

    # Принимаем данные от клиента
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Received from client: {data}")

    # Разбираем данные, ожидая три числа (a, b, c)
    try:
        a, b, c = map(float, data.split())
    except ValueError:
        response = "Invalid input. Please enter three numbers separated by spaces."
    else:
        # Проверяем, являются ли числа решением теоремы Пифагора
        is_pythagorean = a**2 + b**2 == c**2
        response = "Yes, it is a Pythagorean triple." if is_pythagorean else "No, it is not a Pythagorean triple."

    # Отправляем ответ клиенту
    client_socket.send(response.encode('utf-8'))

    # Закрываем соединение с клиентом
    client_socket.close()


```