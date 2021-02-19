from django.urls import path, include
from rest_framework import routers

from api.views import field_views, batch_views, well_views

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
    path('batch/coordinates/', batch_views.load_coordinates),
]
