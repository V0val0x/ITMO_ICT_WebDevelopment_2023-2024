import http.client

# Адрес и порт сервера
SERVER_ADDRESS = "localhost:8080"


def send_get_request(path="/"):
    # Создаем соединение с сервером
    conn = http.client.HTTPConnection(SERVER_ADDRESS)

    # Отправляем GET-запрос
    conn.request("GET", path)

    # Получаем и выводим ответ от сервера
    response = conn.getresponse()
    print(response.read().decode('utf-8'))

    conn.close()


def send_post_request():
    # Запрашиваем данные о дисциплине и оценке с клавиатуры
    discipline, grade = input("Введите дисциплину и оценку через пробел: ").split()
    data = f"{discipline}, {grade}"

    # Создаем соединение с сервером
    conn = http.client.HTTPConnection(SERVER_ADDRESS)

    # Преобразуем данные в байты с использованием UTF-8 кодировки
    data = data.encode('utf-8')

    # Отправляем POST-запрос с данными
    headers = {'Content-type': 'text/plain; charset=utf-8'}
    conn.request("POST", "/", data, headers)

    # Получаем и выводим ответ от сервера
    response = conn.getresponse()
    print(response.read().decode('utf-8'))

    conn.close()


# Примеры запросов:

# Отправляем GET-запрос для получения оценок
send_get_request()

# Отправляем POST-запрос для добавления оценки
send_post_request()

# Отправляем GET-запрос для проверки, что оценка добавлена
send_get_request()
