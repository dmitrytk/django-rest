import pytest
from rest_framework import status

from api.models import Field, Well, Inclinometry, Mer, Rate, FieldCoordinate, Zone

pytestmark = pytest.mark.django_db


class TestFieldApi:

    def test_field_list(self, api_client, field):
        field_list_url = '/api/fields/'
        # Post field
        response = api_client.post(field_list_url, {'name': 'New_Field'})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'New_Field'

        # Get all fields
        response = api_client.get(field_list_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

    #
    def test_field_detail(self, api_client, field):
        field_detail_url = f'/api/fields/{field.id}/'
        # Get field
        response = api_client.get(field_detail_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == field.name

        # Update field
        response = api_client.put(field_detail_url, {'name': 'New_Field'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == 'New_Field'

        # Delete one field
        response = api_client.delete(field_detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Field.objects.count() == 0

    def test_field_wells(self, api_client, field, well):
        field_wells_url = f'/api/fields/{field.id}/wells/'
        # Get wells
        response = api_client.get(field_wells_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

        # Delete wells
        response = api_client.delete(field_wells_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Well.objects.count() == 0

    def test_field_inc(self, api_client, field, inc):
        field_inc_url = f'/api/fields/{field.id}/inclinometry/'
        # Get inc
        response = api_client.get(field_inc_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete inc
        response = api_client.delete(field_inc_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Inclinometry.objects.count() == 0

    def test_field_mer(self, api_client, field, mer):
        field_mer_url = f'/api/fields/{field.id}/mer/'
        # Get mer
        response = api_client.get(field_mer_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete mer
        response = api_client.delete(field_mer_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Mer.objects.count() == 0

    def test_field_rates(self, api_client, field, rates):
        field_rates_url = f'/api/fields/{field.id}/rates/'
        # Get rate
        response = api_client.get(field_rates_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete rate
        response = api_client.delete(field_rates_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Rate.objects.count() == 0

    def test_field_coordinates(self, api_client, field, coordinates):
        field_coordinates_url = f'/api/fields/{field.id}/coordinates/'
        # Get coordinates
        response = api_client.get(field_coordinates_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete coordinates
        response = api_client.delete(field_coordinates_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert FieldCoordinate.objects.count() == 0

    def test_field_zones(self, api_client, field, zones):
        field_zones_url = f'/api/fields/{field.id}/zones/'
        # Get zones
        response = api_client.get(field_zones_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete zones
        response = api_client.delete(field_zones_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Zone.objects.count() == 0
