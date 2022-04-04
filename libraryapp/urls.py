from django.urls import path
from libraryapp.views import RegistrationAPIView


urlpatterns = [
  path("signup/", RegistrationAPIView.as_view(), name="registration"),
]
