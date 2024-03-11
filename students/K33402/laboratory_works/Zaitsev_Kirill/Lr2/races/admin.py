from django.contrib import admin
from .models import Team, Racer, Race, RaceEntry, Comment, RaceResult


# Register models for administration and customize their display
@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)


@admin.register(Racer)
class RacerAdmin(admin.ModelAdmin):
    list_display = ('user', 'team', 'description', 'experience')
    list_filter = ('team', 'experience')


class RaceResultInline(admin.TabularInline):
    model = RaceResult
    extra = 1


@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'get_winner_time')
    list_filter = ('winner',)
    inlines = [RaceResultInline]

    def get_winner_time(self, obj):
        winner_result = RaceResult.objects.filter(race=obj, team=obj.winner).first()
        return winner_result.time_taken if winner_result else None

    get_winner_time.short_description = 'Time taken by winner'


@admin.register(RaceEntry)
class RaceEntryAdmin(admin.ModelAdmin):
    list_display = ('racer', 'race')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'race', 'comment_type', 'created_at', 'rating')
    list_filter = ('comment_type', 'created_at')
