from typing import List, Callable, Type

from django.http import JsonResponse
from rest_framework import status
from rest_framework.serializers import ModelSerializer

from api import queries
from api.models import Inclinometry, Well
from api.serializers import IncSerializer, MerSerializer
from api.services.raw_sql_service import batch_load
from api.utils import mappers
from api.utils.validators import validate_batch_data


def load_inclinometry(data) -> JsonResponse:
    if not validate_batch_data(data):
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    field_id = data['field_id']
    serializer = IncSerializer(data=data['data'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['data'])
        _delete_old_inc(field_id, wells)
        batch_load(queries.INCLINOMETRY_LOAD, [(field_id, *mappers.map_inc(row)) for row in serializer.validated_data])
        return JsonResponse(serializer.validated_data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def load_mer(data) -> JsonResponse:
    if not validate_batch_data(data):
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    field_id = data['field_id']
    serializer = MerSerializer(data=data['data'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['data'])
        batch_load(queries.MER_LOAD, [(field_id, *mappers.map_mer(row)) for row in serializer.validated_data])
        return JsonResponse(serializer.validated_data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def load_data(data: dict, serializer: Type[ModelSerializer], query: str, mapper: Callable) -> JsonResponse:
    if not validate_batch_data(data):
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    field_id = data['field_id']
    ser = serializer(data=data, many=True)
    if ser.is_valid():
        wells = _get_well_names(data['data'])
        batch_load(query, [(field_id, *mapper(row)) for row in ser.validated_data])
        return JsonResponse(ser.validated_data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def _get_well_names(data: List[dict]) -> List[str]:
    return [row['well'] for row in data]


def _create_new_wells(field_id: int, well_names: List[str]) -> None:
    return Well.objects.bulk_create(
        [Well(name=well_name, field_id=field_id) for well_name in well_names], ignore_conflicts=True
    )


def _delete_old_inc(field_id: int, well_name_list: List[str]) -> None:
    return Inclinometry.objects \
        .filter(well__field_id=field_id, well__name__in=well_name_list) \
        .delete()
