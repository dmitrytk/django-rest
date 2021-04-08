from rest_framework import viewsets, status
from rest_framework.response import Response


class SandboxViewSet(viewsets.ViewSet):
    def list(self, request):
        return Response({'message': 'Hello world'}, status=status.HTTP_200_OK)
