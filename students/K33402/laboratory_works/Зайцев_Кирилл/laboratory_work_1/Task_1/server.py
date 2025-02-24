import socket

# Создаем UDP сокет
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Устанавливаем адрес и порт для сервера
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# Ожидаем и обрабатываем запросы от клиента
while True:
    data, client_address = server_socket.recvfrom(1024)
    print(f"Received from {client_address}: {data.decode('utf-8')}")

    # Отправляем ответ клиенту
    response = "Hello, client"
    server_socket.sendto(response.encode('utf-8'), client_address)
