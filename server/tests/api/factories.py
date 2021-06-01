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


class WellStateFactory(DjangoModelFactory):
    value_full = factory.Sequence(lambda n: f'State_{n}')
    value_short = factory.Sequence(lambda n: f's_{n}')

    class Meta:
        model = 'api.WellState'


class WellWorkTypeFactory(DjangoModelFactory):
    value_full = factory.Sequence(lambda n: f'Work_{n}')
    value_short = factory.Sequence(lambda n: f'w_{n}')

    class Meta:
        model = 'api.WellWorkType'


class MerFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Mer'

    date = factory.Sequence(lambda n: datetime.date(2010, 1, 1) + datetime.timedelta(days=n * 31))
    production = factory.LazyAttribute(lambda x: random.random() * 1000)
    well = factory.SubFactory(WellFactory)
    work_type = factory.SubFactory(WellWorkTypeFactory)
    state = factory.SubFactory(WellStateFactory)


class RateFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Rate'

    date = factory.Sequence(lambda n: datetime.date(2010, 1, 1) + datetime.timedelta(days=n))
    rate = factory.LazyAttribute(lambda x: random.random() * 100)
    well = factory.SubFactory(WellFactory)
    work_type = factory.SubFactory(WellWorkTypeFactory)


class HorizonFactory(DjangoModelFactory):
    class Meta:
        model = 'api.Horizon'

    value_short = factory.Sequence(lambda n: f'z_{n}')
    value_full = factory.Sequence(lambda n: f'Zone_{n}')
    field = factory.SubFactory(FieldFactory)


class WellHorizonFactory(DjangoModelFactory):
    class Meta:
        model = 'api.WellHorizon'

    horizon = factory.SubFactory(HorizonFactory)
    well = factory.SubFactory(WellFactory)
    top_md = factory.LazyAttribute(lambda x: random.random() * 10000)
    bot_md = factory.LazyAttribute(lambda obj: obj.top_md + 10)


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
