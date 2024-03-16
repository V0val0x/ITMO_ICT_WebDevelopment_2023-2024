```python
from django.contrib import messages
from django.contrib.auth import login as auth_login
from django.contrib.auth import update_session_auth_hash, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Min
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse


from .forms import *
from .models import Race, RaceResult, RaceEntry

"""Функция user_register отвечает за обработку запросов на регистрацию новых пользователей.
   Если запрос выполнен методом POST, то создается экземпляр формы UserCreationForm, заполненный данными из запроса.
   При успешной валидации формы пользователь добавляется в базу данных,
   а затем происходит его автоматический вход в систему с помощью функции auth_login.
   В случае, если запрос выполнен методом GET, отображается пустая форма регистрации."""
def user_register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('tablo')  # Перенаправляем пользователя на главную страницу после успешной регистрации
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


def base(request):
    return render(request, "tablo.html")


"""Функция формирует список всех гоночных событий и связанных с ними результатов,
   который затем передается в шаблон для отображения."""
@login_required
def tablo(request):
    races = Race.objects.all()
    race_results = []

    for race in races:
        winner_result = race.raceresult_set.filter(team=race.winner).aggregate(min_time=Min('time_taken'))
        min_time = winner_result.get('min_time')
        race_results.append({
            'race': race,
            'min_time': min_time,
        })

    return render(request, "tablo.html", {"race_results": race_results})


"""Функция comments отображает комментарии к конкретному гоночному событию.
   При выполнении запроса методом POST создается новый комментарий и сохраняется в базе данных.
   В случае запроса методом GET отображается форма для добавления нового комментария."""
@login_required
def comments(request, race_id):
    race = get_object_or_404(Race, id=race_id)
    comments = Comment.objects.filter(race=race)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.race = race
            new_comment.author = request.user
            new_comment.save()
    else:
        form = CommentForm()

    return render(
        request,
        "comments.html",
        {"race": race, "comments": comments, "form": form},
    )


"""Функция race_detail отображает детали конкретного гоночного события,
 включая результаты и список зарегистрированных пользователей на гонку.
  Пользователи могут зарегистрироваться или снять свою регистрацию на гонку,
   отправив соответствующий POST-запрос."""
@login_required
def race_detail(request, race_id):
    race = get_object_or_404(Race, pk=race_id)
    results = race.raceresult_set.all()

    # Получить список зарегистрированных пользователей на эту гонку
    registered_users = race.raceentry_set.values_list('racer__user__username', flat=True)

    # Обработка запроса для регистрации/снятия регистрации
    if request.method == 'POST':
        form = RaceEntryForm(request.POST)
        if form.is_valid():
            racer = form.cleaned_data['racer']
            if racer.user.username in registered_users:
                # Если пользователь уже зарегистрирован, снимаем регистрацию
                RaceEntry.objects.filter(racer=racer, race=race).delete()
            else:
                # Регистрируем пользователя на гонку
                RaceEntry.objects.create(racer=racer, race=race)
            return redirect('race_detail', race_id=race_id)
    else:
        form = RaceEntryForm()

    context = {
        'race': race,
        'results': results,
        'registered_users': registered_users,
        'form': form,
    }
    return render(request, 'race_detail.html', context)


# Функция racer_registration реализует регистрацию пользователя на гонку при отправке запроса методом POST.
@login_required
def racer_registration(request, race_id):
    if request.method == 'POST':
        race = get_object_or_404(Race, pk=race_id)
        user = request.user
        racer = Racer.objects.get(user=user)
        race_entry = RaceEntry(race=race, racer=racer)
        race_entry.save()
        return redirect('race_detail', race_id=race_id)
    else:
        return redirect('race_detail', race_id=race_id)


# Функция racer_unregistration реализует отмену регистрации пользователя на гонку при отправке запроса методом POST.
@login_required
def racer_unregistration(request, race_id):
    if request.method == 'POST':
        race = get_object_or_404(Race, pk=race_id)
        user = request.user
        racer = Racer.objects.get(user=user)
        RaceEntry.objects.filter(race=race, racer=racer).delete()
        return redirect('race_detail', race_id=race_id)
    else:
        return redirect('race_detail', race_id=race_id)


# Функция handle_form_errors отвечает за обработку ошибок валидации формы и вывод соответствующих сообщений об ошибках.
def handle_form_errors(request, form):
    for field, errors in form.errors.items():
        for error in errors:
            messages.error(request, f"{field}: {error}")


# Функция user_logout реализует выход пользователя из системы.
def user_logout(request):
    logout(request)
    return redirect(reverse('base'))


"""Функция profile позволяет пользователям просматривать и редактировать свой профиль.
   Пользователь может изменить свой пароль или обновить информацию о себе, включая команду,
   описание и опыт участия в гонках."""
@login_required
def profile(request):
    user = request.user  # Get the current user
    form = ProfileUpdateForm(instance=user)
    password_form = PasswordChangeCustomForm(user)

    if request.method == 'POST':
        if 'password_change' in request.POST:
            password_form = PasswordChangeCustomForm(user, request.POST)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Пароль успешно изменен.')
                return redirect('profile')
            else:
                handle_form_errors(request, password_form)
                if not user.has_usable_password():
                    messages.error(request, 'Пароль не может быть изменен.')
        else:
            form = ProfileUpdateForm(request.POST, instance=user)
            if form.is_valid():
                user = form.save()
                try:
                    racer = user.racer
                except Racer.DoesNotExist:
                    racer = Racer(user=user)

                team_id = form.cleaned_data.get('team')
                if team_id:
                    team = Team.objects.get(pk=team_id)
                    racer.team = team
                else:
                    racer.team = None  # If no team is selected

                if 'description' in form.cleaned_data:
                    racer.description = form.cleaned_data['description']
                if 'experience' in form.cleaned_data:
                    racer.experience = form.cleaned_data['experience']
                racer.save()
                messages.success(request, 'Информация о профиле успешно обновлена.')
                return redirect('profile')

    return render(request, 'profile.html', {'form': form, 'password_form': password_form})


# Функция all_race_results выводит краткий обзор всех гонок
def all_race_results(request):
    all_results = RaceResult.objects.all()

    # Сортировка результатов по гонкам и времени прохождения
    sorted_results = sorted(all_results, key=lambda x: (x.race.id, x.time_taken))

    return render(request, "all_race_results.html", {"all_results": sorted_results})

```