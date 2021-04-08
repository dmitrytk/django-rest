import pytest

from api.models import Field


@pytest.fixture
def create_field(scope='class'):
    Field.objects.create(name='Carichan')


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient
    return APIClient()
