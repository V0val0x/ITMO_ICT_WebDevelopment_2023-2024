from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


# Define a Team model representing racing teams
class Team(models.Model):
    # Field for the team name with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    # Display the team name as the string representation of the object
    def __str__(self):
        return self.name

    # Define metadata for the model
    class Meta:
        verbose_name = "Команда"  # Singular name for the model in admin interface
        verbose_name_plural = "Команды"  # Plural name for the model in admin interface


# Define a Racer model representing individual racers
class Racer(models.Model):
    # Associate each racer with a User object in a one-to-one relationship
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Пользователь")

    # Allow racers to be part of a racing team in a many-to-one relationship
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, verbose_name="Команда")

    # Field for a description of the racer
    description = models.TextField(verbose_name="Описание")

    # Field for the racer's experience, allowing for blank entries
    experience = models.IntegerField(verbose_name="Опыт", null=True, blank=True)

    # Display the racer's username as the string representation of the object
    def __str__(self):
        return self.user.username

    # Define metadata for the model
    class Meta:
        verbose_name = "Гонщик"  # Singular name for the model in admin interface
        verbose_name_plural = "Гонщики"  # Plural name for the model in admin interface


# Define a Race model representing racing events
class Race(models.Model):
    # Field for the name of the race with a maximum length of 100 characters
    name = models.CharField(max_length=100)

    # Field for the date and time of the race
    date = models.DateTimeField()

    # Allow specifying the winner of the race (team) in a many-to-one relationship
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, blank=True, null=True, verbose_name="Победитель")

    # Display the race name as the string representation of the object
    def __str__(self):
        return self.name

    # Define metadata for the model
    class Meta:
        verbose_name = "Гонка"  # Singular name for the model in admin interface
        verbose_name_plural = "Гонки"  # Plural name for the model in admin interface


# Define a RaceResult model representing the results of a race
class RaceResult(models.Model):
    # Associate each result with a specific race in a many-to-one relationship
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")

    # Associate each result with a specific team in a many-to-one relationship
    team = models.ForeignKey(Team, on_delete=models.CASCADE, verbose_name="Команда")

    # Field for the time taken by the team to complete the race
    time_taken = models.DurationField(verbose_name="Время прохождения")

    # Display a string representation of the result object
    def __str__(self):
        return f"{self.race.name} - {self.team.name} - {self.time_taken}"

    # Define metadata for the model
    class Meta:
        verbose_name = "Результат гонки"  # Singular name for the model in admin interface
        verbose_name_plural = "Результаты гонок"  # Plural name for the model in admin interface


# Define a RaceEntry model representing a racer's participation in a race
class RaceEntry(models.Model):
    # Associate each entry with a specific racer in a many-to-one relationship
    racer = models.ForeignKey(Racer, on_delete=models.CASCADE, verbose_name="Гонщик")

    # Associate each entry with a specific race in a many-to-one relationship
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")

    # Define metadata for the model
    class Meta:
        verbose_name = "Участие в гонке"  # Singular name for the model in admin interface
        verbose_name_plural = "Участия в гонках"  # Plural name for the model in admin interface


# Define a Comment model representing user comments on races
class Comment(models.Model):
    # Define choices for the type of comment
    COMMENT_TYPES = (
        ("cooperation", "Предложения"),  # Suggestions
        ("race", "Гонки"),  # Races
        ("complaint", "Жалоба"),  # Complaints
        ("other", "Другое"),  # Other
    )

    # Associate each comment with a specific race in a many-to-one relationship
    race = models.ForeignKey(Race, on_delete=models.CASCADE, verbose_name="Гонка")

    # Associate each comment with a specific author (User) in a many-to-one relationship
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор")

    # Field for the text content of the comment
    text = models.TextField(verbose_name="Текст комментария")

    # Field for the type of comment, using predefined choices
    comment_type = models.CharField(
        max_length=20,
        choices=COMMENT_TYPES,
        verbose_name="Тип комментария"
    )

    # Field for the rating of the comment, validating that it falls within a specified range
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        verbose_name="Рейтинг"
    )

    # Field for the date and time of comment creation, automatically set to the current timestamp
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    # Display a string representation of the comment object
    def __str__(self):
        return f"{self.author.username} - {self.comment_type} - {self.race.name}"

    # Define metadata for the model
    class Meta:
        verbose_name = "Комментарий"  # Singular name for the model in admin interface
        verbose_name_plural = "Комментарии"  # Plural name for the model in admin interface
