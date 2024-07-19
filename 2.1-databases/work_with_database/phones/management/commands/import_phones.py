import csv

from django.core.management.base import BaseCommand
from phones.models import Phone
from work_with_database.phones.models import Phone
from django.utils.text import slugify

mkdir -p work_with_database/phones/management/commands/
touch work_with_database/phones/management/__init__.py
touch work_with_database/phones/management/commands/__init__.py



class Command(BaseCommand):
    help = 'Import phones from a CSV file'

    def handle(self, *args, **options):
        with open('phones.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                phone = Phone(
                    id=row['id'],
                    name=row['name'],
                    price=row['price'],
                    image=row['image'],
                    release_date=row['release_date'],
                    lte_exists=row['lte_exists'],
                    slug=slugify(row['name'])
                )
                phone.save()

        self.stdout.write(self.style.SUCCESS('Successfully imported phones'))
