from django.urls import path, include
from rest_framework import routers

from api.views import field_views, batch_views, well_views
from api.views.foo_views import foo

router = routers.SimpleRouter()
router.register(r'fields', field_views.FieldViewSet)
router.register(r'wells', well_views.WellViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # Batch URLs
    path('batch/wells/', batch_views.load_wells),
    path('batch/inclinometry/', batch_views.load_inclinometry),
    path('batch/mer/', batch_views.load_mer),
    path('batch/rates/', batch_views.load_rates),
    path('batch/zones/', batch_views.load_zones),
    path('batch/cases/', batch_views.load_cases),
    path('batch/perforations/', batch_views.load_perforations),
    path('batch/pumps/', batch_views.load_pumps),
    path('batch/coordinates/', batch_views.load_coordinates),

    path('foo/', foo),
]
