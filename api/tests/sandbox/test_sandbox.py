from django.db import connection
from rest_framework.test import APITestCase

from api import queries
from api.utils.mappers import map_mer_view


class TestBatchApi(APITestCase):
    fixtures = ['api.json']

    def test_sandbox(self):
        with connection.cursor() as cursor:
            cursor.execute(queries.MER_RANGE, [1])
            rows = cursor.fetchall()
            mer = [map_mer_view(row) for row in rows]
            for m in mer:
                print(m)
