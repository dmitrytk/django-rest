from django.test import TestCase

from api import queries
from api.models import Inclinometry, Mer, Rate
from api.services.inc_service import _delete_old_inc
from api.services.raw_sql_service import batch_load


class TestDatabase(TestCase):
    fixtures = ['api.json']
    field_name = 'UpperSalym'
    well_name = '99R'
    md = 10
    date = '2020-01-01'
    rate = 756.08
    invalid_data = [(1, '99R')]

    def test_load_incl(self):
        valid_data = [
            (1, self.well_name, 10, 15.26, None),
            (1, self.well_name, 20, None, None),
        ]
        batch_load(queries.INCLINOMETRY_LOAD, valid_data)
        self.assertEqual(Inclinometry.objects.all().count(), 2)

    def test_load_mer(self):
        valid_data = [
            (1, self.well_name, '2020-01-01', 'active', 456.26, 4658.10, 37),
            (1, self.well_name, '2020-01-01', 'active', 456.88, 4658.10, 37),
        ]
        batch_load(queries.MER_LOAD, valid_data)
        self.assertEqual(Mer.objects.all().count(), 1)

    def test_load_rate(self):
        valid_data = [
            (1, self.well_name, '2020-01-01', 456.26, 4658.10, 37.56, 798),
            (1, self.well_name, '2020-01-01', 456.88, 4658.10, 37.489, None),
        ]
        batch_load(queries.RATES_LOAD, valid_data)
        self.assertEqual(Rate.objects.all().count(), 2)

    def test_delete_old_inc(self):
        Inclinometry.objects.create(well_id=1, md=10)
        Inclinometry.objects.create(well_id=1, md=20)
        Inclinometry.objects.create(well_id=2, md=20)
        Inclinometry.objects.create(well_id=3, md=10)
        self.assertEqual(Inclinometry.objects.all().count(), 4)
        _delete_old_inc(1, ['99R', '3028'])
        self.assertEqual(Inclinometry.objects.all().count(), 1)
