from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import field_views, batch_views, well_views

router = DefaultRouter()
router.register(r'fields', field_views.FieldViewSet)

urlpatterns = [
    # Field URLs
    path('api/', include(router.urls)),

    # Batch URLs
    path('api/batch/inclinometry', batch_views.load_inclinometry),
    path('api/batch/mer', batch_views.load_mer),
    path('api/batch/rates', batch_views.load_rates),
    path('api/batch/zones', batch_views.load_zones),
    path('api/batch/coordinates', batch_views.load_coordinates),

    # Well URLs
    path('api/wells', well_views.WellList.as_view()),
    path('api/wells/<int:pk>/', well_views.WellDetail.as_view()),
]
