from rest_framework import viewsets
from rest_framework.decorators import action

from api.models import Well
from api.serializers import WellSerializer
from api.services import well_service


class WellViewSet(viewsets.ModelViewSet):
    queryset = Well.objects.all()
    serializer_class = WellSerializer

    # Child objects
    @action(detail=True, methods=['get', 'delete'])
    def inclinometry(self, request, *args, **kwargs):
        if request.method == 'GET':
            return well_service.get_well_inclinometry(self.get_object().id)
        elif request.method == 'DELETE':
            return well_service.delete_well_inclinometry(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def mer(self, request, *args, **kwargs):
        if request.method == 'GET':
            return well_service.get_well_mer(self.get_object().id)
        elif request.method == 'DELETE':
            return well_service.delete_well_mer(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def rates(self, request, *args, **kwargs):
        if request.method == 'GET':
            return well_service.get_well_rates(self.get_object().id)
        elif request.method == 'DELETE':
            return well_service.delete_well_rates(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def zones(self, request, *args, **kwargs):
        if request.method == 'GET':
            return well_service.get_well_zones(self.get_object().id)
        elif request.method == 'DELETE':
            return well_service.delete_well_zones(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def cases(self, request, *args, **kwargs):
        if request.method == 'GET':
            return well_service.get_well_cases(self.get_object().id)
        elif request.method == 'DELETE':
            return well_service.delete_well_cases(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def perforations(self, request, *args, **kwargs):
        if request.method == 'GET':
            return well_service.get_well_perforations(self.get_object().id)
        elif request.method == 'DELETE':
            return well_service.delete_well_perforations(self.get_object().id)

    @action(detail=True, methods=['get', 'delete'])
    def pumps(self, request, *args, **kwargs):
        if request.method == 'GET':
            return well_service.get_well_pumps(self.get_object().id)
        elif request.method == 'DELETE':
            return well_service.delete_well_pumps(self.get_object().id)
