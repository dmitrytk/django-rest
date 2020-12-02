from rest_framework import status
from rest_framework.response import Response

from api.models import Inclinometry, Mer, Rate, Zone
from api.serializers import IncSerializer, MerSerializer, RateSerializer, ZoneSerializer


# GET CHILD OBJECTS
# /wells/{id}/inclinometry GET
def get_well_inclinometry(pk):
    inc = Inclinometry.objects.filter(well_id=pk)
    serializer = IncSerializer(inc, many=True)
    return Response(serializer.data)


# /wells/{id}/mer GET
def get_well_mer(pk):
    mer = Mer.objects.filter(well_id=pk)
    serializer = MerSerializer(mer, many=True)
    return Response(serializer.data)


# /wells/{id}/rates GET
def get_well_rates(pk):
    rate = Rate.objects.filter(well_id=pk)
    serializer = RateSerializer(rate, many=True)
    return Response(serializer.data)


# /wells/{id}/zones GET
def get_well_zones(pk):
    rate = Zone.objects.filter(well_id=pk)
    serializer = ZoneSerializer(rate, many=True)
    return Response(serializer.data)


# DELETE CHILD OBJECTS
# /wells/{id}/inclinometry DELETE
def delete_well_inclinometry(pk):
    count = Inclinometry.objects.filter(well_id=pk).delete()
    return Response({'message': f'{count[0]} Inc were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /wells/{id}/mer DELETE
def delete_well_mer(pk):
    count = Mer.objects.filter(well_id=pk).delete()
    return Response({'message': f'{count[0]} Mer were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /wells/{id}/rates DELETE
def delete_well_rates(pk):
    count = Rate.objects.filter(well_id=pk).delete()
    return Response({'message': f'{count[0]} Rates were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /wells/{id}/zones DELETE
def delete_well_zones(pk):
    count = Zone.objects.filter(well_id=pk).delete()
    return Response({'message': f'{count[0]} Zones were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)
