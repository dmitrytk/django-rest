from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Well, Inclinometry, Mer, Rate, Zone
from api.tests.populate import populate_db


class TestFieldApi(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.field_name, cls.field_id, cls.well_name, cls.well_id = populate_db()

        cls.new_well_name = '1P'
        # URLS
        cls.well_list_url = '/api/wells/'
        cls.well_detail_url = f'/api/wells/{cls.well_id}/'
        cls.well_inc_url = f'/api/wells/{cls.well_id}/inclinometry/'
        cls.well_mer_url = f'/api/wells/{cls.well_id}/mer/'
        cls.well_rates_url = f'/api/wells/{cls.well_id}/rates/'
        cls.well_coordinates_url = f'/api/wells/{cls.well_id}/coordinates/'
        cls.well_zones_url = f'/api/wells/{cls.well_id}/zones/'

    # BASIC CRUD
    def test_well_list(self):
        response = self.client.get(self.well_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_well_detail(self):
        response = self.client.get(self.well_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.well_name)

    def test_well_create(self):
        response = self.client.post(self.well_list_url, data={'name': self.new_well_name, 'field': self.field_id})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.new_well_name)

    def test_well_update(self):
        response = self.client.put(self.well_detail_url,
                                   data={'name': '1z', 'field': self.field_id, 'pad': '1', 'type': 'разведочная'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], '1z')

    def test_well_delete(self):
        response = self.client.delete(self.well_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Well.objects.count(), 0)

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
