from rest_framework import status
from rest_framework.test import APITestCase

from api.models import Field, Well, Inclinometry, Mer, Rate, FieldCoordinate, Zone
from api.tests.populate import populate_db


class TestFieldApi(APITestCase):

    @classmethod
    def setUpTestData(cls):
        cls.field_name, cls.field_id, cls.well_name, cls.well_id = populate_db()
        cls.new_field_name = 'Ваделыпское'
        cls.update_field_name = 'Западно-Салымское'
        # URLS
        cls.field_list_url = '/api/fields/'
        cls.field_detail_url = f'/api/fields/{cls.field_id}/'
        cls.field_wells_url = f'/api/fields/{cls.field_id}/wells/'
        cls.field_inc_url = f'/api/fields/{cls.field_id}/inclinometry/'
        cls.field_mer_url = f'/api/fields/{cls.field_id}/mer/'
        cls.field_rates_url = f'/api/fields/{cls.field_id}/rates/'
        cls.field_coordinates_url = f'/api/fields/{cls.field_id}/coordinates/'
        cls.field_zones_url = f'/api/fields/{cls.field_id}/zones/'

    def test_field_list(self):
        # Post field
        response = self.client.post(self.field_list_url, {'name': self.new_field_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], self.new_field_name)
        print("Done")

        # Get all fields
        response = self.client.get(self.field_list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    #
    def test_field_detail(self):
        # Get field
        response = self.client.get(self.field_detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Update field
        response = self.client.put(self.field_detail_url, {'name': self.update_field_name}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Delete one field
        response = self.client.delete(self.field_detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Field.objects.count(), 0)

    def test_field_wells(self):
        # Get wells
        response = self.client.get(self.field_wells_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

        # Delete wells
        response = self.client.delete(self.field_wells_url)
        self.assertEqual(Well.objects.count(), 0)

    def test_field_inc(self):
        # Get inc
        response = self.client.get(self.field_inc_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Delete inc
        response = self.client.delete(self.field_inc_url)
        self.assertEqual(Inclinometry.objects.count(), 0)

    def test_field_mer(self):
        # Get mer
        response = self.client.get(self.field_mer_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Delete mer
        response = self.client.delete(self.field_mer_url)
        self.assertEqual(Mer.objects.count(), 0)

    def test_field_rates(self):
        # Get rate
        response = self.client.get(self.field_rates_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Delete rate
        response = self.client.delete(self.field_rates_url)
        self.assertEqual(Rate.objects.count(), 0)

    def test_field_coordinates(self):
        # Get coordinates
        response = self.client.get(self.field_coordinates_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Delete coordinates
        response = self.client.delete(self.field_coordinates_url)
        self.assertEqual(FieldCoordinate.objects.count(), 0)

    def test_field_zones(self):
        # Get zones
        response = self.client.get(self.field_zones_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

        # Delete zones
        response = self.client.delete(self.field_zones_url)
        self.assertEqual(Zone.objects.count(), 0)
