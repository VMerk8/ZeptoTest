from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .serializers import LibrarySerializer, AuthorSerializer, BookSerializer
from .models import Author, Book, Library


class LibraryView(ModelViewSet):
    serializer_class = LibrarySerializer
    queryset = Library.objects.all()


class BookView(ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    book_set = Book.objects.prefetch_related('authors_names')

    @action(detail=False, methods=['get'], url_name='get_authors')
    def get_authors(self, request):
        result = Book.objects.prefetch_related('authors_names').\
            filter(library_id__in=request.query_params.getlist('library')).values('authors_names')
        return Response(result)

    @action(detail=False, methods=['get'], url_name='get_library_books')
    def get_library_books(self, request):
        result = Book.objects.filter(library_id=request.query_params.get('library_id')).values('name')
        return Response(result)


class AuthorView(ModelViewSet):
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
