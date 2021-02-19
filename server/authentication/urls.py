from django.conf.urls import url

from authentication.views import UserRetrieveUpdateAPIView, RegistrationAPIView, LoginAPIView

urlpatterns = [
    url(r'^user/?$', UserRetrieveUpdateAPIView.as_view()),
    url(r'^users/?$', RegistrationAPIView.as_view()),
    url(r'^users/login/?$', LoginAPIView.as_view()),
]
