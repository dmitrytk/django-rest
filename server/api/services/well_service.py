from rest_framework import status
from rest_framework.response import Response

from api import queries
from api.models import Inclinometry, Mer, Rate, Zone
from api.serializers import IncSerializer, ZoneSerializer
# GET CHILD OBJECTS
# /wells/{id}/inclinometry GET
from api.services.raw_sql_service import get_raw_view
from api.utils import mappers


def get_well_inclinometry(pk):
    inc = Inclinometry.objects.filter(well_id=pk)
    serializer = IncSerializer(inc, many=True)
    return Response(serializer.data)


# /wells/{id}/mer GET
def get_well_mer(pk):
    data = get_raw_view(queries.MER_RANGE, [pk], mappers.map_mer_view)
    return Response(data)


# /wells/{id}/rates GET
def get_well_rates(pk):
    data = get_raw_view(queries.RATES_RANGE, [pk], mappers.map_rates_view)
    return Response(data)


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
