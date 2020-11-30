from django.http import JsonResponse
from rest_framework import status
from rest_framework.parsers import JSONParser

from api.models import Field, Inclinometry
from api.serializers import FieldSerializer, WellSerializer, IncSerializer


# BASIC CRUD
# /fields GET
def get_all():
    fields = Field.objects.all()
    fields_serializer = FieldSerializer(fields, many=True)
    return JsonResponse(fields_serializer.data, safe=False)


# /fields/:id GET
def get_one(field):
    field_serializer = FieldSerializer(field)
    return JsonResponse(field_serializer.data)


# /fields/:id PUT
def update(request, field):
    field_data = JSONParser().parse(request)
    field_serializer = FieldSerializer(field, data=field_data)
    if field_serializer.is_valid():
        field_serializer.save()
        return JsonResponse(field_serializer.data)
    return JsonResponse(field_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /fields/:id DELETE
def delete(field):
    field.delete()
    return JsonResponse({'message': 'Field was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# /fields  POST
def create(request):
    field_data = JSONParser().parse(request)
    field_serializer = FieldSerializer(data=field_data)
    if field_serializer.is_valid():
        field_serializer.save()
        return JsonResponse(field_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(field_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# /fields  DELETE
def delete_all():
    count = Field.objects.all().delete()
    return JsonResponse({'message': '{} Fields were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


# CHILD OBJECTS
# /fields/{id}/wells
def get_field_wells(pk):
    try:
        field = Field.objects.get(pk=pk)
        well_serializer = WellSerializer(field.wells, many=True)
        return JsonResponse(well_serializer.data, safe=False)
    except Field.DoesNotExist:
        return JsonResponse({'message': 'The field does not exist'}, status=status.HTTP_404_NOT_FOUND)


# /fields/{id}/inclinometry
def get_field_inclinometry(pk):
    inc = Inclinometry.objects.filter(well__field_id=pk)
    serializer = IncSerializer(inc, many=True)
    return JsonResponse(serializer.data, safe=False)


def delete_field_inclinometry(pk):
    count = Inclinometry.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Inc were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)
