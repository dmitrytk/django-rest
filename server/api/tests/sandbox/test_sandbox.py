from rest_framework.test import APITestCase

from api.models import Field
from api.tests.utils.populate import populate_db


class TestSandbox(APITestCase):
    def setUp(self):
        populate_db()

    def test_sandbox(self):
        field = Field.objects.all().first()
        self.assertEqual(field.name, 'Carichan')
