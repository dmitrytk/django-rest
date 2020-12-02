from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Field
from api.serializers import FieldSerializer
from api.services import field_service


class FieldList(generics.ListCreateAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def delete(self, request, *args, **kwargs):
        _, deleted = self.queryset.delete()
        return Response({'message': f'{deleted["api.Field"]} Fields were deleted successfully!'},
                        status=status.HTTP_204_NO_CONTENT)


class FieldDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer


@api_view(['GET'])
def field_wells(request, pk):
    return field_service.get_field_wells(pk)


@api_view(['GET', 'DELETE'])
def field_inclinometry(request, pk):
    if request.method == 'GET':
        return field_service.get_field_inclinometry(pk)
    elif request.method == 'DELETE':
        return field_service.delete_field_inclinometry(pk)


@api_view(['GET', 'DELETE'])
def field_mer(request, pk):
    if request.method == 'GET':
        return field_service.get_field_mer(pk)
    elif request.method == 'DELETE':
        return field_service.delete_field_mer(pk)


@api_view(['GET', 'DELETE'])
def field_rates(request, pk):
    if request.method == 'GET':
        return field_service.get_field_rates(pk)
    elif request.method == 'DELETE':
        return field_service.delete_field_rates(pk)


@api_view(['GET', 'DELETE'])
def field_coordinates(request, pk):
    if request.method == 'GET':
        return field_service.get_field_coordinates(pk)
    elif request.method == 'DELETE':
        return field_service.delete_field_coordinates(pk)


@api_view(['GET', 'DELETE'])
def field_zones(request, pk):
    if request.method == 'GET':
        return field_service.get_field_zones(pk)
    elif request.method == 'DELETE':
        return field_service.delete_field_zones(pk)
