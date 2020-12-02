from rest_framework.test import APITestCase

from api.models import Inclinometry, Mer, Rate, Zone, FieldCoordinate


class TestBatchApi(APITestCase):
    fixtures = ['api.json']
    well_name = '99R'
    inclinometry_url = '/api/batch/inclinometry'
    mer_url = '/api/batch/mer'
    rates_url = '/api/batch/rates'
    zones_url = '/api/batch/zones'
    coordinates_url = '/api/batch/coordinates'

    def test_load_inclinometry(self):
        # Load inclinometry
        data = {
            'field_id': 1,
            'data': [
                {'well': self.well_name, 'md': 10, 'inc': None, 'azi': 78.23},
                {'well': self.well_name, 'md': 20},
                {'well': '1P', 'md': 1},  # add new well
            ]
        }
        response = self.client.post(self.inclinometry_url, data, format='json')
        self.assertEqual(Inclinometry.objects.count(), 3)  # old inclinometry will be deleted 0 + 3 = 2

    def test_load_mer(self):
        data = {
            'field_id': 1,
            'data': [
                {'well': self.well_name, 'date': '01.01.2000'},
                {'well': self.well_name, 'date': '01.01.2000'},  # duplicate date will be overwritten
                {'well': '1P', 'date': '01.01.2000'},  # add new well
            ]
        }
        response = self.client.post(self.mer_url, data, format='json')
        self.assertEqual(Mer.objects.all().count(), 4)  # 2 + 1 + 1 = 4

    def test_load_rates(self):
        data = {
            'field_id': 1,
            'data': [
                {'well': self.well_name, 'date': '01.01.2000', 'rate': 256.78, 'status': 'work'},
                {'well': self.well_name, 'date': '01.01.2000'},
                {'well': '1P', 'date': '01.01.2000'},  # add new well
            ]
        }
        response = self.client.post(self.rates_url, data, format='json')
        self.assertEqual(Rate.objects.all().count(), 5)  # 2 + 2 + 1 = 5

    def test_load_zones(self):
        data = {
            'field_id': 1,
            'data': [
                {'well': self.well_name, 'name': 'pk1', 'top_md': 1500.25},
                {'well': self.well_name, 'name': 'pk2', 'top_md': 1550.26},
                {'well': '1P', 'name': 'uvat', 'top_md': 860.25},  # add new well
            ]
        }
        response = self.client.post(self.zones_url, data, format='json')
        self.assertEqual(Zone.objects.all().count(), 5)  # 2 + 2 + 1 = 5

    def test_load_coordinates(self):
        data = {
            'field_id': 1,
            'data': [
                {'lat': 60.23, 'lng': 50.28},
                {'lat': 60.28, 'lng': 50.29},
            ]
        }
        response = self.client.post(self.coordinates_url, data, format='json')
        self.assertEqual(FieldCoordinate.objects.all().count(), 2)
