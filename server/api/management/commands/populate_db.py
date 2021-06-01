from django.core.management import BaseCommand

from api.models import Field


class Command(BaseCommand):
    help = 'Clear and populate DB with sample data'

    def handle(self, *args, **options):
        Field.objects.filter().delete()
        Field.objects.create(name='Верхнесалымское')
        Field.objects.create(name='Царичанское')
