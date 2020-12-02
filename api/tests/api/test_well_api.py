from rest_framework.test import APITestCase


class TestFieldApi(APITestCase):
    fixtures = ['api.json']
    new_field_name = 'New Filat'
    field_list_url = '/api/fields/'
    field_detail_url = '/api/fields/1/'
    field_wells_url = '/api/fields/1/wells/'
    field_inc_url = '/api/fields/1/inclinometry/'
    field_mer_url = '/api/fields/1/mer/'
    field_rates_url = '/api/fields/1/rates/'
    field_coordinates_url = '/api/fields/1/coordinates/'
    field_zones_url = '/api/fields/1/zones/'

    def test_field_list(self):
        pass
   