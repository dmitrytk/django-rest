from random import random

from django.core.management import BaseCommand

from api.models import Field, HorizonType, WellWorkType, WellState, Well, Inclinometry, Horizon, WellHorizon


class Command(BaseCommand):
    help = 'Populate DB with sample data'

    def handle(self, *args, **options):
        (horizon_type, work_type, state) = self.populate_dict_values()
        field1 = Field.objects.create(name='Верхнесалымское', type='нефятное', location='ХМАО')
        Field.objects.create(name='Царичанское', type='нефятное', location='Оренбургская область')

        horizon1 = Horizon.objects.create(field=field1, value_full='Уватская', value_short='ув',
                                          type=horizon_type)
        Horizon.objects.create(field=field1, value_full='Ханты-Мансийская', value_short='хм', type=horizon_type)
        Horizon.objects.create(field=field1, value_full='Викуловская', value_short='вк', type=horizon_type)

        well1 = Well.objects.create(field=field1, name='1WW')
        Well.objects.create(field=field1, name='3028')

        WellHorizon.objects.create(well=well1, horizon=horizon1, top_md=random() * 1000, bot_md=random() * 2000)

        Inclinometry.objects.bulk_create([
            Inclinometry(well=well1, md=random(), inc=random(), azi=random()) for i in range(100)
        ])

    def populate_dict_values(self):
        h = HorizonType.objects.create(name='свита')
        HorizonType.objects.create(name='пласт')
        HorizonType.objects.create(name='ярус')
        HorizonType.objects.create(name='отдел')
        HorizonType.objects.create(name='пачка')

        w = WellWorkType.objects.create(value_short='вз', value_full='водозаборная')
        WellWorkType.objects.create(value_short='пог', value_full='поглощающая')
        WellWorkType.objects.create(value_short='наг', value_full='нагнетательная')
        WellWorkType.objects.create(value_short='арт', value_full='артезиаснкая')

        s = WellState.objects.create(value_short='раб', value_full='в работе')
        WellState.objects.create(value_short='лик', value_full='в ликвидации')
        WellState.objects.create(value_short='кон', value_full='в консервации')
        WellState.objects.create(value_short='осв', value_full='в освоении')
        WellState.objects.create(value_short='бур', value_full='в бурении')
        WellState.objects.create(value_short='пье', value_full='пьезометрическая')
        return (h, w, s)
