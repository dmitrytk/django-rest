from rest_framework.test import APITestCase

from api.serializers import WellSerializer, IncSerializer


class TestBatchApi(APITestCase):
    fixtures = ['api.json']

    def test_sandbox(self):
        data = {
            'field': 1,
            'data': [
                {'name': 1},
                {'name': '99R'},
            ]
        }
        for row in data['data']:
            row['field'] = data['field']
        well_serializer = WellSerializer(data=data['data'], many=True)
        inc_serializer = IncSerializer(data=[{'md': 20}], many=True)
        print(well_serializer.is_valid())
        print(inc_serializer.is_valid())
        self.assertEqual(1, 1)
