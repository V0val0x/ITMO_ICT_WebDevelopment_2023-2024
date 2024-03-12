from django.urls import path
from .views import *

app_name = "warriors_app"

warrior_list = WarriorViewSet.as_view({'get': 'list'})

urlpatterns = [
    path('warriors/', warrior_list),
    path('warriors/full-info/', WarriorViewSet.as_view({'get': 'get_full_info'})),
    path('warriors/<int:pk>/',
         WarriorViewSet.as_view({'get': 'get_warrior_info', 'delete': 'delete_warrior', 'put': 'edit_warrior'})),
    path('profession/create/', ProfessionCreateView.as_view()),
    path('skill/create/', SkillCreateView.as_view()),
    path('skill/', SkillListView.as_view()),
]
