from rest_framework import routers

from api.views import field_views, batch_views, well_views, sandbox_views

router = routers.SimpleRouter()
router.register(r'fields', field_views.FieldViewSet, basename='fields')
router.register(r'wells', well_views.WellViewSet, basename='wells')
router.register(r'batch', batch_views.BatchViewSet, basename='batch')
router.register(r'sandbox', sandbox_views.SandboxViewSet, basename='sandbox')

app_name = "api"
urlpatterns = router.urls
