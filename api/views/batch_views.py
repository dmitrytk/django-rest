from rest_framework.decorators import api_view

from api.services import batch_service


@api_view(['POST'])
def load_inclinometry(request):
    return batch_service.load_inclinometry(request.data)


@api_view(['POST'])
def load_mer(request):
    return batch_service.load_mer(request.data)


@api_view(['POST'])
def load_rates(request):
    return batch_service.load_rates(request.data)


@api_view(['POST'])
def load_zones(request):
    return batch_service.load_zones(request.data)


@api_view(['POST'])
def load_coordinates(request):
    return batch_service.load_coordinates(request.data)
