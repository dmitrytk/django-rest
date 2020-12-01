from django.http import JsonResponse
from rest_framework import status

from api.models import Inclinometry, Well, Mer, Rate
from api.serializers import IncSerializer, WellSerializer, MerSerializer, RateSerializer


# CHILD OBJECTS
# /fields/{id}/wells
def get_field_wells(pk):
    wells = Well.objects.filter(well__field_id=pk)
    serializer = WellSerializer(wells, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/inclinometry
def get_field_inclinometry(pk):
    inc = Inclinometry.objects.filter(well__field_id=pk)
    serializer = IncSerializer(inc, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/mer
def get_field_mer(pk):
    mer = Mer.objects.filter(well__field_id=pk)
    serializer = MerSerializer(mer, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/rates
def get_field_rates(pk):
    rate = Rate.objects.filter(well__field_id=pk)
    serializer = RateSerializer(rate, many=True)
    return JsonResponse(serializer.data, safe=False)


# /fields/{id}/inclinometry DELETE
def delete_field_inclinometry(pk):
    count = Inclinometry.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Inc were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/mer DELETE
def delete_field_mer(pk):
    count = Mer.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Mer were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)


# /fields/{id}/rates DELETE
def delete_field_rates(pk):
    count = Rate.objects.filter(well__field_id=pk).delete()
    return JsonResponse({'message': '{} Rates were deleted successfully!'.format(count[0])},
                        status=status.HTTP_204_NO_CONTENT)
