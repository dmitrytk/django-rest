from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from users.serializers import UserSerializer


@api_view()
def me(request):
    serializer = UserSerializer(request.user)
    return Response(serializer.data, status=status.HTTP_200_OK)
