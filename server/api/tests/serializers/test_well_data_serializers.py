from django.test import SimpleTestCase

from api.serializers import IncSerializer, RateSerializer, MerSerializer


class TestSerializer(SimpleTestCase):
    well_name = '99R'

    def test_mer_serialization(self):
        valid_data = [{'well': self.well_name, 'date': '01.01.2020'}]
        invalid_data = [{'well': self.well_name}]
        serializer = MerSerializer(data=valid_data, many=True)
        self.assertEqual(serializer.is_valid(), True)
        serializer = MerSerializer(data=invalid_data, many=True)
        self.assertEqual(serializer.is_valid(), False)

    def test_inc_serialization(self):
        valid_data = [{'well': self.well_name, 'md': 10.20, 'inc': 25.35, 'azi': 45.68}]
        invalid_data = [{'well': self.well_name}]
        serializer = IncSerializer(data=valid_data, many=True)
        self.assertEqual(serializer.is_valid(), True)
        serializer = IncSerializer(data=invalid_data, many=True)
        self.assertEqual(serializer.is_valid(), False)

    def test_rate_serialization(self):
        valid_data = [{'well': self.well_name, 'date': '01.01.2020', 'rate': 4568.68, 'pressure': 45.65}]
        invalid_data = [{'well': self.well_name}]
        serializer = RateSerializer(data=valid_data, many=True)
        self.assertEqual(serializer.is_valid(), True)
        serializer = RateSerializer(data=invalid_data, many=True)
        self.assertEqual(serializer.is_valid(), False)
