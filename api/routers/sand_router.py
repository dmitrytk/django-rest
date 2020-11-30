from django.http import JsonResponse
from rest_framework import routers, viewsets, status

router = routers.SimpleRouter()


class MyViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """

    def list(self, request):
        return JsonResponse({'message': 'GET'}, status=status.HTTP_200_OK)


router.register('', MyViewSet, basename='set')
