```python
from django.contrib import admin

from .models import Team, Racer, Race, RaceEntry, Comment, RaceResult


# Регистрируем модель Team в административном интерфейсе Django и настраиваем отображение списка команд
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


# Регистрируем модель Racer в административном интерфейсе Django и настраиваем отображение списка гонщиков
@admin.register(Racer)
class RacerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'description', 'experience')
    list_filter = ('team', 'experience')


# Создаем встроенную форму для отображения результатов гонок в административном интерфейсе
class RaceResultInline(admin.TabularInline):
    model = RaceResult
    extra = 1


# Регистрируем модель Race в административном интерфейсе Django и настраиваем отображение списка гонок
@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'get_winner_time')
    list_filter = ('winner',)
    inlines = [RaceResultInline]

    # Определяем метод для отображения времени, затраченного победителем гонки
    def get_winner_time(self, obj):
        winner_result = RaceResult.objects.filter(race=obj, team=obj.winner).first()
        return winner_result.time_taken if winner_result else None

    get_winner_time.short_description = 'Time taken by winner'


# Регистрируем модель RaceEntry в административном интерфейсе Django и настраиваем отображение списка участников гонок
@admin.register(RaceEntry)
class RaceEntryAdmin(admin.ModelAdmin):
    list_display = ('racer', 'race')


# Регистрируем модель Comment в административном интерфейсе Django и настраиваем отображение списка комментариев
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'race', 'comment_type', 'created_at', 'rating')
    list_filter = ('comment_type', 'created_at')

```