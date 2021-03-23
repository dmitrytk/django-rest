from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import me

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('me/', me, name='me'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
