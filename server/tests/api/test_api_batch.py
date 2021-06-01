import pytest
from django.urls import reverse
from rest_framework import status

from api.models import Well, Inclinometry, Mer, Rate, WellHorizon, FieldCoordinate, WellCase, WellPump, WellPerforation

pytestmark = pytest.mark.django_db


class TestBatchApi:

    def test_load_wells(self, api_client, field, well):
        data = {
            'field_id': field.id,
            'rows': [
                {'name': well.name, 'bottom': 3000},
                {'name': '1P'},
            ]
        }
        response = api_client.post(reverse('api:batch-wells'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено скважин: 2'
        assert Well.objects.count() == 2

    def test_load_inclinometry(self, api_client, field, well, inc):
        data = {
            'field_id': field.id,
            'rows': [
                {'well': well.name, 'md': 10, 'inc': None, 'azi': 78.23},
                {'well': well.name, 'md': 20},
                {'well': '1P', 'md': 1},  # add new well
            ]
        }
        response = api_client.post(reverse('api:batch-inclinometry'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено инклинометрии: 3'
        assert Inclinometry.objects.count() == 3

    def test_load_mer(self, api_client, well, well_work_type, well_state, mer):
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'date': '01.01.2000', 'state': well_state.value_full,
                 'work_type': well_work_type.value_full},
                {'well': well.name, 'date': '01.01.2000', 'state': well_state.value_full,
                 'work_type': well_work_type.value_full},  # duplicate date will be overwritten
                {'well': '1P', 'date': '01.01.2000', 'state': well_state.value_full,
                 'work_type': well_work_type.value_full},  # add new well
            ]
        }
        response = api_client.post(reverse('api:batch-mer'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено МЭР: 3'
        assert Mer.objects.all().count() == 12

    def test_load_rates(self, api_client, well, well_work_type, rates):
        data = {
            'field_id': well.field.id,
            'rows': [
                {'well': well.name, 'date': '01.01.2000', 'rate': 256.78, 'work_type': well_work_type.value_full},
                {'well': well.name, 'date': '01.01.2000'},
                {'well': '1P', 'date': '01.01.2000'},  # add new well
            ]
        }
        response = api_client.post(reverse('api:batch-rates'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено режимных наблюдений: 3'
        assert Rate.objects.all().count() == 13

    def test_load_horizons(self, api_client, well, horizon, well_horizon):
        data = {
            'field_id': well.field.id,
            'rows': [
                # duplicate horizon will be overwritten
                {'well': well.name, 'horizon': horizon.value_full, 'top_md': 1500.25},
                {'well': '1P', 'horizon': horizon.value_full, 'top_md': 860.25},  # add new well
            ]
        }
        response = api_client.post(reverse('api:batch-horizons'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено пластов: 2'
        assert WellHorizon.objects.all().count() == 2

    def test_load_coordinates(self, api_client, field, coordinates):
        data = {
            'field_id': field.id,
            'rows': [
                {'lat': 60.2345, 'lng': 50.28, 'x': 312312323, 'y': 4423424234},
                {'lat': 60.28, 'lng': 50.29, 'x': 312312323, 'y': 4423424234},
            ]
        }
        response = api_client.post(reverse('api:batch-coordinates'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено координат: 2'
        assert FieldCoordinate.objects.all().count() == 2

    def test_load_cases(self, api_client, field, well, cases):
        data = {
            'field_id': field.id,
            'rows': [
                {'well': well.name, 'name': 'кондуктор', 'diameter': 425},
            ]
        }
        response = api_client.post(reverse('api:batch-cases'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено обсадных колонн: 1'
        assert WellCase.objects.all().count() == 11

    def test_load_pumps(self, api_client, field, well, pump):
        data = {
            'field_id': field.id,
            'rows': [
                {'well': well.name, 'name': '11000Z', 'diameter': 146},
            ]
        }
        response = api_client.post(reverse('api:batch-pumps'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено насосов: 1'
        assert WellPump.objects.all().count() == 1

    def test_load_perforations(self, api_client, field, well, perforations):
        data = {
            'field_id': field.id,
            'rows': [
                {'well': well.name, 'top_md': 1250, 'bot_md': 1260},
                {'well': well.name, 'top_md': 1270, 'bot_md': 1280},
            ]
        }
        response = api_client.post(reverse('api:batch-perforations'), data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['message'] == 'Загружено интервалов перфорации: 2'
        assert WellPerforation.objects.all().count() == 12
