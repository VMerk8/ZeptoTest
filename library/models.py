from django.db import models


class Library(models.Model):
    library_name = models.CharField(max_length=100, verbose_name="Название библиотеки")
    address = models.CharField(max_length=250, verbose_name="Адрес")
    capacity = models.PositiveIntegerField(verbose_name="Вместимость")

    def __str__(self):
        return self.library_name

    class Meta:
        verbose_name = 'Библиотека'
        verbose_name_plural = 'Библиотеки'


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(verbose_name="Дата рождения")

    def __str__(self):
        return self.author_name

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = 'Авторы'


class Book(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название книги")
    publication_year = models.PositiveSmallIntegerField(verbose_name="Год публикации")
    authors_names = models.ManyToManyField(Author, verbose_name="Имена авторов")
    library_id = models.ForeignKey(
        Library, related_name="books", verbose_name="Библиотека", null=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
