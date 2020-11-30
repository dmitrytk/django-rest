from typing import List

from django.http import JsonResponse
from rest_framework import status

from api.models import Inclinometry
from api.serializers import IncSerializer
from api.utils.validators import validate_batch_data


def load_inclinometry(request) -> JsonResponse:
    if not validate_batch_data(request.data):
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    field_id = request.data['field_id']
    serializer = IncSerializer(data=request.data['data'], many=True, allow_empty=False)
    if serializer.is_valid():
        wells = _get_well_names(request.data['data'])
        _delete_old_inc(field_id, wells)
        return JsonResponse(serializer.validated_data, safe=False)
    else:
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)


def _get_well_names(data: List[dict]) -> List[str]:
    return [row['well'] for row in data]


def _delete_old_inc(field_id: int, well_name_list: List[str]) -> None:
    return Inclinometry.objects \
        .filter(well__field_id=field_id, well__name__in=well_name_list) \
        .delete()
