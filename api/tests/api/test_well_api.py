from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Well


class TestFieldApi(APITestCase):
    fixtures = ['api.json']
    well_name = '1P'
    new_well_name = '999R'
    well_list_url = '/api/fields/1/wells/'
    well_detail_url = '/api/fields/1/wells/1/'

    def test_well_list(self):
        # Post well
        response = self.client.post(self.well_list_url, {'name': self.well_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.well_name)

        # Get all wells
        response = self.client.get(self.well_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_well_detail(self):
        # Get well
        response = self.client.get(self.well_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], '99R')

        # Update well
        response = self.client.put(self.well_detail_url, {'name': self.new_well_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.new_well_name)

        # Delete one well
        response = self.client.delete(self.well_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Well.objects.count(), 2)
