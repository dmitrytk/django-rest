from django.urls import path, include
from rest_framework import routers

from api.views import field_views, batch_views, well_views

router = routers.SimpleRouter()
router.register(r'fields', field_views.FieldViewSet)
router.register(r'wells', well_views.WellViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    # Batch URLs
    path('api/batch/wells/', batch_views.load_wells),
    path('api/batch/inclinometry/', batch_views.load_inclinometry),
    path('api/batch/mer/', batch_views.load_mer),
    path('api/batch/rates/', batch_views.load_rates),
    path('api/batch/zones/', batch_views.load_zones),
    path('api/batch/coordinates/', batch_views.load_coordinates),

]
