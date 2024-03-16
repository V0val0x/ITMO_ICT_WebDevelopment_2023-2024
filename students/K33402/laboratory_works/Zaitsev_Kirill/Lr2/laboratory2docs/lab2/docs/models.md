```python
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Определение модели Team, представляющей гоночные команды
class Team(models.Model):
    # Поле для названия команды с максимальной длиной 100 символов
    name = models.CharField(max_length=100)

    # Отображение названия команды в виде строки
    def __str__(self):
        return self.name

    # Метаданные модели
    class Meta:
        verbose_name = "Команда"  # Единственное число для отображения в административном интерфейсе
        verbose_name_plural = "Команды"  # Множественное число для отображения в административном интерфейсе


# Определение модели Racer, представляющей гонщиков
class Racer(models.Model):
    # Связь каждого гонщика с объектом пользователя User в однозначном соответствии
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    # Разрешение гонщикам быть частью гоночной команды в соответствии один ко многим
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, verbose_name="Команда")

    # Поле для описания гонщика
    description = models.TextField(verbose_name="Описание")

    # Поле для опыта гонщика, допускающее пустые записи
    experience = models.IntegerField(verbose_name="Опыт", null=True, blank=True)

    # Отображение имени пользователя гонщика в виде строки
    def __str__(self):
        return self.user.username

    # Метаданные модели
    class Meta:
        verbose_name = "Гонщик"  # Единственное число для отображения в административном интерфейсе
        verbose_name_plural = "Гонщики"  # Множественное число для отображения в административном интерфейсе


# Определение модели Race, представляющей гоночные события
class Race(models.Model):
    # Поле для названия гонки с максимальной длиной 100 символов
    name = models.CharField(max_length=100)

    # Поле для даты и времени гонки
    date = models.DateTimeField()

    # Разрешение указания победителя гонки (команды) в соответствии один ко многим
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Победитель")

    # Отображение названия гонки в виде строки
    def __str__(self):
        return self.name

    # Метаданные модели
    class Meta:
        verbose_name = "Гонка"  # Единственное число для отображения в административном интерфейсе
        verbose_name_plural = "Гонки"  # Множественное число для отображения в административном интерфейсе


# Определение модели RaceResult, представляющей результаты гонки
class RaceResult(models.Model):
    # Связь каждого результата с определенной гонкой в соответствии один ко многим
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")

    # Связь каждого результата с определенной командой в соответствии один ко многим
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Команда")

    # Поле для времени, затраченного командой на завершение гонки
    time_taken = models.DurationField(verbose_name="Время прохождения")

    # Отображение строкового представления объекта результата
    def __str__(self):
        return f"{self.race.name} - {self.team.name} - {self.time_taken}"

    # Метаданные модели
    class Meta:
        verbose_name = "Результат гонки"  # Единственное число для отображения в административном интерфейсе
        verbose_name_plural = "Результаты гонок"  # Множественное число для отображения в административном интерфейсе


# Определяем модель RaceEntry для представления участия гонщика в гонке
class RaceEntry(models.Model):
    # Связываем каждую запись с конкретным гонщиком в отношении многие-к-одному
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE, verbose_name="Гонщик")

    # Связываем каждую запись с конкретной гонкой в отношении многие-к-одному
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")

    # Метаданные модели
    class Meta:
        verbose_name = "Участие в гонке"  # Название модели в административном интерфейсе (единственное число)
        verbose_name_plural = "Участия в гонках"  # Название модели в административном интерфейсе (множественное число)


# Определяем модель Comment для представления комментариев пользователей к гонкам
class Comment(models.Model):
    # Определяем варианты для типов комментариев
    COMMENT_TYPES = (
        ("cooperation", "Предложения"),  # Предложения
        ("race", "Гонки"),  # Гонки
        ("complaint", "Жалоба"),  # Жалобы
        ("other", "Другое"),  # Другое
    )

    # Связываем каждый комментарий с конкретной гонкой в отношении многие-к-одному
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")

    # Связываем каждый комментарий с конкретным автором (пользователем) в отношении многие-к-одному
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    # Поле для текстового содержимого комментария
    text = models.TextField(verbose_name="Текст комментария")

    # Поле для типа комментария, используя заранее определенные варианты
    comment_type = models.CharField(
        max_length=20,
        choices=COMMENT_TYPES,
        verbose_name="Тип комментария"
    )

    # Поле для рейтинга комментария, с валидацией находится ли он в заданном диапазоне
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг"
    )

    # Поле для даты и времени создания комментария, автоматически устанавливается текущим временем
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # Отображаем строковое представление объекта комментария
    def __str__(self):
        return f"{self.author.username} - {self.comment_type} - {self.race.name}"

    # Метаданные модели
    class Meta:
        verbose_name = "Комментарий"  # Название модели в административном интерфейсе (единственное число)
        verbose_name_plural = "Комментарии"  # Название модели в административном интерфейсе (множественное число)

```