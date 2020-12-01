from django.db import models


class Field(models.Model):
    """Oil field model"""

    name = models.CharField(max_length=70, unique=True)
    type = models.CharField(max_length=70, null=True, blank=True)
    location = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'fields'


class FieldCoordinate(models.Model):
    field = models.ForeignKey(
        Field, related_name='coordinates', on_delete=models.CASCADE)
    lat = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    lng = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    x = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    y = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'field_coordinates'


class Well(models.Model):
    """Well model"""
    name = models.CharField(max_length=70)
    field = models.ForeignKey(
        Field, related_name='wells', on_delete=models.CASCADE)
    pad = models.CharField(max_length=70, null=True, blank=True, default='')
    type = models.CharField(max_length=200, null=True, blank=True, default='')
    status = models.CharField(max_length=200, null=True, blank=True, default='')
    alt = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    bottom = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    lat = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    lng = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    x = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)
    y = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'wells'
        unique_together = ('name', 'field',)

    def __str__(self):
        return self.name


class Inclinometry(models.Model):
    """Inclinometry model"""

    well = models.ForeignKey(
        Well, related_name='inc', on_delete=models.CASCADE)
    md = models.DecimalField(max_digits=20, decimal_places=2)
    inc = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    azi = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'inclinometry'


class AbstractRateModel(models.Model):
    """Generic production data"""

    well = models.ForeignKey(
        Well, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=50, null=True)
    rate = models.DecimalField(max_digits=30, decimal_places=2, null=True)

    class Meta:
        abstract = True


class Mer(AbstractRateModel):
    """Month production report model"""

    production = models.DecimalField(max_digits=30, decimal_places=2, null=True)
    work_days = models.IntegerField(null=True)

    class Meta:
        db_table = 'mer'
        unique_together = ('well', 'date',)


class Rate(AbstractRateModel):
    """Daily production model"""

    pressure = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    dynamic_level = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    static_level = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'rates'


class Zone(models.Model):
    """Geological Zone/Layer model"""

    well = models.ForeignKey(Well, on_delete=models.CASCADE)
    name = models.CharField(max_length=70)
    top_md = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bot_md = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    top_tvd = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    bot_tvd = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    h = models.DecimalField(max_digits=10, decimal_places=2, null=True)

    class Meta:
        db_table = 'zones'
        unique_together = ('name', 'well',)

    def __str__(self):
        return self.name
