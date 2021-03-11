from django.contrib import admin

from api.models import Field, Well, Inclinometry, Zone, Rate, Mer

admin.site.register(Field)
admin.site.register(Well)
admin.site.register(Inclinometry)
admin.site.register(Zone)
admin.site.register(Rate)
admin.site.register(Mer)
