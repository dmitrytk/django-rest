import pytest

from api.models import Inclinometry, Field, Well
from tests.api.factories import IncFactory, FieldFactory, WellFactory


@pytest.fixture
def populate_db(scope='session'):
    field = Field.objects.create(name='Carichan')
    well = Well.objects.create(field=field, name='99R')
    return well


@pytest.fixture
def field() -> Field:
    return FieldFactory()


@pytest.fixture
def well() -> Well:
    return WellFactory()


@pytest.fixture
def inc() -> Inclinometry:
    return IncFactory()
