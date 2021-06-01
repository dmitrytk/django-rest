from django.contrib import admin

from api.models import Field, Well, Inclinometry, Horizon, Rate, Mer, WellCase, WellPerforation, WellPump, WellWorkType, \
    WellState, HorizonType

admin.site.register(Field)
admin.site.register(Well)
admin.site.register(Inclinometry)
admin.site.register(HorizonType)
admin.site.register(Horizon)
admin.site.register(Rate)
admin.site.register(Mer)
admin.site.register(WellCase)
admin.site.register(WellPerforation)
admin.site.register(WellPump)
admin.site.register(WellWorkType)
admin.site.register(WellState)
