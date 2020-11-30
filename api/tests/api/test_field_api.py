from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Field


class TestFieldRoutes(APITestCase):
    field_name = 'Carichan'
    new_field_name = 'NewCarichan'
    field_list_url = '/api/fields'
    field_detail_url = '/api/fields/1/'

    def test_field_list_api(self):
        # Post field
        response = self.client.post(self.field_list_url, {'name': self.field_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.field_name)

        # Get all fields
        response = self.client.get(self.field_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Delete all field
        response = self.client.delete(self.field_list_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Field.objects.all().count(), 0)

    def test_field_detail_api(self):
        # Post field
        self.client.post(self.field_list_url, {'name': self.field_name}, format='json')
        
        # Get field
        response = self.client.get(self.field_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.field_name)

        # Update field
        response = self.client.put(self.field_detail_url, {'name': self.new_field_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Field.objects.all().first().name, self.new_field_name)

        # Delete one field
        response = self.client.delete(self.field_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Field.objects.all().count(), 0)
