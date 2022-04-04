from django.shortcuts import render
from libraryapp.serializers import RegistrationSerializer,BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_auth.serializers import LoginSerializer
from rest_auth.views import LoginView as RestLoginView
from rest_framework import permissions
from django.contrib.auth import login
from rest_framework.views import APIView

class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {

                    "Message": "Admin Signup Successfully....",
                    "User": serializer.data,
                    "Status": status.HTTP_201_CREATED,
                }
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        user.verification = True
        login(request, user)
        return Response(serializer.data)