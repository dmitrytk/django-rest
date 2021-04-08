import datetime
import random

import factory
from factory.django import DjangoModelFactory


class FieldFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Field'  # Equivalent to ``model = api.models.Field``

    name = factory.Sequence(lambda n: f'Field_{n}')


class WellFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Well'

    name = factory.Sequence(lambda n: f'Well_{n}')
    field = factory.SubFactory(FieldFactory)


class IncFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Inclinometry'

    md = factory.LazyAttribute(lambda x: random.random() * 100)
    well = factory.SubFactory(WellFactory)


class MerFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Mer'

    date = factory.Sequence(lambda n: datetime.date(2010, 1, 1) + datetime.timedelta(days=n * 31))
    rate = factory.LazyAttribute(lambda x: random.random() * 1000)
    well = factory.SubFactory(WellFactory)


class RateFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Rate'

    date = factory.Sequence(lambda n: datetime.date(2010, 1, 1) + datetime.timedelta(days=n))
    rate = factory.LazyAttribute(lambda x: random.random() * 100)
    well = factory.SubFactory(WellFactory)


class ZoneFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Zone'

    name = factory.Sequence(lambda n: f'Zone_{n}')
    top_md = factory.LazyAttribute(lambda x: random.random() * 10000)
    bot_md = factory.LazyAttribute(lambda obj: obj.top_md + 10)
    well = factory.SubFactory(WellFactory)


class CoordinateFactory(DjangoModelFactory):
    class Meta:
        model = 'api.FieldCoordinate'

    lat = factory.LazyAttribute(lambda x: random.random() * 100)
    lng = factory.LazyAttribute(lambda x: random.random() * 100)
    field = factory.SubFactory(FieldFactory)


class CaseFactory(DjangoModelFactory):
    class Meta:
        model = 'api.WellCase'

    name = factory.Sequence(lambda n: f'Case_{n}')
    diameter = factory.LazyAttribute(lambda x: random.random() * 100)
    well = factory.SubFactory(WellFactory)


class PerforationFactory(DjangoModelFactory):
    class Meta:
        model = 'api.WellPerforation'

    top_md = factory.LazyAttribute(lambda x: random.random() * 10000)
    bot_md = factory.LazyAttribute(lambda obj: obj.top_md + 10)
    well = factory.SubFactory(WellFactory)


class PumpFactory(DjangoModelFactory):
    class Meta:
        model = 'api.WellPump'

    name = factory.Sequence(lambda n: f'Pump_{n}')
    well = factory.SubFactory(WellFactory)
