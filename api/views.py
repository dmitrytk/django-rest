from django.db import connection, transaction
from django.http.response import JsonResponse
from rest_framework import status, mixins, generics
from rest_framework.decorators import api_view

from api import queries
from api.models import Field
from api.serializers import FieldSerializer, TestSerializer
from api.services import field_service
from api.utils.validators import validate_batch_data


class FieldList(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                generics.GenericAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        count = self.queryset.delete()
        return JsonResponse({'message': '{} Fields were deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


class FieldDetail(mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


@api_view(['GET'])
def field_wells(request, pk):
    return field_service.get_field_wells(pk)


@api_view(['GET', 'DELETE'])
def field_inclinometry(request, pk):
    if request.method == 'GET':
        return field_service.get_field_inclinometry(pk)
    elif request.method == 'DELETE':
        return field_service.delete_field_inclinometry(pk)


# SANDBOX
def execute(data):
    with connection.cursor() as cursor:
        cursor.executemany(queries.INCLINOMETRY_LOAD, data)


@transaction.atomic
@api_view(['POST'])
def sandbox(request):
    if not validate_batch_data(request.data):
        return JsonResponse({'message': 'Invalid data'}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    field_id = request.data['field_id']
    serializer = TestSerializer(data=request.data['data'], many=True)
    if serializer.is_valid():
        print(serializer.instance)
        return JsonResponse(serializer.validated_data, safe=False)
    return JsonResponse({'message': 'Invalid'})
