from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path

from .views import (
    race_detail,
    racer_registration,
    racer_unregistration,
)

from .views import *

urlpatterns = [
    path('races/<int:race_id>/', race_detail, name='race_detail'),
    path('races/<int:race_id>/register/', racer_registration, name='racer_registration'),
    path('races/<int:race_id>/unregister/', racer_unregistration, name='racer_unregistration'),
    path("admin/", admin.site.urls),
    path("", base, name="base"),
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path('logout/', user_logout, name='logout'),
    path("register/", user_register, name="register_user"),
    path("profile/", profile, name="profile"),
    path("races/", tablo, name="tablo"),
    path("races/<int:race_id>/comments/", comments, name="comments"),
    path('all_race_results/', all_race_results, name='all_race_results'),
]
