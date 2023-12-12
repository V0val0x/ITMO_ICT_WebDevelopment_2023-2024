import socket

# Создаем UDP сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Устанавливаем адрес и порт сервера
server_address = ('localhost', 12345)

# Отправляем сообщение серверу
message = "Hello, server"
client_socket.sendto(message.encode('utf-8'), server_address)

# Получаем ответ от сервера
data, _ = client_socket.recvfrom(1024)
print(data.decode('utf-8'))

# Закрываем соединение
client_socket.close()
