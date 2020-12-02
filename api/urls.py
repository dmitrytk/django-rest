from django.urls import path

from api.views import field_views, batch_views, well_views

urlpatterns = [
    # Field URLs
    path('api/fields', field_views.FieldList.as_view()),
    path('api/fields/<int:pk>/', field_views.FieldDetail.as_view()),
    path('api/fields/<int:pk>/wells', field_views.field_wells),
    path('api/fields/<int:pk>/inclinometry', field_views.field_inclinometry),
    path('api/fields/<int:pk>/mer', field_views.field_mer),
    path('api/fields/<int:pk>/rates', field_views.field_rates),
    path('api/fields/<int:pk>/coordinates', field_views.field_coordinates),
    path('api/fields/<int:pk>/zones', field_views.field_zones),

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
