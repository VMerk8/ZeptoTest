from rest_framework import serializers

from .models import Author, Book, Library


class LibrarySerializer(serializers.ModelSerializer):

    class Meta:
        model = Library
        fields = ['id', 'library_name', 'address', 'capacity']


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ['id', 'name', 'publication_year', 'library_id']


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Author
        fields = ['id', 'author_name', 'date_of_birth']
