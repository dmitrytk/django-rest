from django.test import TestCase

from api import queries
from api.services.raw_sql_service import get_raw_view
from api.utils import mappers


class TestBatchService(TestCase):
    fixtures = ['api.json']

    def test_mer_view(self):
        data = get_raw_view(queries.MER_RANGE, [1], mappers.map_mer_view)
        self.assertEqual(len(data), 2)

    def test_rates_view(self):
        data = get_raw_view(queries.RATES_RANGE, [1], mappers.map_rates_view)
        self.assertEqual(len(data), 2)
