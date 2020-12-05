from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Well, Inclinometry, Mer, Rate, Zone


class TestFieldApi(APITestCase):
    fixtures = ['api.json']
    new_well_name = '1P'
    well_list_url = '/api/wells/'
    well_detail_url = '/api/wells/1/'
    well_wells_url = '/api/wells/1/wells/'
    well_inc_url = '/api/wells/1/inclinometry/'
    well_mer_url = '/api/wells/1/mer/'
    well_rates_url = '/api/wells/1/rates/'
    well_coordinates_url = '/api/wells/1/coordinates/'
    well_zones_url = '/api/wells/1/zones/'

    # BASIC CRUD
    def test_well_list(self):
        response = self.client.get(self.well_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_well_detail(self):
        response = self.client.get(self.well_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], '99R')

    def test_well_create(self):
        response = self.client.post(self.well_list_url, data={'name': self.new_well_name, 'field': 1})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.new_well_name)

    def test_well_update(self):
        response = self.client.put(self.well_detail_url, data={'name': '1z', 'field': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], '1z')

    def test_well_delete(self):
        response = self.client.delete(self.well_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Well.objects.count(), 2)

    # GET CHILD OBJECTS
    def test_get_well_inclinometry(self):
        response = self.client.get(self.well_inc_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_well_mer(self):
        response = self.client.get(self.well_mer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_well_rates(self):
        response = self.client.get(self.well_rates_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_well_zones(self):
        response = self.client.get(self.well_zones_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    # DELETE CHILD OBJECTS
    def test_delete_well_inclinometry(self):
        response = self.client.delete(self.well_inc_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Inclinometry.objects.count(), 0)

    def test_delete_well_mer(self):
        response = self.client.delete(self.well_mer_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Mer.objects.count(), 0)

    def test_delete_well_rates(self):
        response = self.client.delete(self.well_rates_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Rate.objects.count(), 0)

    def test_delete_well_zones(self):
        response = self.client.delete(self.well_zones_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Zone.objects.count(), 0)
