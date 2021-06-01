from django.core.management import BaseCommand

from api.models import Field, HorizonType, WellWorkType, WellState


class Command(BaseCommand):
    help = 'Clear DB'

    def handle(self, *args, **options):
        Field.objects.filter().delete()
        HorizonType.objects.filter().delete()
        WellWorkType.objects.filter().delete()
        WellState.objects.filter().delete()
