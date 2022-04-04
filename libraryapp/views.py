from django.shortcuts import render
from libraryapp.serializers import RegistrationSerializer,BookSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_auth.serializers import LoginSerializer

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