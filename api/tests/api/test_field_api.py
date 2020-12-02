from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.models import Field, Inclinometry, Mer, Rate, FieldCoordinate, Zone


class TestFieldRoutes(APITestCase):
    client = APIClient()
    fixtures = ['api.json']
    field_name = 'Filat'
    new_field_name = 'New Filat'
    field_list_url = '/api/fields'
    field_detail_url = '/api/fields/1/'
    field_inc_url = '/api/fields/1/inclinometry'
    field_mer_url = '/api/fields/1/mer'
    field_rates_url = '/api/fields/1/rates'
    field_coordinates_url = '/api/fields/1/coordinates'
    field_zones_url = '/api/fields/1/zones'

    def test_field_list(self):
        # Post field
        response = self.client.post(self.field_list_url, {'name': self.field_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.field_name)

        # Get all fields
        response = self.client.get(self.field_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

        # Delete all field
        response = self.client.delete(self.field_list_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Field.objects.all().count(), 0)

    def test_field_detail(self):
        # Get field
        response = self.client.get(self.field_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update field
        response = self.client.put(self.field_detail_url, {'name': self.new_field_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete one field
        response = self.client.delete(self.field_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Field.objects.all().count(), 1)

    def test_field_inc(self):
        # Get inc
        response = self.client.get(self.field_inc_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete inc
        response = self.client.delete(self.field_inc_url)
        self.assertEqual(Inclinometry.objects.count(), 0)

    def test_field_mer(self):
        # Get mer
        response = self.client.get(self.field_mer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete mer
        response = self.client.delete(self.field_mer_url)
        self.assertEqual(Mer.objects.count(), 0)

    def test_field_rates(self):
        # Get rate
        response = self.client.get(self.field_rates_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete rate
        response = self.client.delete(self.field_rates_url)
        self.assertEqual(Rate.objects.count(), 0)

    def test_field_coordinates(self):
        # Get coordinates
        response = self.client.get(self.field_coordinates_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete coordinates
        response = self.client.delete(self.field_coordinates_url)
        self.assertEqual(FieldCoordinate.objects.count(), 0)

    def test_field_zones(self):
        # Get rate
        response = self.client.get(self.field_zones_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete rate
        response = self.client.delete(self.field_zones_url)
        self.assertEqual(Zone.objects.count(), 0)
