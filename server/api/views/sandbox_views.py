from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.models import Field, Well, Inclinometry
from api.serializers import FieldSerializer, WellSerializer, IncSerializer


@api_view()
def sandbox(request):
    field = Field()
    field.name = "Carichan"
    well  = Well(field=field)
    inc = Inclinometry(well=well)
    ser = IncSerializer(inc)
    print(ser.data)
    return Response('foo')
