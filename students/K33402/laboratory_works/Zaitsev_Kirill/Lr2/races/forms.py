from .models import Racer, Comment, Team
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


# Define a form for user registration with additional email field
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


# Define a form for race entry with a choice field for selecting a racer
class RaceEntryForm(forms.Form):
    racer = forms.ModelChoiceField(queryset=Racer.objects.all(), empty_label=None)


# Define a form for racer registration with fields for description and experience
class RacerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Racer
        fields = ['description', 'experience']


# Define a form for user comments with fields for comment type, rating, and text
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["comment_type", "rating", "text"]
        widgets = {
            'comment_type': forms.Select(attrs={'class': 'form-control'}),
            'rating': forms.NumberInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }


# Define a form for updating user profiles with fields for team, description, and experience
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

    # Initialize form fields with current user data
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

    # Validate password change form data
    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password = cleaned_data.get('new_password')
        new_password_confirm = cleaned_data.get('new_password_confirm')

        if new_password or new_password_confirm:
            if not current_password:
                raise forms.ValidationError("To change the password, please provide the current password.")

            user = self.instance
            if not user.check_password(current_password):
                raise forms.ValidationError("The current password you provided is incorrect.")

            if new_password != new_password_confirm:
                raise forms.ValidationError("The new passwords do not match.")
        return cleaned_data


# Define a custom password change form with styled password input fields
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
