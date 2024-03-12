from django.urls import path
from . import views

urlpatterns = [
    path('owner/<int:owner_id>/', views.car_owner_detail),
    path('all_car_owners/', views.all_car_owners, name='all_car_owners'),
    path('all_cars/', views.all_cars),
    path('car/<int:car_id>/', views.car_detail),
    path('add_car_owner/', views.add_car_owner),
    path('car/create/', views.CarCreateView.as_view(), name='car_create'),
    path('car/update/<int:pk>/', views.CarUpdateView.as_view(), name='car_update'),
    path('car/delete/<int:pk>/', views.CarDeleteView.as_view(), name='car_delete'),
]
