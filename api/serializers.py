from rest_framework import serializers

from api.models import Field, Well, Inclinometry, Mer, Rate, FieldCoordinate, Zone


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class WellSerializer(serializers.ModelSerializer):

    def get_unique_together_validators(self):
        return []

    class Meta:
        model = Well
        fields = '__all__'


class IncSerializer(serializers.ModelSerializer):
    well = serializers.CharField(required=False)

    class Meta:
        model = Inclinometry
        fields = '__all__'


class MerSerializer(serializers.ModelSerializer):
    well = serializers.CharField()

    class Meta:
        model = Mer
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    well = serializers.CharField()

    class Meta:
        model = Rate
        fields = '__all__'


class FieldCoordinateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FieldCoordinate
        exclude = ('field',)


class ZoneSerializer(serializers.ModelSerializer):
    well = serializers.CharField()

    class Meta:
        model = Zone
        fields = '__all__'
