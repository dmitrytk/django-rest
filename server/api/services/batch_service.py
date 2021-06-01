from typing import List, Optional, Set

from django.db import transaction
from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer

from api import queries
from api.models import Inclinometry, Well, FieldCoordinate
from api.serializers import IncSerializer, MerSerializer, RateSerializer, FieldCoordinateSerializer, \
    WellSerializer, WellCaseSerializer, WellPerforationSerializer, WellPumpSerializer, WellHorizonSerializer
from api.services.raw_sql_service import batch_load
from api.utils import mappers
from api.utils.validators import validate_batch_data


def get_error_details(errors: dict) -> dict:
    """Get detailed error message from DRF ErrorDetail"""
    result = {'errors count': len(errors), 'errors': []}
    for err in errors:
        for key, value in err.items():
            k = key
            v = "\t".join([vv for vv in value])
            result['errors'].append(f'{k}: {v}')
    return result


def invalid_data_error(serializer: Optional[Serializer] = None) -> Response:
    """Return 422 Status and serializer errors"""
    payload = {'message': 'Некорректные данные'}
    if serializer is not None:
        payload['errors'] = get_error_details(serializer.errors)
    return Response(payload, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


@transaction.atomic
def load_wells(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    for row in data['rows']:
        row['field'] = data['field_id']

    serializer = WellSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        well_names = set([well['name'] for well in data['rows']])
        old_wells = Well.objects.filter(field_id=data['field_id'], name__in=well_names)
        serializer.update(old_wells, serializer.validated_data)
        return Response({'message': f'Загружено скважин: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


@transaction.atomic
def load_inclinometry(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    field_id = data['field_id']
    serializer = IncSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['rows'])
        _create_new_wells(field_id, wells)
        _delete_old_inc(field_id, wells)
        batch_load(queries.INCLINOMETRY_LOAD, [(field_id, *mappers.map_inc(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено инклинометрии: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


@transaction.atomic
def load_mer(data: dict) -> Response:
    if not validate_batch_data(data):
        print('not valid')
        return invalid_data_error()
    field_id = data['field_id']
    serializer = MerSerializer(data=data['rows'], many=True)
    if serializer.is_valid():

        wells = _get_well_names(data['rows'])
        _create_new_wells(field_id, wells)
        batch_load(queries.MER_LOAD, [(field_id, *mappers.map_mer(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено МЭР: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        print(serializer.errors)
        return invalid_data_error(serializer)


@transaction.atomic
def load_rates(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    field_id = data['field_id']
    serializer = RateSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['rows'])
        _create_new_wells(field_id, wells)
        batch_load(queries.RATE_LOAD, [(field_id, *mappers.map_rate(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено режимных наблюдений: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


@transaction.atomic
def load_horizons(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    field_id = data['field_id']
    serializer = WellHorizonSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['rows'])
        _create_new_wells(field_id, wells)
        batch_load(queries.HORIZON_LOAD, [(field_id, *mappers.map_horizon(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено пластов: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


@transaction.atomic
def load_cases(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    field_id = data['field_id']
    serializer = WellCaseSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['rows'])
        _create_new_wells(field_id, wells)
        batch_load(queries.CASE_LOAD, [(field_id, *mappers.map_case(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено обсадных колонн: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


@transaction.atomic
def load_perforations(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    field_id = data['field_id']
    serializer = WellPerforationSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['rows'])
        _create_new_wells(field_id, wells)
        batch_load(queries.PERFORATION_LOAD,
                   [(field_id, *mappers.map_perforation(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено интервалов перфорации: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


@transaction.atomic
def load_pumps(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    field_id = data['field_id']
    serializer = WellPumpSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        wells = _get_well_names(data['rows'])
        _create_new_wells(field_id, wells)
        batch_load(queries.PUMP_LOAD, [(field_id, *mappers.map_pump(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено насосов: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


@transaction.atomic
def load_coordinates(data: dict) -> Response:
    if not validate_batch_data(data):
        return invalid_data_error()
    field_id = data['field_id']
    serializer = FieldCoordinateSerializer(data=data['rows'], many=True)
    if serializer.is_valid():
        _delete_old_coordinates(field_id)
        batch_load(queries.COORDINATE_LOAD,
                   [(field_id, *mappers.map_coordinate(row)) for row in serializer.validated_data])
        return Response({'message': f'Загружено координат: {len(serializer.validated_data)}'},
                        status=status.HTTP_200_OK)
    else:
        return invalid_data_error(serializer)


def _get_well_names(data: List[dict]) -> Set[str]:
    """Return well names set from input data"""
    result = {row.get('well') for row in data if row.get('well') is not None}
    return result


def _create_new_wells(field_id: int, well_names: Set[str]) -> None:
    """Create new wells if not exists"""
    return Well.objects.bulk_create(
        [Well(name=well_name, field_id=field_id) for well_name in well_names], ignore_conflicts=True
    )


def _delete_old_inc(field_id: int, well_names: Set[str]) -> None:
    """Delete old inclinometry for loaded wells"""
    return Inclinometry.objects \
        .filter(well__field_id=field_id, well__name__in=well_names) \
        .delete()


def _delete_old_coordinates(field_id: int) -> None:
    return FieldCoordinate.objects.filter(field_id=field_id).delete()
