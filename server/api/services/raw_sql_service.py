from typing import List, Tuple, Any, Callable

from django.db import connection


def batch_load(query: str, data: List[Tuple]) -> None:
    """Batch data load"""
    with connection.cursor() as cursor:
        cursor.executemany(query, data)


def get_raw_view(query: str, query_params: List[Any], mapper: Callable) -> List[dict]:
    """Get mapped queryset from raw SQL query"""
    with connection.cursor() as cursor:
        cursor.execute(query, query_params)
        rows = cursor.fetchall()
        print(rows)
        data = [mapper(row) for row in rows]
    return data
