from django.test import SimpleTestCase

from api.serializers import FieldSerializer


class TestSerializer(SimpleTestCase):
    databases = '__all__'

    def test_field_serialization(self):
        valid_data = {'name': 'Carichan'}
        invalid_data = {'type': 'Oil'}
        serializer = FieldSerializer(data=valid_data)
        self.assertEqual(serializer.is_valid(), True)
        serializer = FieldSerializer(data=invalid_data)
        self.assertEqual(serializer.is_valid(), False)
