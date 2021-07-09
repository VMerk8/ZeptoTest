from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AuthorView, BookView, LibraryView

router = DefaultRouter()
router.register('library', LibraryView, basename='library')
router.register('book', BookView, basename='book')
router.register('author', AuthorView)

urlpatterns = [
    path('api/', include(router.urls))
]
