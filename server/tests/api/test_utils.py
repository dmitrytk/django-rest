import pytest
from django.forms import model_to_dict

from api.models import Well
from api.utils.mappers import map_inc, map_mer, map_rate, map_coordinate, map_case
from api.utils.validators import validate_batch_data

pytestmark = pytest.mark.unit


class TestMappers:
    def test_map_inc(self):
        data = {'well': '99R', 'md': 10, 'azi': 45.36}
        assert map_inc(data) == ['99R', 10, None, 45.36]

    def test_map_mer(self):
        data = {'well': '99R', 'date': '2020-01-01', 'work_days': 1}
        assert map_mer(data) == ['99R', '2020-01-01', None, None, None, 1]

    def test_map_rate(self):
        data = {'well': '99R', 'date': '2020-01-01', 'dynamic_level': 45.35}
        assert map_rate(data) == ['99R', '2020-01-01', None, None, 45.35, None, None]

    def test_map_coordinate(self):
        data = {'lat': 68.78, 'lng': 74.45}
        assert map_coordinate(data) == [68.78, 74.45, None, None]

    def test_map_case(self):
        data = {'well': '99R', 'name': 'Case_0', 'diameter': 325}
        assert map_case(data) == ['99R', 'Case_0', 325, None, None, None, None, None]
        field = Well(name='Field_0')
        dc = model_to_dict(field)
        print(dc)
        assert False


class TestValidators:

    def test_batch_validators(self):
        valid_data = {'field_id': 1, 'rows': [1, 2]}
        invalid_data = {'field_id': 1, 'rows': 'red'}
        assert validate_batch_data(valid_data)
        assert validate_batch_data(invalid_data) == False
