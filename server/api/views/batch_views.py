from rest_framework import viewsets
from rest_framework.decorators import action

from api.services import batch_service


class BatchViewSet(viewsets.ViewSet):
    @action(detail=False, methods=['post'])
    def wells(self, request, *args, **kwargs):
        return batch_service.load_wells(request.data)

    @action(detail=False, methods=['post'])
    def inclinometry(self, request, *args, **kwargs):
        return batch_service.load_inclinometry(request.data)

    @action(detail=False, methods=['post'])
    def mer(self, request, *args, **kwargs):
        return batch_service.load_mer(request.data)

    @action(detail=False, methods=['post'])
    def rates(self, request, *args, **kwargs):
        return batch_service.load_rates(request.data)

    @action(detail=False, methods=['post'])
    def horizons(self, request, *args, **kwargs):
        return batch_service.load_horizons(request.data)

    @action(detail=False, methods=['post'])
    def coordinates(self, request, *args, **kwargs):
        return batch_service.load_coordinates(request.data)

    @action(detail=False, methods=['post'])
    def cases(self, request, *args, **kwargs):
        return batch_service.load_cases(request.data)

    @action(detail=False, methods=['post'])
    def perforations(self, request, *args, **kwargs):
        return batch_service.load_perforations(request.data)

    @action(detail=False, methods=['post'])
    def pumps(self, request, *args, **kwargs):
        return batch_service.load_pumps(request.data)
