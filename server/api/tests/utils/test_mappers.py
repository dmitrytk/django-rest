from django.test import SimpleTestCase

from api.models import Field
from api.utils.mappers import map_inc, map_mer, map_rate


class TestMappers(SimpleTestCase):

    def test_map_inc(self):
        data = {'well': '99R', 'md': 10, 'azi': 45.36}
        self.assertListEqual(map_inc(data), ['99R', 10, None, 45.36])

    def test_map_mer(self):
        data = {'well': '99R', 'date': '2020-01-01', 'work_days': 1}
        self.assertListEqual(map_mer(data), ['99R', '2020-01-01', None, None, None, 1])

    def test_map_rate(self):
        data = {'well': '99R', 'date': '2020-01-01', 'dynamic_level': 45.35}
        print(Field._meta.fields)
        self.assertListEqual(map_rate(data), ['99R', '2020-01-01', None, None, 45.35, None, None])
