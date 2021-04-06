from rest_framework import serializers

from api.models import Field, Well, Inclinometry, Mer, Rate, FieldCoordinate, Zone, WellCase, WellPump, WellPerforation


class FieldSerializer(serializers.ModelSerializer):
    class Meta:
        model = Field
        fields = '__all__'


class WellListSerializer(serializers.ListSerializer):
    """"Serializer for batch well load"""

    # Update or create well
    def update(self, instance, validated_data):
        # Existing wells
        well_mapping = {well.name: well for well in instance}
        # loaded wells
        data_mapping = {item['name']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for well_name, data in data_mapping.items():
            well = well_mapping.get(well_name, None)
            if well is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(well, data))

        return ret


class WellSerializer(serializers.ModelSerializer):

    # Disable unique name-field constraint for batch well load
    def get_unique_together_validators(self):
        return []

    class Meta:
        model = Well
        fields = '__all__'
        list_serializer_class = WellListSerializer


class IncSerializer(serializers.ModelSerializer):
    well = serializers.CharField(required=False)

    class Meta:
        model = Inclinometry
        fields = '__all__'


class MerSerializer(serializers.ModelSerializer):
    well = serializers.CharField()
    date = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = Mer
        fields = '__all__'


class RateSerializer(serializers.ModelSerializer):
    well = serializers.CharField()
    date = serializers.DateField(format='%d.%m.%Y')

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


class WellCaseSerializer(serializers.ModelSerializer):
    well = serializers.CharField()

    class Meta:
        model = WellCase
        fields = '__all__'


class WellPerforationSerializer(serializers.ModelSerializer):
    well = serializers.CharField()

    class Meta:
        model = WellPerforation
        fields = '__all__'


class WellPumpSerializer(serializers.ModelSerializer):
    well = serializers.CharField()

    class Meta:
        model = WellPump
        fields = '__all__'


class BatchSerializer(serializers.Serializer):
    field_id = serializers.IntegerField()
    rows = serializers.ListField()
