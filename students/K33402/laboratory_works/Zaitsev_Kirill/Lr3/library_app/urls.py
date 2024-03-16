from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

app_name = 'library_app'

router = DefaultRouter()
router.register('reader', viewset=ReaderViewSet)
router.register('category', viewset=CategoryViewSet)
router.register('author', viewset=AuthorViewSet)
router.register('reading-room', viewset=ReadingRoomViewSet)
router.register('book', viewset=BookViewSet)
router.register('book-copy', viewset=BookCopyViewSet)
router.register('book-take', viewset=BookTakeViewSet)

urlpatterns = [
    path('register/', RegistrationView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('change-password/<int:pk>/', ChangePasswordView.as_view(), name='change-password'),

    path('', include(router.urls)),
]
