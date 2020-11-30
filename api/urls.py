from django.urls import path

from api import views

urlpatterns = [
    path('api/fields', views.FieldList.as_view()),
    path('api/fields/<int:pk>/', views.FieldDetail.as_view()),
    path('api/fields/<int:pk>/wells', views.field_wells),
    path('api/fields/<int:pk>/inc', views.field_inclinometry),
    path('api/sandbox', views.sandbox),
]
