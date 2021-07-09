import secrets
import string
from datetime import timedelta, date

from django.core.management.base import BaseCommand
import random
from library.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        for i in range(1000):

            Library.objects.create(
                library_name=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(5)),
                address=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(15)),
                capacity=random.randint(1, 9223372036854775807)
            )

            start_date = date(1812, 1, 1)
            end_date = date(2005, 12, 31)
            time_between_dates = end_date - start_date
            days_between_dates = time_between_dates.days
            random_number_of_days = random.randrange(days_between_dates)
            random_date = start_date + timedelta(days=random_number_of_days)

            Author.objects.create(
                author_name=''.join(secrets.choice(string.ascii_uppercase + string.digits) for i in range(7)),
                date_of_birth=random_date
            )

            first_author_id = Author.objects.values('id').first()['id']
            last_author_id = Author.objects.values('id').last()['id']
            first_library_id = Library.objects.values('id').first()['id']
            last_library_id = Library.objects.values('id').last()['id']

            Book.objects.create(
                                name=''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(15)),
                                publication_year=random.randint(1890, 2021),
                                library_id=Library.objects.get(id=random.randint(first_library_id, last_library_id))).\
                authors_names.add(Author.objects.get(id=random.randint(first_author_id, last_author_id)))
