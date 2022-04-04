from django.urls import path
from libraryapp.views import RegistrationAPIView,LoginView


urlpatterns = [
  path("signup/", RegistrationAPIView.as_view(), name="registration"),
  path("login/", LoginView.as_view(), name="login"),
]
