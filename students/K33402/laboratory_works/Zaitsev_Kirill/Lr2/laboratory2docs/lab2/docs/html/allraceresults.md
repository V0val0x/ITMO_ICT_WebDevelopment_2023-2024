```html
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">
    <style>
        body {
            background-color: #f0f0f0;
        }
        .container {
            background-color: #fff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        h1 {
            color: #007BFF;
        }
        .btn {
            margin: 5px;
            width: 200px;
        }
    </style>
    <title>Главная страница</title>
</head>
<body>
<div class="container mt-5">
    <h1 class="mb-4">Добро пожаловать на официальный сайт гонок XXX!</h1>
    <a href="{% url 'login' %}" class="btn btn-primary">Вход</a>
    <a href="{% url 'register_user' %}" class="btn btn-secondary">Регистрация</a>
</div>
</body>
</html>
```