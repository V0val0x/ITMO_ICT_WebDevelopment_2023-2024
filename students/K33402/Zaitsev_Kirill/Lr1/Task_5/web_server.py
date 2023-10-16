import http.server
import socketserver

# Устанавливаем порт, на котором будет работать сервер
PORT = 8080


# Создаем обработчик запросов для сервера
class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        # Обрабатываем POST-запрос
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        # Добавляем данные в файл grades.txt
        with open('grades.txt', 'a') as file:
            file.write(post_data + '\n')

        # Отправляем клиенту ответ
        self.send_response(200)
        self.end_headers()
        self.wfile.write(bytes("Data received and saved.", 'utf-8'))

    def do_GET(self):
        # Обрабатываем GET-запрос
        if self.path == '/':
            # Открываем файл grades.txt и читаем данные из него
            with open('grades.txt', 'r') as file:
                data = file.read()

            # Генерируем HTML-страницу на основе данных из файла
            html = f"""
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN">
            <html>
            <head>
                <title>Оценки</title>
            </head>
            <body>
                <h1>Оценки</h1>
                <p>{data}</p>
            </body>
            </html>
            """

            # Отправляем клиенту HTML-страницу
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode('utf-8'))
        else:
            # Если запрос не на корневой URL, обработка не поддерживается
            self.send_response(404)
            self.end_headers()


# Создаем сервер с указанным портом и обработчиком запросов
with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print(f"Serving at port {PORT}")
    # Запускаем сервер
    httpd.serve_forever()
