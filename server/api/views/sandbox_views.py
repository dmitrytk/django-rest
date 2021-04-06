from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import Field
from api.serializers import IncSerializer


class SandboxViewSet(viewsets.ViewSet):
    def list(self, request):
        field = Field.objects.get(name='Carichan')
        data = {
            'field_id': field.id,
            'rows': [
                {'well': '99R', 'md': 25, 'inc': 36, 'azi': 45.2},
            ]
        }

        serializer = IncSerializer(data=data['rows'], many=True)
        print(serializer.is_valid())

        return Response({'message': 'Hello world'}, status=status.HTTP_200_OK)
