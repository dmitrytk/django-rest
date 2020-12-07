import time
from random import random

from rest_framework.test import APITestCase

from api.models import Well, Mer
from api.serializers import WellSerializer


class TestBatchApi(APITestCase):
    fixtures = ['api.json']

    def test_sandbox(self):
        data = {
            'field': 1,
            'rows': [
                {'name': f'Well{random()}'} for _ in range(1000)
            ]
        }
        start = time.time()
        for row in data['rows']:
            row['field'] = data['field']

        serializer = WellSerializer(data=data['rows'], many=True)
        if serializer.is_valid():
            well_names = set([well['name'] for well in data['rows']])
            old_wells = Well.objects.filter(field_id=data['field'], name__in=well_names)
            result = serializer.update(old_wells, serializer.validated_data)
            print(result)
        else:
            print(serializer.errors)
        print(f'Done in {time.time() - start} sec.')
        self.assertEqual(Well.objects.count(), 1003)
        self.assertEqual(Mer.objects.count(), 2)
