from typing import List, Tuple

from django.db import connection


def batch_load(query: str, data: List[Tuple]) -> None:
    """Batch inclinometry load"""
    with connection.cursor() as cursor:
        cursor.executemany(query, data)
