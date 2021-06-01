import datetime

import pytest
from rest_framework import status

from api.models import Well, Inclinometry, Mer, Rate, WellPerforation, WellPump, WellCase, WellHorizon
from tests.api.factories import WellFactory, MerFactory, RateFactory

pytestmark = pytest.mark.django_db


class TestWellApi:

    # BASIC CRUD
    def test_well_list(self, api_client, well):
        well_list_url = '/api/wells/'

        # Get Wells
        WellFactory()
        response = api_client.get(well_list_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 2

        # Create Well
        response = api_client.post(well_list_url, data={'name': 'New Well', 'field': well.field.id})
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['name'] == 'New Well'

    def test_well_detail(self, api_client, well):
        well_detail_url = f'/api/wells/{well.id}/'

        # Get Well
        response = api_client.get(well_detail_url)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == well.name

        # Update Well
        response = api_client.put(well_detail_url,
                                  data={'name': '1z', 'field': well.field.id, 'pad': '1', 'type': 'разведочная'})
        assert response.status_code == status.HTTP_200_OK
        assert response.data['name'] == '1z'

        # Delete Well
        response = api_client.delete(well_detail_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Well.objects.count() == 0

    # GET CHILD OBJECTS
    def test_well_inclinometry(self, api_client, well, inc):
        well_inclinometry_url = f'/api/wells/{well.id}/inclinometry/'

        # Get Inclinometry
        response = api_client.get(well_inclinometry_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete Inclinometry
        response = api_client.delete(well_inclinometry_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Inclinometry.objects.count() == 0

    #
    def test_well_mer(self, api_client, well):
        well_mer_url = f'/api/wells/{well.id}/mer/'
        # Create Mer
        MerFactory(well=well, date=datetime.date(2020, 1, 1))
        MerFactory(well=well, date=datetime.date(2020, 5, 1))

        # Get Mer
        response = api_client.get(well_mer_url)
        assert response.status_code == status.HTTP_200_OK
        print(f'Mer in db: {Mer.objects.count()}')
        assert len(response.data) == 5

        # Delete Mer
        response = api_client.delete(well_mer_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Mer.objects.count() == 0

    def test_well_rates(self, api_client, well):
        well_rates_url = f'/api/wells/{well.id}/rates/'
        # Create Rates
        RateFactory(well=well, date=datetime.date(2020, 1, 1))
        RateFactory(well=well, date=datetime.date(2020, 1, 20))

        # Get Rates
        response = api_client.get(well_rates_url)
        assert response.status_code, status.HTTP_200_OK
        assert len(response.data) == 20

        # Delete Rates
        response = api_client.delete(well_rates_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert Rate.objects.count() == 0

    def test_well_horizons(self, api_client, well, well_horizon):
        well_horizons_url = f'/api/wells/{well.id}/horizons/'

        # Get Horizons
        response = api_client.get(well_horizons_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

        # Delete Horizons
        response = api_client.delete(well_horizons_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert WellHorizon.objects.count() == 0

    def test_well_perforations(self, api_client, well, perforations):
        well_perforations_url = f'/api/wells/{well.id}/perforations/'

        # Get Perforations
        response = api_client.get(well_perforations_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete Perforations
        response = api_client.delete(well_perforations_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert WellPerforation.objects.count() == 0

    def test_well_pumps(self, api_client, well, pump):
        well_pumps_url = f'/api/wells/{well.id}/pumps/'

        # Get Pumps
        response = api_client.get(well_pumps_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 1

        # Delete Pumps
        response = api_client.delete(well_pumps_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert WellPump.objects.count() == 0

    def test_well_cases(self, api_client, well, cases):
        well_cases_url = f'/api/wells/{well.id}/cases/'

        # Get Cases
        response = api_client.get(well_cases_url)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == 10

        # Delete Cases
        response = api_client.delete(well_cases_url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert WellCase.objects.count() == 0
