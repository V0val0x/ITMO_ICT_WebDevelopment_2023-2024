```python
import socket

# Создаем TCP сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 12345)
client_socket.connect(server_address)

# Вводим три числа (a, b, c)
a = float(input("Enter the first number (a): "))
b = float(input("Enter the second number (b): "))
c = float(input("Enter the third number (c): "))

# Отправляем данные серверу
message = f"{a} {b} {c}"
client_socket.send(message.encode('utf-8'))

# Получаем ответ от сервера
result = client_socket.recv(1024).decode('utf-8')
print(f"Server's response: {result}")

# Закрываем соединение
client_socket.close()

```