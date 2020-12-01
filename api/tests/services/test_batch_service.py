from django.test import TestCase

from api.models import Inclinometry, Mer
from api.services.batch_service import load_inclinometry, load_mer


class TestBatchService(TestCase):
    fixtures = ['api.json']
    well_name = '99R'

    def test_load_inclinometry(self):
        print(Inclinometry.objects.count())
        data = {
            'field_id': 1,
            'data': [
                {'well': self.well_name, 'md': 10, 'inc': None, 'azi': 78.23},
                {'well': self.well_name, 'md': 20}
            ]
        }
        load_inclinometry(data)
        self.assertEqual(Inclinometry.objects.count(), 2)  # old inclinometry will be deleted 0 + 2 = 2

    def test_load_mer(self):
        data = {
            'field_id': 1,
            'data': [
                {'well': self.well_name, 'date': '01.01.2000'},
                {'well': self.well_name, 'date': '01.01.2000'}  # duplicate date will be overwritten
            ]
        }
        load_mer(data)
        self.assertEqual(Mer.objects.all().count(), 3)  # 2 + 1 = 3
