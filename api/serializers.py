from rest_framework import serializers

from api.models import Field, Well, Inclinometry, Mer, Rate


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class WellSerializer(serializers.ModelSerializer):
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


class TestSerializer(serializers.Serializer):
    well = serializers.CharField()
    md = serializers.DecimalField(max_digits=20, decimal_places=2)
    inc = serializers.DecimalField(max_digits=20, decimal_places=2, required=False)
    azi = serializers.DecimalField(max_digits=20, decimal_places=2, required=False)

    class Meta:
        fields = '__all__'
