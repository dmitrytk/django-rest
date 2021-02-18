from django.test import SimpleTestCase

from api.utils.validators import validate_batch_data


class TestValidators(SimpleTestCase):

    def test_batch_validators(self):
        valid_data = {'field_id': 1, 'rows': [1, 2]}
        invalid_data = {'field_id': 1, 'rows': 'red'}
        self.assertEqual(validate_batch_data(valid_data), True)
        self.assertEqual(validate_batch_data(invalid_data), False)
