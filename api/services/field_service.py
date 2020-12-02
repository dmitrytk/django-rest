from rest_framework import status
from rest_framework.response import Response

from api.models import Inclinometry, Well, Mer, Rate, FieldCoordinate, Zone
from api.serializers import IncSerializer, WellSerializer, MerSerializer, RateSerializer, FieldCoordinateSerializer, \
    ZoneSerializer


# CREATE WELL
# /fields/{id}/wells POST
def create_well(pk, data):
    well = Well.objects.create(field_id=pk, **data)
    serializer = WellSerializer(well)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# GET CHILD OBJECTS
# /fields/{id}/wells GET
def get_field_wells(pk):
    wells = Well.objects.filter(field_id=pk)
    serializer = WellSerializer(wells, many=True)
    return Response(serializer.data)


# /fields/{id}/inclinometry GET
def get_field_inclinometry(pk):
    inc = Inclinometry.objects.filter(well__field_id=pk)
    serializer = IncSerializer(inc, many=True)
    return Response(serializer.data)


# /fields/{id}/mer GET
def get_field_mer(pk):
    mer = Mer.objects.filter(well__field_id=pk)
    serializer = MerSerializer(mer, many=True)
    return Response(serializer.data)


# /fields/{id}/rates GET
def get_field_rates(pk):
    rate = Rate.objects.filter(well__field_id=pk)
    serializer = RateSerializer(rate, many=True)
    return Response(serializer.data)


# /fields/{id}/coordinates GET
def get_field_coordinates(pk):
    rate = FieldCoordinate.objects.filter(field_id=pk)
    serializer = FieldCoordinateSerializer(rate, many=True)
    return Response(serializer.data)


# /fields/{id}/zones GET
def get_field_zones(pk):
    rate = Zone.objects.filter(well__field_id=pk)
    serializer = ZoneSerializer(rate, many=True)
    return Response(serializer.data)


# DELETE CHILD OBJECTS
# /fields/{id}/wells DELETE
def delete_field_wells(pk):
    _, deleted = Well.objects.filter(field_id=pk).delete()
    return Response({'message': f'{deleted["api.Well"]} Wells were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/inclinometry DELETE
def delete_field_inclinometry(pk):
    count = Inclinometry.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Inc were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/mer DELETE
def delete_field_mer(pk):
    count = Mer.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Mer were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/rates DELETE
def delete_field_rates(pk):
    count = Rate.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Rates were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/coordinates DELETE
def delete_field_coordinates(pk):
    count = FieldCoordinate.objects.filter(field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Coordinates were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/zones DELETE
def delete_field_zones(pk):
    count = Zone.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Zones were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)
