from rest_framework import status
from rest_framework.test import APITestCase


class TestFieldApi(APITestCase):
    fixtures = ['api.json']
    new_well_name = '1P'
    field_list_url = '/api/fields/'
    field_detail_url = '/api/fields/1/'
    field_wells_url = '/api/fields/1/wells/'
    field_inc_url = '/api/fields/1/inclinometry/'
    field_mer_url = '/api/fields/1/mer/'
    field_rates_url = '/api/fields/1/rates/'
    field_coordinates_url = '/api/fields/1/coordinates/'
    field_zones_url = '/api/fields/1/zones/'

    def test_well_list(self):
        response = self.client.get('/api/wells/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_well_detail(self):
        response = self.client.get('/api/wells/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], '99R')

    def test_well_create(self):
        response = self.client.post('/api/wells/', data={'name': self.new_well_name, 'field': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.new_well_name)
