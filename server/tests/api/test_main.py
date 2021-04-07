import pytest as pytest

from api.models import Inclinometry

pytestmark = [
    pytest.mark.django_db,
    # pytest.mark.unit,
]


class TestField:

    def test_field_creation(self, inc):
        assert Inclinometry.objects.count() == 10
