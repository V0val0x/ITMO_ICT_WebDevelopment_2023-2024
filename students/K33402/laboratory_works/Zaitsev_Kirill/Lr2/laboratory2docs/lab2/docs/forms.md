```python
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User

from .models import Racer, Comment, Team


# Определяем форму для регистрации пользователей с дополнительным полем электронной почты
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }


# Определяем форму для регистрации гонщиков с полями для описания и опыта
class RacerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ['description', 'experience']


# Определяем форму для комментариев пользователей с полями для типа комментария, рейтинга и текста
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_type", "rating", "text"]
        widgets = {
            'comment_type': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


# Определяем форму для участия гонщика в соревновании
class RaceEntryForm(forms.Form):
    racer = forms.ModelChoiceField(queryset=Racer.objects.all(), empty_label=None)


# Определяем форму для обновления профиля пользователя с полями для команды, описания и опыта
class ProfileUpdateForm(UserChangeForm):
    team_choices = [(r.id, r.name) for r in Team.objects.all()]
    team = forms.ChoiceField(choices=[("", "Выберите команду")] + team_choices,
                             widget=forms.Select(attrs={'class': 'form-control'}), required=False, label="Команда")
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}), required=False,
                                  label="Описание")
    experience = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'min': 0}), required=False,
                                    label="Опыт")
    current_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}), required=False,
        label="Текущий пароль")
    new_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}), required=False,
        label="Новый пароль")
    new_password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}), required=False,
        label="Подтвердите новый пароль")

    class Meta:
        model = User
        fields = ('username', 'email', 'team', 'description', 'experience')

    # Инициализируем поля формы текущими данными пользователя
    def __init__(self, *args, **kwargs):
        super(ProfileUpdateForm, self).__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            try:
                racer = instance.racer
                if racer:
                    if racer.team:
                        self.fields['team'].initial = racer.team.id
                    self.fields['description'].initial = racer.description
                    self.fields['experience'].initial = racer.experience
            except Racer.DoesNotExist:
                pass

    # Проверяем корректность данных формы для изменения пароля
    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        new_password_confirm = cleaned_data.get('new_password_confirm')

        if new_password or new_password_confirm:
            if not current_password:
                raise forms.ValidationError("Чтобы изменить пароль, укажите текущий пароль.")

            user = self.instance
            if not user.check_password(current_password):
                raise forms.ValidationError("Указанный текущий пароль неверен.")

            if new_password != new_password_confirm:
                raise forms.ValidationError("Новые пароли не совпадают.")
        return cleaned_data


# Определяем кастомную форму для изменения пароля с форматированными полями ввода пароля
class PasswordChangeCustomForm(PasswordChangeForm):
    old_password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'current-password'}),
        label="Текущий пароль")
    new_password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        label="Новый пароль")
    new_password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'autocomplete': 'new-password'}),
        label="Подтвердите новый пароль")

```