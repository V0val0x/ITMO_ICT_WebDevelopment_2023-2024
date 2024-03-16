    from django.contrib import admin
    from django.urls import path, include, re_path
    
    urlpatterns = [
        path("admin/", admin.site.urls),
        path('library/', include('library_app.urls')),
        path(r'auth/', include('djoser.urls')),
        re_path(r'auth/', include('djoser.urls.authtoken')),
    ]



    from django.urls import path
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
    router.register('book-taken', viewset=BookTakeViewSet)
    
    urlpatterns = router.urls
