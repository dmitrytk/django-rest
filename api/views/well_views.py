from rest_framework import generics

from api.models import Well
from api.serializers import WellSerializer


class WellList(generics.ListCreateAPIView):
    queryset = Well.objects.all()
    serializer_class = WellSerializer


class WellDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Well.objects.all()
    serializer_class = WellSerializer
