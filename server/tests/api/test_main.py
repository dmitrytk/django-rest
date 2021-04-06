import pytest as pytest

from api.models import Field, Well
from tests.api.factories import WellFactory

pytestmark = [
    pytest.mark.django_db,
    # pytest.mark.unit,
]


class TestField:

    def test_field_creation(self, field):
        well = WellFactory.create_batch(3, field=field)[0]
        assert Well.objects.count() == 3
        assert Field.objects.count() == 1
        assert field.name == 'Field_0'
        assert well.name == 'Well_0'
