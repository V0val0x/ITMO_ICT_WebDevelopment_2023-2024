from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Car, CarOwner, Ownership, CustomUser


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'registration_number', 'color')


@admin.register(CarOwner)
class CarOwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'birth_date', 'full_name')


admin.site.register(Ownership)  # редактировать модель Ownership в админ-панели


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'passport_number', 'home_address', 'nationality')
