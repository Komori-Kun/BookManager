import csv
from django.core.management.base import BaseCommand
from library.models import Author

class Command(BaseCommand):
    help = 'Import authors from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str, help='The path to the CSV file.')

    def handle(self, *args, **kwargs):
        csv_file = kwargs['csv_file']
        with open(csv_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                Author.objects.create(name=row[0])
        self.stdout.write(self.style.SUCCESS('Successfully imported authors'))
