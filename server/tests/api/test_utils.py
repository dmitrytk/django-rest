import pytest

from api.utils.mappers import map_inc, map_mer, map_rate, map_coordinate, map_case, map_mer_view, map_rates_view
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

    def test_map_mer_view(self):
        data = ('01.01.2020', 'in work', None, None, None)
        expected = {'date': '01.01.2020',
                    'status': 'in work',
                    'rate': None,
                    'production': None,
                    'work_days': None
                    }
        assert map_mer_view(data) == expected

    def test_map_range_view(self):
        data = ('01.01.2020', 'in work', None, None, None, None)
        expected = {'date': '01.01.2020',
                    'status': 'in work',
                    'rate': None,
                    'dynamic_level': None,
                    'static_level': None,
                    'pressure': None
                    }
        assert map_rates_view(data) == expected


class TestValidators:

    def test_batch_validators(self):
        valid_data = {'field_id': 1, 'rows': [1, 2]}
        invalid_data = {'field_id': 1, 'rows': 'red'}
        assert validate_batch_data(valid_data)
        assert validate_batch_data(invalid_data) == False
