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
        }
        .btn-secondary {
            background-color: #6c757d;
            color: #fff;
        }
        .btn-secondary:hover {
            background-color: #5a6268;
        }
        .btn-primary {
            background-color: #007BFF;
        }
        .btn-primary:hover {
            background-color: #0056b3;
        }
        h1 {
            color: #007BFF;
            text-align: center;
        }
        h2 {
            color: #007BFF;
        }
        .list-group {
            margin-top: 20px;
        }
        .list-group-item {
            margin-top: 10px;
            border-color: #007BFF;
        }
        .form-control {
            width: 100%;
        }
            form {
        max-width: 400px;
        margin: 0 auto;
        }
        .form-group {
            margin-bottom: 15px;
        }
        .form-group label {
            display: block;
        }
        .form-group input {
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        .btn-block {
            width: 100%;
        }
    </style>
</head>
<body>
<div class="container mt-5">
    <a href="{% url 'tablo' %}" class="btn btn-secondary mb-4">К таблице</a>
    <form method="post" class="mb-5">
        {% csrf_token %}
        <div class="form-group">
            {{ form.author.label_tag }}
            {{ form.author }}
        </div>
        <div class="form-group">
            {{ form.comment_type.label_tag }}
            {{ form.comment_type }}
        </div>
        <div class="form-group">
            {{ form.rating.label_tag }}
            {{ form.rating }}
        </div>
        <div class="form-group">
            {{ form.text.label_tag }}
            {{ form.text }}
        </div>
        <button type="submit" class="btn btn-primary">Отправить</button>
    </form>
    <h2 class="mb-3">Список комментариев</h2>
    <ul class="list-group">
        {% for comment in comments %}
        <li class="list-group-item">
            <strong>{{ comment.author.username }}</strong> ({{ comment.created_at|date:"Y-m-d H:i:s" }})
            <br>
            Тип: {{ comment.get_comment_type_display }}
            <br>
            Рейтинг: {{ comment.rating }}
            <br>
            {{ comment.text }}
        </li>
        {% endfor %}
    </ul>
</div>
</body>
</html>
```