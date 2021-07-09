from django.urls import path, include
from .views import LibraryView, BookView, AuthorView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('library', LibraryView, basename='library')
router.register('book', BookView, basename='book')
router.register('author', AuthorView)

urlpatterns = [
    path('api/', include(router.urls))
]
