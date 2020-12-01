from django.urls import path

from api import views

urlpatterns = [
    path('api/fields', views.FieldList.as_view()),
    path('api/fields/<int:pk>/', views.FieldDetail.as_view()),
    path('api/fields/<int:pk>/wells', views.field_wells),
    path('api/fields/<int:pk>/inclinometry', views.field_inclinometry),
    path('api/fields/<int:pk>/mer', views.field_mer),
    path('api/fields/<int:pk>/rates', views.field_rates),
    path('api/fields/<int:pk>/coordinates', views.field_coordinates),
    path('api/fields/<int:pk>/zones', views.field_zones),
]
