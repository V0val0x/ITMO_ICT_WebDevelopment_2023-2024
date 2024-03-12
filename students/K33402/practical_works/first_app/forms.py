from django import forms
from django.forms import DateTimeInput

from .models import Car, CarOwner
from django import forms
from django.utils import timezone


class CarOwnerForm(forms.ModelForm):
    birth_date = forms.DateTimeField(
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        initial=timezone.now(),
        input_formats=['%Y-%m-%dT%H:%M:%S']
    )

    class Meta:
        model = CarOwner
        fields = ['first_name', 'last_name', 'birth_date']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['registration_number', 'brand', 'model', 'color']
