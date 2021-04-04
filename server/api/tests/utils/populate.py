from api.models import Field, Well


def populate_db():
    field = Field.objects.create(name='Carichan')
    Well.objects.create(name='99R', field=field)
