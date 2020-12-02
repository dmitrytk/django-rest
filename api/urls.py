from django.urls import path, include
from rest_framework_nested import routers

from api.views import field_views, batch_views, well_views

router = routers.SimpleRouter()
router.register(r'fields', field_views.FieldViewSet)
field_router = routers.NestedSimpleRouter(router, r'fields', lookup='field')
field_router.register(r'wells', well_views.WellViewSet, basename='fields-wells')

urlpatterns = [
    # Field URLs
    # path('api/', include(router.urls)),
    path('api/', include(router.urls)),
    path('api/', include(field_router.urls)),

    # Batch URLs
    path('api/batch/inclinometry', batch_views.load_inclinometry),
    path('api/batch/mer', batch_views.load_mer),
    path('api/batch/rates', batch_views.load_rates),
    path('api/batch/zones', batch_views.load_zones),
    path('api/batch/coordinates', batch_views.load_coordinates),

]
