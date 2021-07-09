from http import HTTPStatus

import pytest
from django.urls import reverse

from library.models import *


@pytest.mark.django_db
class TestLibraryView:

    def test_library_view_post(self, client):
        test_data = {
            'library_name': 'First',
            'address': 'Pushkina 1',
            'capacity': 100
        }
        response = client.post(reverse('library-list'), data=test_data, content_type='application/json')
        assert response.status_code == HTTPStatus.CREATED

    def test_library_view_get_list(self, client):
        response = client.get(reverse('library-list'))
        assert response.status_code == HTTPStatus.OK

    def test_library_view_get_detail(self, client):
        Library.objects.create(library_name='Fire', address='asdsad', capacity=123)
        response = client.get(reverse('library-detail', kwargs={'pk': 1}))
        assert response.status_code == HTTPStatus.OK

    def test_library_view_put(self, client):
        Library.objects.create(library_name='Fire', address='asdsad', capacity=123)
        test_data = {
            'library_name': 'First',
            'address': 'Pushkina 1',
            'capacity': 100
        }
        response = client.put(reverse('library-detail', kwargs={'pk': 1}), data=test_data,
                              content_type='application/json')
        assert response.status_code == HTTPStatus.OK

    def test_library_view_patch(self, client):
        Library.objects.create(library_name='Fire', address='asdsad', capacity=123)
        test_data = {
            'library_name': 'First',
            'address': 'Pushkina 1'
        }
        response = client.patch(reverse('library-detail', kwargs={'pk': 1}), data=test_data,
                                content_type='application/json')
        assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
class TestAuthorView:

    def test_author_view_get_list(self, client):
        response = client.get(reverse('author-list'))
        assert response.status_code == HTTPStatus.OK

    def test_author_view_get_detail(self, client):
        Author.objects.create(author_name='Pantheon', date_of_birth='1997-01-01')
        response = client.get(reverse('author-detail', kwargs={'pk': 1}))
        assert response.status_code == HTTPStatus.OK

    def test_author_view_put(self, client):
        Author.objects.create(author_name='Pantheon', date_of_birth='1997-01-01')
        test_data = {
            'author_name': 'Darius',
            'date_of_birth': '2001-09-03'
        }
        response = client.put(reverse('author-detail', kwargs={'pk': 1}), data=test_data,
                              content_type='application/json')
        assert response.status_code == HTTPStatus.OK

    def test_author_view_post(self, client):
        test_data = {
            'author_name': 'Darius',
            'date_of_birth': '2001-09-03'
        }
        response = client.post(reverse('author-list'), data=test_data, content_type='application/json')
        assert response.status_code == HTTPStatus.CREATED

    def test_author_view_patch(self, client):
        Author.objects.create(author_name='Pantheon', date_of_birth='1997-01-01')
        test_data = {
            'date_of_birth': '1994-06-28'
        }
        response = client.patch(reverse('author-detail', kwargs={'pk': 1}), data=test_data,
                                content_type='application/json')
        assert response.status_code == HTTPStatus.OK


@pytest.mark.django_db
class TestBookView:

    def test_book_view_get_list(self, client):
        response = client.get(reverse('book-list'))
        assert response.status_code == HTTPStatus.OK

    def test_book_view_get_detail(self, client):
        Library.objects.create(library_name='Sand', address='Pionerskaya 1', capacity=200)
        Book.objects.create(name='Скрытый в земле', publication_year='1990', library_id=Library.objects.get(id=1))
        response = client.get(reverse('book-detail', kwargs={'pk': 1}))
        assert response.status_code == HTTPStatus.OK

    def test_book_view_put(self, client):
        Library.objects.create(library_name='Sand', address='Pionerskaya 1', capacity=200)
        Book.objects.create(name='Скрытый в земле', publication_year='1990', library_id=Library.objects.get(id=1))
        test_data = {
            'name': 'Darius',
            'publication_year': 2001,
            'library_id': 1
        }
        response = client.put(reverse('book-detail', kwargs={'pk': 1}), data=test_data,
                              content_type='application/json')
        assert response.status_code == HTTPStatus.OK

    def test_book_view_post(self, client):
        Library.objects.create(library_name='Sand', address='Pionerskaya 1', capacity=200)
        test_data = {
            'name': 'Darius',
            'publication_year': 2001,
            'library_id': 1
        }
        response = client.post(reverse('book-list'), data=test_data, content_type='application/json')
        assert response.status_code == HTTPStatus.CREATED

    def test_book_view_patch(self, client):
        Library.objects.create(library_name='Sand', address='Pionerskaya 1', capacity=200)
        Book.objects.create(name='Скрытый в земле', publication_year='1990', library_id=Library.objects.get(id=1))
        test_data = {
            'name': 'Katarina'
        }
        response = client.patch(reverse('book-detail', kwargs={'pk': 1}), data=test_data,
                                content_type='application/json')
        assert response.status_code == HTTPStatus.OK

    def test_book_view_get_library_books(self, client):
        Library.objects.create(library_name='Sand', address='Pionerskaya 1', capacity=200)
        Book.objects.create(name='Скрытый в земле', publication_year='1990', library_id=Library.objects.get(id=1))
        test_data = {
            'library_id': 1
        }
        response = client.get(reverse('book-get_library_books'), data=test_data, content_type='application/json')
        print(response.__dict__)
        assert response.status_code == HTTPStatus.OK

    def test_book_view_get_authors(self, client):
        Author.objects.create(author_name='Jax', date_of_birth='1997-06-06')
        Library.objects.create(library_name='Sand', address='Pionerskaya 1', capacity=200)
        Book.objects.create(name='Скрытый в земле', publication_year='1990', library_id=Library.objects.get(id=1))
        Book.objects.get(id=1).authors_names.add(Author.objects.get(id=1))
        test_data = {
            'library': 1
        }
        response = client.get(reverse('book-get_authors'), data=test_data, content_type='application/json')
        print(response.__dict__)
        assert response.status_code == HTTPStatus.OK
