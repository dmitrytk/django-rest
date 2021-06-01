from django.db import models


class Field(models.Model):
    """Oil field model"""

    name = models.CharField(max_length=70, unique=True)
    type = models.CharField(max_length=70, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'fields'


class FieldCoordinate(models.Model):
    field = models.ForeignKey(
        Field, related_name='coordinates', on_delete=models.CASCADE)
    lat = models.FloatField(null=True, blank=True)
    lng = models.FloatField(null=True, blank=True)
    x = models.FloatField(null=True, blank=True)
    y = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'field_coordinates'

    def __str__(self):
        return f'lat={self.lat} lng={self.lng}  x={self.x}  y={self.y}'


class Well(models.Model):
    """Well model"""
    name = models.CharField(max_length=70)
    field = models.ForeignKey(
        Field, related_name='wells', on_delete=models.CASCADE)
    pad = models.CharField(max_length=70, null=True)
    type = models.CharField(max_length=70, null=True)
    status = models.CharField(max_length=200, null=True)
    alt = models.FloatField(null=True)
    bottom = models.FloatField(null=True)
    lat = models.FloatField(null=True)
    lng = models.FloatField(null=True)
    x = models.FloatField(null=True)
    y = models.FloatField(null=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        unique_together = ('name', 'field',)
        db_table = 'wells'


class Inclinometry(models.Model):
    well = models.ForeignKey(
        Well, related_name='inc', on_delete=models.CASCADE)
    md = models.FloatField()
    inc = models.FloatField(null=True)
    azi = models.FloatField(null=True)

    class Meta:
        db_table = 'inclinometry'

    def __str__(self):
        return f'well={self.well} md={self.md}   inc={self.inc}  azi={self.azi}'


class WellState(models.Model):
    value_short = models.CharField(max_length=5)
    value_full = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.value_full}'

    class Meta:
        db_table = 'well_states'


class WellWorkType(models.Model):
    value_short = models.CharField(max_length=5)
    value_full = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.value_full}'

    class Meta:
        db_table = 'well_work_types'


class Mer(models.Model):
    well = models.ForeignKey(
        Well, related_name='mer', on_delete=models.CASCADE)
    date = models.DateField()
    production = models.FloatField(null=True)
    work_hours = models.FloatField(null=True)
    work_type = models.ForeignKey(WellWorkType, related_name='mer_work_type', on_delete=models.DO_NOTHING, null=True)
    state = models.ForeignKey(WellState, related_name='mer_state', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'well={self.well} date={self.date} production={self.production} work_type={self.work_type} state={self.state}'

    class Meta:
        unique_together = ('well', 'date',)
        db_table = 'mer'


class Rate(models.Model):
    well = models.ForeignKey(
        Well, related_name='rate', on_delete=models.CASCADE)
    date = models.DateField()
    rate = models.FloatField(null=True)
    dynamic_level = models.FloatField(null=True)
    static_level = models.FloatField(null=True)
    pressure = models.FloatField(null=True)
    work_type = models.ForeignKey(WellWorkType, related_name='rate_work_type', on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f'well={self.well} date={self.date} rate={self.rate} work_type={self.work_type}'

    class Meta:
        db_table = 'rates'


class HorizonType(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'horizon_types'


class Horizon(models.Model):
    field = models.ForeignKey(
        Field, on_delete=models.CASCADE)
    type = models.ForeignKey(
        HorizonType, on_delete=models.CASCADE)
    value_short = models.CharField(max_length=10)
    value_full = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.value_full}'

    class Meta:
        db_table = 'horizons'


class WellHorizon(models.Model):
    horizon = models.ForeignKey(
        Horizon, on_delete=models.CASCADE)
    well = models.ForeignKey(
        Well, on_delete=models.CASCADE)
    top_md = models.FloatField(null=True)
    bot_md = models.FloatField(null=True)
    top_tvdss = models.FloatField(null=True)
    bot_tvdss = models.FloatField(null=True)

    def __str__(self):
        return f'name={self.horizon} top_md={self.top_md} bot_md={self.bot_md} top_tvdss={self.top_tvdss} bot_tvdss={self.bot_tvdss}'

    class Meta:
        unique_together = ('well', 'horizon',)
        db_table = 'well_horizons'


class WellCase(models.Model):
    """Inclinometry model"""

    well = models.ForeignKey(
        Well, related_name='cases', on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    diameter = models.FloatField()
    length = models.FloatField(null=True)
    top_md = models.FloatField(null=True)
    bot_md = models.FloatField(null=True)
    cemented = models.BooleanField(null=True)
    cement_top = models.FloatField(null=True)

    def __str__(self):
        return f'Case: {self.name}  diameter={self.diameter}'

    class Meta:
        db_table = 'cases'
        unique_together = ('name', 'well',)


class WellPerforation(models.Model):
    """Inclinometry model"""

    well = models.ForeignKey(
        Well, related_name='perforations', on_delete=models.CASCADE)
    perforator_type = models.CharField(max_length=70, null=True)
    hole_diameter = models.FloatField(null=True)
    holes_per_meter = models.FloatField(null=True)
    top_md = models.FloatField()
    bot_md = models.FloatField()

    def __str__(self):
        return f'Perforation: top_md={self.top_md}  bot_md={self.bot_md}'

    class Meta:
        db_table = 'perforations'


class WellPump(models.Model):
    """Inclinometry model"""

    well = models.OneToOneField(
        Well, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    md = models.FloatField(null=True)
    rate = models.FloatField(null=True)
    diameter = models.FloatField(null=True)

    def __str__(self):
        return f'Pump: {self.name}  md={self.md}'

    class Meta:
        db_table = 'pumps'
