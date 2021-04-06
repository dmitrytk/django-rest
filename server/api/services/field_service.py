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
# /fields/{id}/wells
def get_field_wells(pk):
    wells = Well.objects.filter(field_id=pk)
    serializer = WellSerializer(wells, many=True)
    return Response(serializer.data)


# /fields/{id}/inclinometry
def get_field_inclinometry(pk):
    inc = Inclinometry.objects.filter(well__field_id=pk)
    serializer = IncSerializer(inc, many=True)
    return Response(serializer.data)


# /fields/{id}/mer
def get_field_mer(pk):
    mer = Mer.objects.filter(well__field_id=pk)
    serializer = MerSerializer(mer, many=True)
    return Response(serializer.data)


# /fields/{id}/rates
def get_field_rates(pk):
    rate = Rate.objects.filter(well__field_id=pk)
    serializer = RateSerializer(rate, many=True)
    return Response(serializer.data)


# /fields/{id}/coordinates
def get_field_coordinates(pk):
    rate = FieldCoordinate.objects.filter(field_id=pk)
    serializer = FieldCoordinateSerializer(rate, many=True)
    return Response(serializer.data)


# /fields/{id}/zones
def get_field_zones(pk):
    rate = Zone.objects.filter(well__field_id=pk)
    serializer = ZoneSerializer(rate, many=True)
    return Response(serializer.data)


# DELETE CHILD OBJECTS
# /fields/{id}/wells
def delete_field_wells(pk):
    _, deleted = Well.objects.filter(field_id=pk).delete()
    return Response({'message': f'{deleted["api.Well"]} Wells were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/inclinometry
def delete_field_inclinometry(pk):
    count = Inclinometry.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Inc were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/mer
def delete_field_mer(pk):
    count = Mer.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Mer were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/rates
def delete_field_rates(pk):
    count = Rate.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Rates were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/coordinates
def delete_field_coordinates(pk):
    count = FieldCoordinate.objects.filter(field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Coordinates were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/zones
def delete_field_zones(pk):
    count = Zone.objects.filter(well__field_id=pk).delete()
    return Response({'message': f'{[count[0]]} Zones were deleted successfully!'},
                    status=status.HTTP_204_NO_CONTENT)
