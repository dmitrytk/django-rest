import datetime

from api.models import Field, Well, Inclinometry, Mer, Rate, Zone, FieldCoordinate, WellPump, WellCase, WellPerforation


def populate_db() -> object:
    """Populate test database with initial data and return field and well names."""

    field_name = 'Верхнесалымское'
    well_name = '99Р'

    field = Field.objects.create(name=field_name)
    well = Well.objects.create(name=well_name, field=field)

    Inclinometry.objects.create(well=well, md=10.0, inc=25.0, azi=152.0)
    Inclinometry.objects.create(well=well, md=20.0, inc=25.0, azi=152.0)

    Mer.objects.create(well=well, date=datetime.date(2021, 1, 1), rate=320.0)
    Mer.objects.create(well=well, date=datetime.date(2021, 2, 1), rate=450.0)

    Rate.objects.create(well=well, date=datetime.date(2021, 1, 1), rate=450.0)
    Rate.objects.create(well=well, date=datetime.date(2021, 1, 2), rate=286.0)

    Zone.objects.create(well=well, name='PK1')
    Zone.objects.create(well=well, name='BV0')

    FieldCoordinate.objects.create(field=field, lat=60.01, lng=71.25)
    FieldCoordinate.objects.create(field=field, lat=60.55, lng=71.88)

    WellPump.objects.create(well=well, name='11000EZ', rate=11000.0)

    WellCase.objects.create(well=well, name='кондуктор', diameter='324.0')
    WellCase.objects.create(well=well, name='эксплуатационная колонна', diameter='168.0')

    WellPerforation.objects.create(well=well, perforator_type='ЗПКМ', top_md='1560.0', bot_md='1570.0')
    WellPerforation.objects.create(well=well, perforator_type='ЗПКМ', top_md='1580.0', bot_md='1590.0')

    return field.name, field.id, well.name, well.id
