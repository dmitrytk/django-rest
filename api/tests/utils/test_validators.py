import time

from django.test import SimpleTestCase

from api.models import Inclinometry
from api.serializers import TestSerializer
from api.utils.validators import validate_batch_data


class TestSerializers(SimpleTestCase):

    def test_batch_validators(self):
        valid_data = {'field_id': 1, 'data': [1, 2]}
        invalid_data = {'field_id': 1, 'data': 'red'}
        self.assertEqual(validate_batch_data(valid_data), True)
        self.assertEqual(validate_batch_data(invalid_data), False)

    def test_serializer(self):
        start = time.time()
        lst = [{"well": "99R", 'md': 0} for i in range(2)]
        ser = TestSerializer(data=lst, many=True)
        if ser.is_valid():
            print('valid')
        print(Inclinometry.__dict__.keys())
        end = time.time()

        print(f'{end - start} sec')
