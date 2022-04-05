from django.urls import path
from libraryapp.views import (
    RegistrationAPIView,
    LoginView,
    ListBook,
    ListBookApiView,
    DetailBookApiView,
)


urlpatterns = [
    path("signup/", RegistrationAPIView.as_view(), name="registration"),
    path("login/", LoginView.as_view(), name="login"),
    path("books/", ListBook.as_view(), name="books"),
    path("books/<int:pk>/", ListBook.as_view(), name="singlebook"),
    path("book/", ListBookApiView.as_view(), name="book"),
    path("book/<int:pk>/", DetailBookApiView.as_view(), name="singlebooks"),
]
