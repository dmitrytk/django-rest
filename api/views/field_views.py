from rest_framework import viewsets
from rest_framework.decorators import action

from api.models import Field
from api.serializers import FieldSerializer
from api.services import field_service


class FieldViewSet(viewsets.ModelViewSet):
    queryset = Field.objects.all()
    serializer_class = FieldSerializer

    # Child objects
    @action(detail=True, methods=['get', 'delete'])
    def wells(self, request, *args, **kwargs):
        if request.method == 'GET':
            return field_service.get_field_wells(self.get_object().id)
        elif request.method == 'DELETE':
            return field_service.delete_field_wells(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def inclinometry(self, request, *args, **kwargs):
        if request.method == 'GET':
            return field_service.get_field_inclinometry(self.get_object().id)
        elif request.method == 'DELETE':
            return field_service.delete_field_inclinometry(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def mer(self, request, *args, **kwargs):
        if request.method == 'GET':
            return field_service.get_field_mer(self.get_object().id)
        elif request.method == 'DELETE':
            return field_service.delete_field_mer(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def rates(self, request, *args, **kwargs):
        if request.method == 'GET':
            return field_service.get_field_rates(self.get_object().id)
        elif request.method == 'DELETE':
            return field_service.delete_field_rates(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def zones(self, request, *args, **kwargs):
        if request.method == 'GET':
            return field_service.get_field_zones(self.get_object().id)
        elif request.method == 'DELETE':
            return field_service.delete_field_zones(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def coordinates(self, request, *args, **kwargs):
        if request.method == 'GET':
            return field_service.get_field_coordinates(self.get_object().id)
        elif request.method == 'DELETE':
            return field_service.delete_field_coordinates(self.get_object().id)
